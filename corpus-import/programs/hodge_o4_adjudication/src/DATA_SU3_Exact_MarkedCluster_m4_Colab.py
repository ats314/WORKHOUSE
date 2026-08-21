"""Exact SU(3) marked-cluster fourth-order engine: count-gated Phase 3.

Import and self-test deliberately stop before the fourth-order coefficient.
The explicit, count-authorized physical entry point uses the exact
state/Fierz/H0/Gram/resolvent core, a strict local Haar
router, and a typed ``P -> W1 -> R1 -> W2 -> R2`` schedule.  It also derives
the pure-six local projector and its endpoint DSU adapter in exact arithmetic.
Phase 2 added an exact, support-labelled face-insertion and rooted-cluster
assembly layer.  Phase 3 adds the endpoint- and polarization-resolved full-T1
operator moments, action-decorated histories, and the translated operator
convolutions required by the folded fourth-order term.  The old scalar
five-face path is retained only as a diagnostic and can never issue a seal.
Production remains fail closed until every member of the sealed, conservative
Stage0 triality-candidate closure is evaluated and sealed target-blind.  The
candidate filter is necessary, not sufficient: no Stage-I amplitude is reused.

There are no fitted targets, retired coefficients, or Hamer data in this file.
The optional Hamer comparison is a separate terminal diagnostic and is disabled
until a construction seal has actually been issued.
"""

from __future__ import annotations

import argparse
import base64
import errno
import gzip
import hashlib
import hmac
import itertools
import json
import os
import secrets
import shutil
import sqlite3
import stat
import sys
import tempfile
import time
import tracemalloc
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from types import MappingProxyType
from typing import Any, Callable, Generic, Iterable, Mapping, Sequence, TypeVar

try:  # Colab provides SymPy; exact local Haar gates do not require it.
    import sympy as sp
except ModuleNotFoundError:  # pragma: no cover - exercised by the bundled runtime.
    sp = None  # type: ignore[assignment]


N = 3
CF = Fraction(4, 3)
REFERENCE_E0 = Fraction(8, 3)
PHASE3_STATUS = "PHASE3_TRIALITY_CANDIDATE_SWEEP_READY_NOT_YET_EVALUATED"
PHASE2_COMPONENT_STATUS = "PHASE2_COMPONENTS_EXACT_NOT_M4"
PHASE3_COMPONENT_STATUS = "PHASE3_FULL_ASSEMBLER_READY_NOT_YET_EVALUATED"
PHASE3_COMPLETED_STATUS = "PHASE3_FULL_T1_MOBIUS_COMPLETE"
SEALED_SOURCE_FD_ENV = "HODGE_SU3_M4_SEALED_SOURCE_FD"
RESUME_AUTH_MEMFD_NAME = "hodge_su3_resume_auth_v1"
CERTIFICATE_OUTPUT_MEMFD_NAME = "hodge_su3_certificate_output_v1"
RESUME_AUTH_SCHEMA = "HODGE-SU3-RESUME-AUTH-v1"
AUTHENTICATED_EXECUTION_ATTESTATION_SCHEMA = (
    "HODGE-SU3-AUTHENTICATED-EXECUTION-ATTESTATION-v1"
)
RESUME_KDF_ITERATIONS = 600_000
RECOVERY_SECRET_PREFIX = "HODGE-M4-v1-"
RESUME_KDF_DOMAIN = b"HODGE-SU3-RESUME-PBKDF2-v1\x00"
DIRECT_FOURTH_ORDER_MAX_MARKED_FACES = 6
FOURTH_ORDER_MAX_MARKED_FACES = 7
O4_TRIALITY_CANDIDATE_MAX_FACES = 6
O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256 = (
    "4e7f5acfd5610a2bd434e88f94c6ba2ba12a258e618a1249f49472f76c5dbd73"
)
O4_TRIALITY_CANDIDATE_PREFLIGHT_SHA256 = (
    "576a4a3f00a41f1805fd015836107fb27ebc44190bd57629c13c17cc28e9f16f"
)
ROOTED_SUPPORT_STREAM_ALGORITHM = "REDELMEIER-FINITE-GRAPH-v1"
T1_POLARIZATION_PLANES: tuple[tuple[int, int], ...] = ((1, 2), (0, 2), (0, 1))
O4_TRIALITY_CANDIDATE_MANIFEST_STABLE_SHA256 = (
    "748e72ec7b1cffa42b5c8b9fd73be9be0da29956a8541ee1af577c2407974c94"
)
O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY = (
    "40b8bcc72b0b6d310f1b556892190090d6be76cdd82fb6520e385c0ecf9bfcb0"
)
PHASE3_RAW_GAP_LEDGER_SCHEMA = "HODGE-SU3-PHASE3-RAW-GAP-LEDGER-v1"
# These are the reviewed, canonical numeric-face keysets produced when the
# three rotated 203-support closures are embedded in the sealed 93-face patch.
# They are deliberately distinct from the coordinate-face digests in the
# geometry certificate: the terminal verifier gates both representations.
O4_TRIALITY_CANDIDATE_ROOT_FACE_BY_POL: Mapping[int, int] = MappingProxyType({
    0: 45,
    1: 44,
    2: 43,
})
O4_TRIALITY_CANDIDATE_NUMERIC_SUPPORT_SHA256: Mapping[int, str] = (
    MappingProxyType({
        0: "b5fe728a050e90bd4f90e47a4f7f67ed71387b60621548aca241f14b035412a4",
        1: "99e7006b23cc8246b0c756debfc5c7bcb9ed41cff83eebcdb3f7bfa51f9735d2",
        2: "dec80e1ca5fb5ffd5e102aaa82e2a9fb583534f63507abb4fbaf0257c7374025",
    })
)
O4_TRIALITY_CANDIDATE_MANIFEST_B85 = (
    "ABzY8000000t(e#+m0hSa{ZNoo+Tg-b*=W(Vs~LLu<!zVc`zCcL6=mwuvMzIR5dg0!Th^Zb<GPiNoB@ig<!+*v{;!ZgTWvp7;)ma"
    "!Rq#Qxmg{y`|au>Ti&gH-QTTlm#4??-|vqP%gz1c;bHIzkoj=1I&8Aj!|})R^ljy)v%#mqRGiD^^R;9v+-x?R*=D-E8LzjK`OHmL"
    "*<?J+#=GnW;_^S(jTh_1cD@-eCaYckFZ0!QkU#YC;oJRj|L|k*>9@i6<Ktm}_`2NfZy&N_{({Z@@tAEMvh7d*cvyYS<fq&H;oqZ&"
    "<9>CU|H)7Hhua_j@zde{`B(gOfBb26_dWmVahsj;ho7GQXnB9!X2)#1Tpb_wyVd65{R1X~@dD$U?QXlv|5v6ib8}!Zb34qYlf}+W"
    "*6Y=HyPB?UZl;sTWV7C7nQXUMY!;gp-rsS$e>`ro_b1<AvYW2Pv)wG4&DQgYn@_V`MDxwYO;?yX!P?EnJCVh1JK4==SvHwZX6xN%"
    "16j?c)4}h<K|U|{hyCU}AN&8ymf!ZLhx@O`)!kWC$Y*6ZaDz{7I2h;ucQPDI2A{^m!Sv~$atJ6tp**AGeB|anmsR$V9kSEu{K(ba"
    "djIwD{_(W@e$00JUzeN5xAF4ytQRfW-5>8BZ&%Cwk=b#%&PQwqpKkIIxA&*VW42sp`G{<Jo~!)t4~KjP_dn<J^){~$$H#0qcv7~<"
    "yX7%kZN9D6x7i!W^XCpe&4z>f^(j04oKIc$>$lb8DSyn1jy~Q!|Nb(wU$gtW?5vu<<o|M7o^q^*EC)4lE|=2xZ$C~?LU>n>Tql-K"
    "Glv&Yr{&}6{1>~`?J39hB7tr8{oz~Td7m+K!||8l;C~<QANJYdVY%Ane|-MR%`q3{a(n;F;g{8MyL^$w>$e`W)BWxFL(Vc?ZF7u="
    "?3ZP(j9Ed#$NT$S)tATnht<RW{*a5|>tXqDTpdnNQu#SM?sxlqz**`~%5ePg`ux(jELY$2?<{=Ht6cAo>;1zrU*TVK31q+KgEskp"
    "uO7Gg|2?mz*QdQMuxA8!tJA+v`7E9F<?#&g<(uDh>s9*Ce|}cGH*w^DbX=YPrfN~<<F;X^_k|>Dm#?*Kvzogbx1Mk2<FV`(m@Y8S"
    "Hg0@_+@NeG(@AzS0VYl+<5jj<V=6bBId*P7D88pMJFjS*jN3-N+q>C(wOdTa$c@@!lD~d7&8=Cs%Q3j!cD2oJ-0o(a<^M5VPqO)T"
    "F~)R<o9SkO^>(~k6tR3i-k;}jf7tA|+2LIe=I5o{Jn9Y0Y`e%MlG`k}@oY1h%yT)-#y9ivZnDj$o7L)O?xx$tZnKzUv)gQMrrT`o"
    "w)3f5Z#R?eq===(yx`fs<nn$pFixH<4CKkgxZ+&DPF=oAK7W?s^Z($>m*MBnBfS0Ru=0}(Uw-uc^zx%?`Uwp`RiEb?eu4KFyuQ`<"
    "Q`3vk@FKh;_5I|397^a$uJBWfC`TyDGJ0Uk42<wP1+Tv~2>pGa3%<HCsSPvi9oY72M7_Eu9TznY5#!MMDW!pN01*Q)G<#B>yol$u"
    "OS=B5>M{!qLwHze0k)2d0*4rIm37)WF5<25f2)g=oC`}1F#<;H3i9f%Zz>Qs6^Q$creS4c`eOeA+Wz!Y)mHiUj#24zgHObz1B0(d"
    "XiCIupyS3xJg*&KgehncMt#R^9ft6*%3eH*(ZArZz|&BerSQOr_u_qG0^=m|y%P6YkB||tL4jeVry)WCUY2igVLXkCSQiqx#^cT{"
    "wQ(({K<_xu@h-;XHbD1^4?#=XGR*%KF0g(A!vasMub;+&5(O_L<mLl)%dpDR5H}Twn+iluMdP@r=LP+thABg&gb^oUL`b+U)OH`N"
    "JPHBt?tN6~SuMU@d6-1J60OeV^QfBbZyMI<CRT@qks;vr7Du7gISz}zI4b<CfcOz5eng4CI4T4zD1Agp9}#jzFk(;~h4wIoi_z=S"
    "sW?2&`HfKHxaNRJZCK!Gt+P-W7x7lagm})w;$(uLOb{UxiJ1QCC<I5jaK!3)SPU>10W2_8;RsiKRQOqldnKY?84|3E694Nc1fqiP"
    "quQSpAy*eAR~IE$R}fgtD1Q{Q=+m}_J4c9$eHI*$=1)M;V+aIUM~Dl?##o}-xaJ6MNhs07&>lo?HCVoJ?UCoU!vdmCbmdX4(86of"
    "H>&+vE+)SIJS_Z57yL>WA&d9fL?F8VIx76Ec2S^VjW)Z=J^bsib9|8#*W#f^y$Kh;DfaLY5?I*3z6hSX93C$Iqjo>+5^pQ^9A5tm"
    "T<G^*@(x_+fugfJ6z_q=qr!!#5Vh-HWCbo<-JKR-S9Om!7X8<A&(+gqU3AgkE?U#R!uqWQUHwy>gc7hX=d^{#!^2bBQy~lD>ml2|"
    "WY+An{6{yNES!7FaX37sp)FemPaw0Wu`elW%guAXP5u*Riz$jfJ>}ID{&qZ`OX+XR894Qk+x;mDlyl?xOwNf?=WM0tw4w^CmsBS#"
    "5BYE3^FM)LGAaD~_htU@$K&Cg400o$A5OJjeqL=J&na5d@p!R#`*-*H3dnSJGb{Xi;T6-x&CSH~)5-JO>uWG}Z~r=O_>OVYcZ?gq"
    "V_f}?w=Axg0mVO@VLH#>R+@r*`hMI!C#Jm$eLM#6mNmFP{G3m7{=CQa?f&%5qZzZs+u*zX>2%JHEM#KUw8OoPZhmC0LgW0YPpNXx"
    "DRRFL2ie^^+iuT~zk9rW*gvO+{b)!E8b9R%-3$kdb4Jkb=TyGKewUp}nU(9sdb63kwXA2`F=U7JbUItyINXTb$ac2Q=CjRqyKuYp"
    "Z0aN%FQyyGHoKekZnKubOMc+0n4VflG5T##OfNj=y1gXYJ?GH9$$fLXIz6Q%6%V@AS$a(aJ4^2=^$>44bCo~+eOQ0-OOjpVo2%(I"
    "5jf-(h${hUd{ReP4fkgqVELcqgB6&j#sr>Dpfp7#T9T4DL8SzR=;=$U>^5~B=4P;-S7KlRib-45lqAzZQlf`R&3tNOGAAd`?Yu2W"
    "um$Pem;dN>=g)EYSPSLNr?516(sS;Ff(f?tsg!W^v4@tX^guHcSj<N;1WH=X)JLqoV&ut+k%FC5l=lMB(%c!eQVM&qa6p-}oE8md"
    "|J|6PQ+*WO6^kn_pUcS`#Bte4j(cub$c2oy%f;G;Ip)DVK|6Ip$2_<@XpVA#sT@Mm4dJOquxL{OF;B+A5wU1X*pc*@wDiD{F*q_V"
    "6#A$xyqM>9hfLW=gtv{99}N;@5Fo2BKH=?q)mnCCDHC<sDQ_YXk5vThIDoYzOgRe)?I<LilaO>f2!-M$Q6v}r;nKt_6zP)GmjhRM"
    "+u$#^Yg=tl*9XUuucMhW#}P1ROBTwGEUXP#DEqOnwqw>wnCBpoybZ7{1m}Q8JD)M&qU3%;Iqt)7@xgTE7#0mgA451Q0g_6PHsvZ}"
    "^P92{u<2mywZ&RNJGZm$48S_Lvu+H)JGoOrJ>VTIN1UBmXjYgLv8*7rAFuQPcDAo@!8;6dt~W5`ZglEO>}Y2RRw{xc?i?IL;aG-("
    ";&ME>NQENL3u+NQOpjkN<BIYoKu)R=j%El~F?3Jzh+&&Gb<p%7hV7)K7s#}=$2eMG_;Man7xQ!Wx-0S#d)ZmKK#qBEFVN6F5k)?@"
    "2WXCR&{79c;k8y)56-rYI5O_un2B;0l9+`dWqkup%PK{keqCG8j;PPARPY*@iE<W_m_=F2VCgf6`b^phLEQ<V97T+Kt|nwhf^1)("
    ">z<(fJ*A2n`jiveD^Pf+y6U4rf~-Uf!E(4scW0o*G)Q#{z9)kNn6vIcT6f^BJCbn&O^d<NV)L1W)s}TmGn6Q#aBT%K>%xzT7*}K3"
    "s(roe?;gsuP5k{?-$7*`fkgdm%syud?PM%0z(Qn?qv(Wo3@!oSNZu<m8WBl~)s<hOLQ}1Yw>L{i`;)-|Op-7|A)ve9d@XhK;gX~a"
    "3S1>+Ah{bv>MoK;r_Ab=z-v~f{7S0BAvQ2;CL+WXX3YXa`^ZDy;h=rwAs->YI`V*pmv!U;OCeZC9*`Cs>BvKruMqV?D0q9S1M6y0"
    "s0j&_3tVC5BXI7?g_(~)NudyOiW?zOMVR;coO~c*-s^Kx@<6*=q@_L*^I}N}d0>UsSV@my#nxy^yu=hSR<blH3y4!Y7Wdr#kX3~&"
    "yoB`9qbWibqKt(jVo{ecNO}yO9;3ZVxIbhlL#FK0!mCi=aPh=Fw?AZU1IH?<5YFL3x)oH!^gp1S-h@_75$+SM0a(8`k9Hh3;<5cH"
    "@KrNDVxHSeiM69FEM8S`*fydbs|FYxz@PwD-|bwYq*nrBmKIY1JN@>AMYmcHapQAM?jEj`k_nEGK@u_;#zHe1E3~RX;Y7TJRx?=b"
    "Deu%xMbl%|0D}XVC1DVBSfcI3MQ1jGqvTkQlH)i^j^-%2<^Z|^UcIn<>w`go3kF;jH`LMGP{%w-u-s6^bgS@FIdB~XE=jtez{S;Q"
    "FRfQC7coVFi;1cFfC)NL%uH1UEF=?LOik4XOp>s^2?p!L1Imd9tP>9?Cmyg)Jm8#oKs)h(Wr3Obt|SSQ)*C464XpLX+22~Xw@7~z"
    "oI4HB?li!;(*W&G1EebgB)B5by@mn*ihv4ODaym36X@12?gMQ^7bY4L!o@XYY1a|kCYR{ej_(7n?J1l&ylRdbV7(BqaMGtp<R}s("
    "F;RfayoKZ7B}iBE!bM1lX+p_M>q0PcDO$C=mJZ}1HY6K)(PB)nx*-RSMToy+v0!hbZ&+-YFU|WE`qrE1enlNE`F4eaSMMOEd9^}f"
    "5|JR~hbG+idzG$RME_frE;J&2&=M4ve4|1^do_9>Chyir<RNJ-*p=-MtnGngZ>gyx6xsG(XOt+vP%9Te2CSLzU3)MGuJvlu3SiwR"
    "9v3gQkcEVpSI9yHtgR9R?~+qtL3D=`6j;yz!+fc939xFJkV_z8h8fn6KT(J)gi@{`9jX;#eK*Gl^EyuaT)j|1NOcNL&xMv2cpgdt"
    ">lk1;k_7`SLk*zdVWulq(Fr$DYE^jA5k{$sFe+7qRH!11Iu%J>rlO9PevQJw%TrtqT78?V6V;<srwFAuCG=E-G1H`_DLl9gT@Z#U"
    "&<ayTU$kJYGf>tUxhREzm$60Abb(fp!ji4tRf=i?cbaku%_vBcatR_}>pYm?<Z#pYlt}d2G`d4@QcFo}k{o7j8d)buIfbkkKln+7"
    "s&s2KmMRKk4vR2{!k0s%%OSB+gSD|Sk{VDVgIDHCCa435H06Y)1|I_)C9z-2l(i%7-!+18!3rL$I;~?1cpT-db|RoLXtO%DfJUKB"
    "Yl{OKi8ifY66(21ps@=G1F?A;ZO{maSuO19h&fp=N>?smQu#7&Vv&Z)mkF4y5WUhKK%~Vb<iDUBDegyI&4b5@D-@rD#)!*Ef&q^a"
    "myy8-9wROxc?&JPpRTV*=g8+X4`LV${~^FRY%8e~X&91|$rtvD%)#SGW~5Mq$B`_F^?}LI3FQ?>%s*oyW~CSK@Pd+TqHlt!IcP$V"
    "uF)JcB<DwFX@eL{NJMgeWRf<J645k6JLyXL8F)E61x*_)_Jcqta^wrc>rJ}R9Wf=hYXnZyE_CC<?Up{LbYM?I(5a~vB!<p3h@IYr"
    "r(-U?DrD$EE<Bosm}4v0h*d?*2TZu^RNe48QR99XqY+r#xTN++=){fNU%U!%g_PMYl$}{W=R^o;%;>_9+ey687q8ycOJcYh`8?!<"
    "r7lk{iB~^p(JdPXy)Zj1?TAB_%PJ~r!t462Hdo1#VjRspfYA#u`LtfeYqBX%JKVm~bt$E5uqhf+Q&U6lpssqOMZ1C{aZ@M8D~e|w"
    "{>fM2PK)nnYF=q2whqdE1;xwMyU|ME!>e9sv3N(r7Dov%bt}dY=0j$hH(I0cHG?+X{x@2L5=m4^Xc=`xOvDt<Q8r*b5xWFR0d2kl"
    "$FLEcdJzVhJ(BPeYj4RsT4KjI@K8u|N0cgRVHGq4bD{g=)g}jVlqj`hk%P1q`RKxhrY`6esIv%ZM-&18NmCmjT<I!Q22dIiq6;H!"
    "7t0`A>59=p5h^P!h=+#qQ?)G_SsScUgEZr%(Pb(t1HVQ@2!Lr>_WG+$r9^~N6+ojY4(0Ew!?oAu52<O2IcrTgN$dSfL?m^E2w|mJ"
    "ZNh-WOvOSnytI8nC~J*aAi|O^lqjQgqYYrC@R4Z5z)IR;u@TV7NF62mL?p~)xWuedc@~=nr&OMHvEoRCj*fTT=Ex*?94V71HM|UM"
    "pdz+ODd#vW6^@qt?K&lYcL1!W5sd6_$4aMmymV?xXx*_w>mzVt>yFgzjmAXkDB)^XY%{B?z@RCx<H(m|fZwUN)x`UB{3`^$HFGpv"
    "rOAj=Uf(n1pbMh{SvZh2<Ls`=crS{8S!z)O41K^_xjQwyswx5f<ef?#j-p0%Dv=J|B75ON9j>-I5G(|xLOKavhC$OUBWnk2eYq*#"
    "8#)U4`U_s_F~SiH1ZlshHG^YFSgzpE1C~i+9V|gxbB?1Dlp{p7?~|T{V|*@4t*WY!byH*r&8n)YOxiNmPP4A3UM1?SC3<i{Y09a("
    "=)gF-bNWU~)SarKwww}mX>F-dYaOw!RU_Omw?Wp*O;f$Y4+7Tf=&Wuj9LZ8Z{Scp|!H*g{h(z6*Sn5GtMNCT(P6k;)$WV8lI}*vq"
    "w(<Z2E@-QcB;N{PXSS7{7qHzvVD+8CSNdV5JCPTz-L_>OxRHhRAJGS_0WH02ndqVAsDkR&h7?`Pgbo*`I*zoV1+n^Nq-V%TEvk~>"
    "C3bB939hr$WFiDtsQ^ab-9!S{A`N6M6;22kruxvd!4+oP9O1xa7~m00y!QGbhw(Z~J!M01t+fbj!wXhNIL>M_+0d{Zu(^JQVYsGh"
    ")kAR6lkkWUtFC3FX<ow7;X>1m*S|9C(y`-Gv}!?zF6}yOh*ptSOelA59a?pCRfGQiC8<#dfxSXv>h!gRO94x;2Rud4IOXa`aTq0K"
    "F2zPx@=Tn?3d4557Ar4W;hL-IZ3EnHcTJqcE{KwSOn;<yyy~r3Qvf!1`%Y@nA>j%iO}x^3wWT{ih5~w*q2+6?YB(<yTxZxxqlfbP"
    "FqcaV+2R!(A=%yL3DVUF<LL+aIh{FDdX-SVwA2oVBuL;CeZ1WCO+H}F<U%MP8F&=0gyjEHC82Vo7D^3P4Y0G@S;hw#b~|0v%vh?%"
    "9HIsn>NhFc0d%D3%OPyE*7|a^!nN0zBM8@-BHs_dg)KJl7PRd96b4+FJg9SWH}%=TgK!O|@=B82O<@`aM&>3Tu%_Dv@;=OK9ML;*"
    "Q&@SM>aFNPaBYV75~giR??f^oWo_y=&I`ab*0QGsE$@^=S!pI447K95*Iy_I*O_W56M&1}zOa7k8!k_M`$)nGPLm5BF%4KZ+4`OH"
    "TJS2XgWk3V)(s|!91OHLx}(JPSf#l7JwyU<yP94hfsJ@-7vTy?6(XK$Dhw$pIPLTZ8yeyEb1p*<1_drm!c`}1pjrlf!Un2kND-4("
    "iukwV?X^u1PQ22MD9{XATn}2J=IY!83auShQoQ^<SQ&1wG~UF@s~_KGD+5@x2NYe<*(CJ0V01W~Uy4>Iw<Y{geXL+$g+A6^(U6Fz"
    "n!3N1ZmkkOsDe>CwMp!w3c}C?BC8Wcvi5>vZ9Fh9o`tE_&;i7-mrf{2_;?cmHb}83-MDx^s2xGu=HnDYV{G9{U+ciRLkT5&nIbcd"
    "$V{_)Eay~OCJ?Q`1o?2fs^)173@3tGXUQ-KG{!WFaG7<M9O-g+xtVB<Wygn;(To`dq>X|I1FOZ$zDCAqXE1A_9WTt~U`c>N9QMv&"
    "m)}l)RBf7cqdWf~DiP^KcK(5(Tt3rz3dtHhGa^OACIMip=dgqn=ajRJwwKP9t(d)rNJ?)`(gfisf-v+zShcDQMS#UN0+O27oCeom"
    "7Z*uPYEG1`z08Wb3$1qluYMYD!U}^qu5DP&UFkG~g|$u050%Rg0R~!oC$A>3r2LOwXWBNb*1UygtQ1dIA1o&`foEq!ZtlnQ)ojJ8"
    "oK{1YZC_%hq>8JViA@$QD}ca|tk{g$Hi1>9mE(iG21h|Hc#upDdQ-}|lzL#YG_n~i?D^t;u*6gkf@rPAkebl4E*Mx??S(#@(OM76"
    "ASNhd#daYkDq|#q1ZGf1*TV%lDAPCFrv<IKq}3*@VlWe>4Xd-2X59?cVg`E?T1^v6*Mh#LAf+X^f}<>0kvTeC`^Q6QMdp&Y2_OfL"
    "7?PE1xB)>-@W_mp07mqPx`k0wPefg?#KaSVXw4=jHo;{jo-h=_A_sCCTH8?rkn8vRQl&Iw#Z_R{XPj5#%<;oj*}{^jti~3WP7Ra|"
    "7g-CK3ruHAfZiQGiwn>Xw->){n$Q7st{BsVk`Wi}`Y`g<W~?wA_D1my1h!4k@xt;NE5IeN>N%!5kXiLKj6xl)MXD!HHLliTV|3+g"
    "2W+nUgtvNF)0lxPU#K&%5~B$Pyn5zLx&K5XUS)*<Ss|dc;2eFyIZk;w8LdH9(^jm`8UtJlT9{7wDZsso%e^XIll6mba80|GCAeah"
    "Fr^tUOyBkT(ArJAuA{Y_eP2OKYjR1^1hHI%QNs#@oKFpK6*#IA3YS56%oZ<f*SYxMI;&NBb+EQ8AS-y4shJa?HCzo_L#yNbHsms?"
    "ppD8FHX~cT8<e_m9ap$|tvGoL?G>-<w*$LGq1_5#^aGqER$2fIt@Snn(U+(I?k!=LRKopKLegr4s49f8^+9^7gQV34QcO?xYJ#4y"
    "PXtWLe^&M0K}yB(ak**Y6<U=XM;){?1w5>}x^RigOHc-rjCL((d1Srn!qrS6qF%Bxa`;E@=9Y+;80ICYgQ#jl0^!=e!H(n{zXU7I"
    "gO6k!kBsGj8_RkB|J7Z!1aLbG*ZCBI3AR5+R6<2i_0jlXX=Q%8U=!qAsKeEW^S5;c*GAjFr~@sH0u<4T%Ka3GiC7#qf3E`Tf~DpI"
    "Fu+>Qv><W$)71cK>x+I)?4R*k_QixQTD@Ii1g^h;{{BL`Lv8=M#1WD%G6k1G(h0Zs)lS-F*7s(oxU`bNy$<gY?QVmG?4U?8cN^tL"
    "MX<ITX4J7-&KE3WHO*!NCZj*)-bqrF7EpxC;Vz(vmO~uIk*pYJ=|n8)ypfCD>tUS-k9D3dS>r^VNWtUISYgU60A$e;GRV1bX)Sd0"
    "^*}3rkVvk|MI~Igyly}GdZ0#Ikw~(zUh}WSH=TrWMU!s26!YQ>wznRDTk#;gZ1Dte6?4VeXcb%rkTcYTl_}1btzI2T0@*6`s!FK}"
    "eXT-LqX1TlxZa^ARlxxC@p2+{B;j%>{wbmr^AzNWCi%CL?318SfT9UPQUoFB0V(~Dq6dmGCH}rks1cy!<@JBjR|T<OFA~Z0Z-gES"
    "+No;X6eV@;bZ*VD5_x(WW;0C^BQ9xn5vw+bz9VU^nn_?gkxr2)If;|*;(1VQL~I<3#)w2l;B;w>*xU&&ni<GKw9!SUG+&CAlF91S"
    "a+*`HemKQ6VSZHKk?y8hq%}^p%Q&55$En@<CgCu0s;zhEq*iXIX>`eyR!>BdZzAa*(siXI048Rr)kP+tiF$>sC+0F_!Vc$w+;@}X"
    "-mZE9YZh#9v_cg1xQv*k6lx{D{+bv^#tXv)VlQ|#&4lo+glHNGq1y;iH4&ieFEsU+Z-NyG&qiP$*IwVDSA3G<$Og?LTP3-W5wNa8"
    "7R4@Jl0wF!;Dqu|#n3zzSJQcUdVxq<3k$UNUc~){%r|k$t$T`?ImZg!_C4NmX2(XX9Jb;hhOUfD^Z`hL*e)Zx7qBJ^iuxs86|wYh"
    "i^A=`>IH1MzoG{)^wPVSyEHVaauf7&@#3}2JyZuQsv045g&?*_5yFbIO%7be3la~v8k3$EFpt22Az@O6tx_JSA1{rzk^xtXmx}0b"
    ")c!*=6@{?HDUw$v#;f7y3*F7vqp)OCf7RgjcH|Pco{>D32G|EYa4mD+SKvZ<v1w<v``~Je7fkVLE;i5?8*~>N=WM2xtmaam9b6#^"
    "p)+L1zs0X0R=LG@NdYV5Nu&b|t&5GskgX@9R1o)8<K!|H1+740#K!Ycig-004N8)}53l9C_ZnW!oWN9g4d;@3@TxL;^8hQR{3J*^"
    "DCK~m_qC@>A>#^Svm8=BxLQS&3B)Vv)Qv)itHouJM7(kZ*PW4k79UME>A`Bca=nIEfk`T<E^tV0bjra!U}@cOp^X+C0wLWyPDygb"
    "Ns+E)ZWAw9<JaAye!EG&Zh_`?3zz2CgV%o2oMt)<JsU<d8HVgjNU=Oa;cU+Ay5d92qK{ES3$<n&<dO_gt;k^0-Bj>`MUbd<cC4c{"
    "%>Z6{g<4K3aZ3}`vJv5*8KlN0B(_~kiKjpM=pJpQDbws7M9SW(pw%WmN&wevCl(J{SY~#t;02HPm$1<6bCT8oYdP)-;X1>K)S}0U"
    "mgefG0N540SG$Y_HNeoVDoi0`{Z7AJz~+l%>wrzuSd`#u)If5%N_~J$bCuQsV`!Q-#s}9hwW<%WVe-!!T<c6@9=LY-G(B+D`qZ*E"
    "W3W5bs`~L@bgI=4{EKoGtV`e*7b23*^sP!AEo|ShiKoUGRvVT2;hN3L5oS3wU$~md0%_11CLfUKQs|488L5y|V(T(ZoD?F9GOY<#"
    "DQL>QOcAxa6n^=$#1>?lxJ%J1#^f{8h+^Xa4?!3YE-R2n#Y>3ek?}&e$u1AAN`?TEqU~&Qy#X60Sp9en8|~HTfv9#i;G$J3b4F6U"
    "*Rw$o$ko|kuja6z=a^BQ9rZdNUiMfKu3DK-I=HqoOUr0A6NZE;TNan0X1<W{(uLT<)lAF-d!5lDcWO*TqSh!a2|M;XT!!;Y)dq(5"
    "n*y-)PH7du8cYXCB@E;3nu>5mac?7$&D7v3CWX+Ys~coU0@vAX16qe`x(#R*Zr^;dgdT;{@F-H+-By>vMlBVILn0Ac%Qcn>2qZ+&"
    "RU_3`l0{2M3E{$3xKd4}2mPb_3DrQfv&6V?`<mL6_P~0F!75tw<<`(nTL3e1quDc_&B8#-W+SxQs-iXCE49?!6{>wlIf++wz{a_6"
    "K%%)I@yS4y=ORT652{2ADF{{(&%|JZ@e#x#ai&f%?tK_JkDwKaQ!Y}VStOnycmrbfXA;0r)nBfGxQfU*^y(>7+)E(3K+#5Uw}iKM"
    "X<CYVwK`(!SC>`9uzvmH18lo7d>ygzgn<fR)pW=-a7`zW)bQHwDG659BGJhp1bR|Q*E&;D39#$8DJS5Vsl&C+>r};SpVrBT*xBWn"
    "sl&BRLRG<Qo`cGR*BR!Rslm0r8B=<U@{VSlx>i;jvm#zyQ<es<@lKLuysD-w5ngAx311a1Z1>>1vX+c`9T`(JywvM&m{@i7gF0yd"
    "UybQi4(TL9doAY%cNM+Vi+FpVa}xCVuHiM_`Mr$SeBbvv+-p)_v7h&#U*L#jcrjF?#^+=jRlyohJS)S6X-ZoVE7{m+6>j6X<k6s2"
    "h9!WjP!5z*x=`o$;i2X5`;hTk526d}LOTUmXZ!+4l&-VWT(A|<_Dy$5Y8If7|CCY{t|94Lv+gQE5dfw1DwT9$JugRS_t<3Vx~s@4"
    "6W%>`61>iKUZg19W4q+0*IfZ+P93lD-03o0^lg~pt$y|#A>Im1>upyfK516_B(0ZU<G0t_Boqs|-}_R(bMw`?EAuz!pPQXdtNf*h"
    "`-kP}aktxV_SyOE&jL7YzGZi-!KcB0{q0Zx`RCC;{xu%`Z8G}j-~aN5zy9T)|1<jIAO8DKfBDlN{`u$8AOHHdfBft3e;)me!5h}I"
    "q<$M@ck67s-5<U#?;dX-_TO*wH$40pe8O<BzgvCHp5$3n?=P=kosT#@tk(P6{J)ON=YLx?NaAS{n_e}kys9Dc{JEKy^|OcU(Dw^G"
    "pW!^8;Yy#;^xC#>S~Q5S+&ROK`~4U1LH~0jJwRh?4d0tyk4eL(!utY<nvH9f9{i@j#Y?ZO5pjIoPnzS(jUU3g(!kW+s8Q$t-_@ir"
    "4(m|NH^eJcWY>t#zBaM7r7&z<bfv#(6ADU8uG%Kz(ut@&&5up0!%E-apZ?Y<Lv`6l$oLW?5XDE*uu?tCHj+!~<;{LZi6&cAX&2vW"
    "N!~ZOH&1+6AT&V>p-B{T)n#)QA(9K{tZ`igWKzkV^v^8bL|0iqVPg8Y7CMdVu|ZEND=4)8G_*wOG-pm}owXnF@Gcd!G*_4QeX}Oy"
    "rehyk*O-Uw=zSv4N(K~7$n?2UbIVJ+^PF|r;=Oa$(AvDT&RQiS;kj)$KDA@`Fq*%<MO7-A*JMDOjYVUBzrJ&ZesdP+$}#k}jEa$6"
    "@wnyL^AI+TzSBU1%?o!@h-*d@act~1XHc_^<?DkuSF7=kr0sLt_B~(kH19qYWzVGSxW}Jr+sr_vQsdG&3yH3`KV1FRde^&)eCRf>"
    "xjbXi#ruf?r*bNjMtzFk;r*_#uVbS`Ip==WY&oPv>?o0nUfAxsYOv1c9_UIrjO~coI;j%3d$vmM5}(X@=BsrgB)CcRHaG;Ir`tqG"
    "`NY;_zYwtqE8A<sK`|U5i!pL8WLf=Dv_8}2kz1e8BAU&OM3@_|Rf?2IbxKDF3U1gIFppeXD4+Z#xHo9bR`rUaX}Vn8)+Nmmv`_@w"
    "_Ysr$kLVJ73^xc5t-+`T-4dhrHV_Z`RwbiU()4B{ht@tietaWT7Gh_$a~vb_DwM!E7+%@62Sj4Rgr03b<f(fmOrj<%!db8R5Pb|q"
    "%ZGHGu~Gt9>(xzxytBS<y0}PDDgP<@3Q9^Bn=!#%1Pw*=sCv}-ve}A~M~C>;g<BokZ`}g^jYP-)+b0W+Pm6JI5aCq$ZoV&`E>JuY"
    "-|^5z91jr{_eJoGBklJC(zu!<ZCohZA!ZXsm(|rL(m08Y=wIOS1%>Rre{bD^F9?CeJnk}yG$~zOPY`j%5$r`03`Rg#BDh>4jjqcG"
    "5eqTKdPQYNT;Lf-OQc*{(p5<iWlS#0M~OFd`XcGHY+4LSjOP+-H6_9$iL|Ye5<%B<=0%xuahsX%Y|(xiXtYT!JAU{;6uX(WpN@j("
    "v)Dbh{n+F;q?4Y9qyAfONI2n%>tL19VGbe<@g#nYML)d9Rd>H#t8H&;-{%@6dP!<*%t<=9Y4$pxc3s$>6MvT#7yS)d7P;S?1g*}n"
    "Z|?Nv+k?XUI~erK{kiVj)&(o-O$Vp?RzF@LT?d1uw-Ei?;4~QIRwy%w7l=ZF|4_G1;Y+a^AyQHr)fr!Y|9>1h{t<3Z0{{"
)
CONSTRUCTION_MANIFEST: Mapping[str, Any] = MappingProxyType(
    {
        "status": PHASE3_STATUS,
        "arithmetic": "Fraction/SymPy Rational only",
        "schedule": "P->W1->R1(Q1)->W2->R2(Q2)",
        "w_domains": ("P", "Q1"),
        "w_forbidden_domain": "Q2",
        "haar_allowlist": (
            (1, 1), (2, 2), (3, 3), (3, 0), (0, 3),
            (4, 1), (1, 4), (6, 0), (0, 6),
        ),
        "pure_six_backend": "EXACT_10_INVARIANT_DSU_ADAPTER",
        "phase2_components": PHASE2_COMPONENT_STATUS,
        "phase3_components": PHASE3_COMPONENT_STATUS,
        "cluster_geometry": "SEALED_STAGE0_TRIALITY_CANDIDATE_DOWNWARD_CLOSURE",
        "fourth_order_max_marked_faces": FOURTH_ORDER_MAX_MARKED_FACES,
        "direct_fourth_order_max_marked_faces":
            DIRECT_FOURTH_ORDER_MAX_MARKED_FACES,
        "support_bound_authority":
            "v24c: initial+intermediate+final P faces+four W faces = 7",
        "candidate_filter_scope": "NECESSARY_NOT_SUFFICIENT_NO_STAGE1_NO_AMPLITUDES",
        "candidate_formula_naive_upper_bound": 9,
        "candidate_exhaustive_observed_maximum": 6,
        "candidate_xy_concrete_supports": 203,
        "candidate_full_t1_cluster_evaluations": 609,
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "lower_support_extension_lemma":
            "PAD_K_LT_4_ON_OUTPUT_FACE_USING_REPETITIONS_THEN_TAKE_CONCRETE_CLOSURE",
        "vacuum_support_extension_lemma":
            "OUTPUT_EQUALS_ROOT_ENDPOINT_PHASE_PLUS_REPEATED_FACE_PADDING",
        "face_insertion": "EXACT_STATE_MULTIPLY_PLUS_EXACT_H0_RESOLVENT",
        "global_blocks": ("A", "K2", "N", "J", "C1", "D", "Sigma3"),
        "endpoint_resolution": "FULL_ORDERED_FACE_X_FACE_WITH_T1_POLARIZATION",
        "folded_convolution":
            "TRANSLATION_EXPANDED_INTERMEDIATE_FACE_AND_POLARIZATION",
        "legacy_scalar_phase2_can_seal": False,
        "checkpointing":
            "TRANSACTIONAL_PER_CLUSTER_SQLITE_BOUND_TO_SCRIPT_GEOMETRY_AUTHORITY",
        "geometry_preflight": "SEALED_609_CLUSTER_CANDIDATE_CLOSURE_ZERO_PHYSICS",
        "cross_cluster_cache_policy": "CLEARED_AFTER_EACH_CONCRETE_CLUSTER",
        "physical_embedding_coverage": "BUILT_FROM_SEALED_CANDIDATE_MANIFEST_AT_LAUNCH",
        "construction_seal": False,
        "hamer_terminal_diagnostic": False,
    }
)


SOURCE_AUTHORITIES: Mapping[str, Mapping[str, str]] = MappingProxyType({
    "stage0_triality_candidate_geometry": MappingProxyType({
        "file": "ENGINE_Y4_hodge_canonical_o4_production_colab.py::STAGE0_SOURCE",
        "sha256": "914F5A36F6E66B74275E9CC7CC25A16201B263F008FD4F76EE4746BFCC10A655",
        "locator": "embedded Stage0 geometry/triality source; ordered signs repaired after canonical geometry",
    }),
    "state_fierz_h0_gram_resolvent": MappingProxyType({
        "file": "sources/NB_HAAR_hodge_electric_resolvent_v06c.ipynb",
        "sha256": "FFE7952C6BA159B3552E7BA001977ED46A8FFBA251C115D4988F7FF4B367ACE1",
        "locator": "code cell 0, extracted lines 137-472",
    }),
    "exact_haar_branches": MappingProxyType({
        "file": "sources/NB_HAAR_hodge_explicit_intertwiner_v04.ipynb",
        "sha256": "4EC79A84F0C22475A9CA868233C16A269FE90F537932904B00D709A836D2830C",
        "locator": "code cell 0, extracted lines 90-160 and 308-504",
    }),
    "mixed_41_exact_algebra": MappingProxyType({
        "file": "sources/NB_HAAR_hodge_mixed_determinant_v05c.ipynb",
        "sha256": "2F12EF86AB494F675F144C56D5D7E4174AF003E2FE0084DCD4E39F9F364EDA48",
        "locator": "code cell 0, extracted lines 75-167",
    }),
    "rooted_incidence_recursion": MappingProxyType({
        "file": "sources/Hodge_v10a21_Exact_Rooted_Cluster_Adjudicator_A100(2).ipynb",
        "sha256": "00678B0602ACC6DFD6A594ADC34FF5698154F0A8A1CF878CF690D1BE82EA0D27",
        "locator": "code cell 1, extracted lines 6795-6818 and 7072-7127",
    }),
    "full_t1_endpoint_support_bound": MappingProxyType({
        "file": "sources/hodge_v10a24c_RootedFullT1_DualColdOracle_O4_A100(1).py",
        "sha256": "935A3A5BA680D1373A5842486B10231D83232D8CB3393BBC250351BC51A68C8B",
        "locator": "lines 6670-6729, 6948-7043, and 7197-7219",
    }),
})


RESTORED_PACKAGE_SHA256: Mapping[str, str] = MappingProxyType({
    "ENGINE_Y4_hodge_canonical_o4_production_colab.py":
        "1970C63A426812BECE12B1BE1706958FD8EA9ECFBEB3D305875D40FF6F2266B5",
    "NB_Y4_hodge_canonical_o4_production_colab.ipynb":
        "7A7840BB6221D4ABF360A1EEDB182832604CFAACC0A207ED8AEB7FB480776D07",
    "test_ENGINE_Y4_hodge_canonical_o4_production_colab.py":
        "A0E89BC026F272040A9186F2A284AEBC6363EF8335B42380D99A3BAB12EDD557",
    "DATA_Y4_stagei_authority_fixture.xz.b85":
        "718270E59F921F32D7A576E4D4A36087667009F65D4A90C0DE76539E377DCEF3",
})


class ExactEngineError(RuntimeError):
    """Base class for failures that must stop an exact construction."""


class UnsupportedHaarFamily(ExactEngineError):
    """A zero-triality family is outside the audited allowlist."""


class ForbiddenHaarFamily(ExactEngineError):
    """A specifically poisoned local family was requested."""

    def __init__(self, message: str, provenance: Mapping[str, str] | None = None) -> None:
        self.provenance = MappingProxyType(dict(provenance or {}))
        suffix = f"; provenance={dict(self.provenance)!r}" if self.provenance else ""
        super().__init__(message + suffix)


class ExactProjectorUnavailable(ExactEngineError):
    """The family is recognized, but its exact backend is not installed."""


class IllegalScheduleTransition(ExactEngineError):
    """The typed perturbative schedule was called out of order."""


class WOnQ2Forbidden(IllegalScheduleTransition):
    """W is never defined on the Q2/R2 sector."""


class ProductionNotReady(ExactEngineError):
    """A production result was requested from a deliberately incomplete build."""


class HamerDiagnosticDisabled(ExactEngineError):
    """The terminal external comparison is disabled before construction seal."""


def as_fraction(value: Any) -> Fraction:
    """Convert exact scalar input without admitting binary floating point."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        return Fraction(int(value), 1)
    if isinstance(value, int):
        return Fraction(value, 1)
    if sp is not None and isinstance(value, sp.Integer):
        return Fraction(int(value), 1)
    if sp is not None and isinstance(value, sp.Rational):
        return Fraction(int(value.p), int(value.q))
    if isinstance(value, float):
        raise TypeError("binary floating point is forbidden in the exact engine")
    return Fraction(value)


def canon(labels: Iterable[int]) -> tuple[int, ...]:
    """Canonicalize a finite set partition by first occurrence."""
    mapping: dict[int, int] = {}
    result: list[int] = []
    for label in labels:
        if label not in mapping:
            mapping[label] = len(mapping)
        result.append(mapping[label])
    return tuple(result)


@dataclass(frozen=True)
class State:
    """Wilson color-partition state with two slots per matrix occurrence."""
    occ: tuple[tuple[int, bool], ...]
    part: tuple[int, ...]

    def __post_init__(self) -> None:
        if len(self.part) != 2 * len(self.occ):
            raise ValueError("State.part must have exactly two slots per occurrence")
        if self.part != canon(self.part):
            raise ValueError("State.part must be canonical")


EMPTY_STATE = State((), ())


def trace_state(steps: Sequence[tuple[int, int]]) -> State:
    """Create a traced Wilson word from oriented physical-link steps."""
    if not steps:
        return EMPTY_STATE
    occurrences: list[tuple[int, bool]] = []
    labels: list[int] = []
    length = len(steps)
    for position, (link, direction) in enumerate(steps):
        left, right = position, (position + 1) % length
        if int(direction) > 0:
            occurrences.append((int(link), True))
            labels.extend((left, right))
        else:
            occurrences.append((int(link), False))
            labels.extend((right, left))  # (Udag)_ab = Ubar_ba
    return State(tuple(occurrences), canon(labels))


def tensor_product(left: State, right: State) -> State:
    shift = max(left.part) + 1 if left.part else 0
    return State(
        left.occ + right.occ,
        canon(left.part + tuple(label + shift for label in right.part)),
    )


def classes(partition: Sequence[int]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = defaultdict(list)
    for slot, label in enumerate(partition):
        result[int(label)].append(slot)
    return dict(result)


def merge_classes(
    partition: Sequence[int], pairs: Iterable[tuple[int, int]]
) -> tuple[int, ...]:
    """Merge partition classes according to exact Kronecker deltas."""
    size = len(partition)
    parent = list(range(size))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    first: dict[int, int] = {}
    for slot, label in enumerate(partition):
        if label in first:
            union(slot, first[label])
        else:
            first[int(label)] = slot
    for left, right in pairs:
        union(int(left), int(right))
    return canon(find(slot) for slot in range(size))


def swap_rows(partition: Sequence[int], first: int, second: int) -> tuple[int, ...]:
    if partition[first] == partition[second]:
        return tuple(partition)
    result = list(partition)
    result[first], result[second] = result[second], result[first]
    return canon(result)


def opposite_reconnect(
    partition: Sequence[int], first_row: int, second_row: int
) -> tuple[int, ...]:
    """F x Fbar cross reconnection from the exact SU(3) Fierz identity."""
    size = len(partition)
    grouped = classes(partition)
    first_class, second_class = partition[first_row], partition[second_row]
    parent = list(range(size))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for members in grouped.values():
        remaining = [slot for slot in members if slot not in (first_row, second_row)]
        for slot in remaining[1:]:
            union(remaining[0], slot)
    first_remaining = [
        slot for slot in grouped[first_class] if slot not in (first_row, second_row)
    ]
    second_remaining = [
        slot for slot in grouped[second_class] if slot not in (first_row, second_row)
    ]
    if first_remaining and second_remaining:
        union(first_remaining[0], second_remaining[0])
    union(first_row, second_row)
    return canon(find(slot) for slot in range(size))


def remove_pair(
    state: State, first: int, second: int, merge_slots: tuple[int, int]
) -> tuple[Fraction, State]:
    """Remove an exposed U/Ubar pair and count free color loops."""
    partition = merge_classes(state.part, (merge_slots,))
    removed = {2 * first, 2 * first + 1, 2 * second, 2 * second + 1}
    kept_slots = [slot for slot in range(len(partition)) if slot not in removed]
    kept_classes = {partition[slot] for slot in kept_slots}
    lost_classes = len(set(partition) - kept_classes)
    scalar = Fraction(N ** max(0, lost_classes - 1), 1)
    occurrences = tuple(
        occurrence for index, occurrence in enumerate(state.occ)
        if index not in (first, second)
    )
    return scalar, State(occurrences, canon(partition[slot] for slot in kept_slots))


def simplify_unitarity(state: State) -> tuple[Fraction, State]:
    """Apply free U Udag cancellations until no exposed pair remains."""
    current, scalar, changed = state, Fraction(1), True
    while changed:
        changed = False
        grouped = classes(current.part)
        by_link: dict[int, list[tuple[int, bool]]] = defaultdict(list)
        for index, (link, is_u) in enumerate(current.occ):
            by_link[link].append((index, is_u))
        for items in by_link.values():
            finished_link = False
            for (first, first_type), (second, second_type) in itertools.combinations(items, 2):
                if first_type == second_type:
                    continue
                first_row, first_col = 2 * first, 2 * first + 1
                second_row, second_col = 2 * second, 2 * second + 1
                if set(grouped[current.part[first_row]]) == {first_row, second_row}:
                    factor, current = remove_pair(current, first, second, (first_col, second_col))
                elif set(grouped[current.part[first_col]]) == {first_col, second_col}:
                    factor, current = remove_pair(current, first, second, (first_row, second_row))
                else:
                    continue
                scalar *= factor
                changed = finished_link = True
                break
            if finished_link:
                break
    return scalar, current


def h0_action(state: State) -> dict[State, Fraction]:
    """Apply H0 = 1/2 sum E_l^2 using only the SU(3) Fierz identity."""
    initial_factor, reduced = simplify_unitarity(state)
    output: dict[State, Fraction] = defaultdict(Fraction)
    output[reduced] += initial_factor * Fraction(len(reduced.occ), 1) * CF / 2
    by_link: dict[int, list[tuple[int, bool]]] = defaultdict(list)
    for index, (link, is_u) in enumerate(reduced.occ):
        by_link[link].append((index, is_u))
    for items in by_link.values():
        for (first, first_type), (second, second_type) in itertools.combinations(items, 2):
            first_row, second_row = 2 * first, 2 * second
            if first_type == second_type:
                raw = State(reduced.occ, swap_rows(reduced.part, first_row, second_row))
                factor, simplified = simplify_unitarity(raw)
                output[simplified] += initial_factor * factor * Fraction(1, 2)
                output[reduced] -= initial_factor * Fraction(1, 2 * N)
            else:
                raw = State(reduced.occ, opposite_reconnect(reduced.part, first_row, second_row))
                factor, simplified = simplify_unitarity(raw)
                output[simplified] -= initial_factor * factor * Fraction(1, 2)
                output[reduced] += initial_factor * Fraction(1, 2 * N)
    return {item: coefficient for item, coefficient in output.items() if coefficient}


class HaarFamily(Enum):
    BALANCED_11 = (1, 1)
    BALANCED_22 = (2, 2)
    BALANCED_33 = (3, 3)
    DETERMINANT_30 = (3, 0)
    DETERMINANT_03 = (0, 3)
    MIXED_41 = (4, 1)
    MIXED_14 = (1, 4)
    PURE_SIX_60 = (6, 0)
    PURE_SIX_06 = (0, 6)


HAAR_FAMILY_BY_COUNTS = {family.value: family for family in HaarFamily}
FORBIDDEN_POISON_FAMILIES = frozenset({(2, 5), (5, 2)})
PURE_SIX_FAMILIES = frozenset({HaarFamily.PURE_SIX_60, HaarFamily.PURE_SIX_06})


@dataclass(frozen=True)
class HaarRouteRequest:
    n_u: int
    n_ubar: int
    operation: str
    source_layer: str
    target_layer: str
    source_state: str
    target_state: str
    link: str
    h0_key: str
    flux_key: str
    configuration: str

    def provenance(self) -> Mapping[str, str]:
        return MappingProxyType({
            "operation": self.operation,
            "source_layer": self.source_layer,
            "target_layer": self.target_layer,
            "source_state": self.source_state,
            "target_state": self.target_state,
            "link": self.link,
            "h0_key": self.h0_key,
            "flux_key": self.flux_key,
            "configuration": self.configuration,
        })


class ExactHaarRouter:
    """Fail-closed router for all local families admitted by this project."""

    def classify(self, n_u: int, n_ubar: int) -> HaarFamily | None:
        if type(n_u) is not int or type(n_ubar) is not int:
            raise TypeError("Haar occurrence counts must be exact Python integers")
        counts = (n_u, n_ubar)
        if counts[0] < 0 or counts[1] < 0:
            raise ValueError("Haar occurrence counts must be nonnegative")
        if counts in FORBIDDEN_POISON_FAMILIES:
            raise ForbiddenHaarFamily(
                f"local Haar family {counts} is explicitly forbidden poison"
            )
        family = HAAR_FAMILY_BY_COUNTS.get(counts)
        if family is not None:
            return family
        # Triality mismatch is an exact zero theorem, not an extra projector.
        if (counts[0] - counts[1]) % N:
            return None
        raise UnsupportedHaarFamily(
            f"zero-triality local Haar family {counts} is outside the nine-family allowlist"
        )

    def require_exact(self, n_u: int, n_ubar: int) -> HaarFamily | None:
        return self.classify(n_u, n_ubar)

    def route(
        self,
        request: HaarRouteRequest,
        contractor: Callable[[HaarFamily | None], Any],
    ) -> Any:
        """Validate schedule/family/provenance before touching a contractor."""
        allowed_layers = {"W1": ("P", "Q1"), "W2": ("Q1", "Q2")}
        expected = allowed_layers.get(request.operation)
        if expected is None or (request.source_layer, request.target_layer) != expected:
            raise IllegalScheduleTransition(
                f"invalid routed W transition {request.operation}: "
                f"{request.source_layer}->{request.target_layer}"
            )
        try:
            family = self.require_exact(request.n_u, request.n_ubar)
        except ForbiddenHaarFamily as error:
            raise ForbiddenHaarFamily(str(error), request.provenance()) from None
        return contractor(family)


DEFAULT_HAAR_ROUTER = ExactHaarRouter()


def permutation_inverse(permutation: Sequence[int]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def permutation_compose(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def permutation_cycles(permutation: Sequence[int]) -> int:
    seen = [False] * len(permutation)
    cycle_count = 0
    for start in range(len(permutation)):
        if seen[start]:
            continue
        cycle_count += 1
        current = start
        while not seen[current]:
            seen[current] = True
            current = permutation[current]
    return cycle_count


def permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


ExactMatrix = tuple[tuple[Fraction, ...], ...]


def fraction_matrix(rows: Sequence[Sequence[Any]]) -> ExactMatrix:
    """Freeze a rectangular exact matrix."""
    result = tuple(tuple(as_fraction(value) for value in row) for row in rows)
    if result and any(len(row) != len(result[0]) for row in result):
        raise ValueError("matrix rows must have equal length")
    return result


def fraction_identity(size: int) -> ExactMatrix:
    return tuple(tuple(Fraction(row == column) for column in range(size))
                 for row in range(size))


def fraction_matrix_multiply(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    if not left or not right:
        raise ValueError("matrix multiplication requires nonempty matrices")
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not align")
    return tuple(tuple(sum((
        left[row][inner] * right[inner][column]
        for inner in range(len(right))
    ), Fraction(0)) for column in range(len(right[0]))) for row in range(len(left)))


def fraction_rref(rows: Sequence[Sequence[Any]]) -> tuple[ExactMatrix, tuple[int, ...]]:
    """Exact reduced row echelon form and pivot columns."""
    matrix = [list(map(as_fraction, row)) for row in rows]
    if not matrix:
        return (), ()
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have equal length")
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(width):
        selected = next((row for row in range(pivot_row, len(matrix))
                         if matrix[row][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][index] - factor * matrix[pivot_row][index]
                for index in range(width)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return fraction_matrix(matrix), tuple(pivot_columns)


def fraction_matrix_rank(rows: Sequence[Sequence[Any]]) -> int:
    return len(fraction_rref(rows)[1])


def fraction_matrix_inverse(rows: Sequence[Sequence[Any]]) -> ExactMatrix:
    matrix = fraction_matrix(rows)
    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError("matrix inverse requires a nonempty square matrix")
    augmented = tuple(
        matrix[row] + fraction_identity(size)[row] for row in range(size)
    )
    reduced, pivots = fraction_rref(augmented)
    if pivots[:size] != tuple(range(size)):
        raise ExactEngineError("exact matrix is singular")
    return tuple(row[size:] for row in reduced)


@lru_cache(maxsize=None)
def balanced_weingarten(
    degree: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[Fraction, ...], ...]]:
    """Return the exact SU(3) balanced projector for degree 1, 2, or 3."""
    if degree not in (1, 2, 3):
        raise UnsupportedHaarFamily(f"balanced degree {degree} is not Phase-1 exact")
    permutations = tuple(itertools.permutations(range(degree)))
    gram = fraction_matrix([[
        N ** permutation_cycles(
            permutation_compose(permutation_inverse(left), right)
        )
        for right in permutations
    ] for left in permutations])
    return permutations, fraction_matrix_inverse(gram)


MIXED_41_GRAM: tuple[tuple[int, ...], ...] = (
    (18, 6, -6, 6),
    (6, 18, 6, -6),
    (-6, 6, 18, 6),
    (6, -6, 6, 18),
)

MIXED_41_PSEUDOINVERSE: tuple[tuple[Fraction, ...], ...] = (
    (Fraction(1, 32), Fraction(1, 96), Fraction(-1, 96), Fraction(1, 96)),
    (Fraction(1, 96), Fraction(1, 32), Fraction(1, 96), Fraction(-1, 96)),
    (Fraction(-1, 96), Fraction(1, 96), Fraction(1, 32), Fraction(1, 96)),
    (Fraction(1, 96), Fraction(-1, 96), Fraction(1, 96), Fraction(1, 32)),
)


# Exact pure-six local algebra.  The accepted invariant ordering is the ten
# epsilon(A) epsilon(A-complement) pairings used by the existing Q2 source.
PURE_SIX_SLOTS = tuple(range(6))


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3 or min(a, b, c) < 0 or max(a, b, c) >= 3:
        return 0
    return permutation_sign((a, b, c))


@lru_cache(maxsize=1)
def pure_six_partitions() -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    out = []
    for combination in itertools.combinations(range(1, 6), 2):
        first = (0,) + combination
        first_set = frozenset(first)
        second = tuple(index for index in PURE_SIX_SLOTS if index not in first_set)
        out.append((first, second))
    if len(out) != 10:
        raise AssertionError("pure-six invariant enumeration must have size ten")
    return tuple(out)


def pure_six_invariant(
    indices: Sequence[int],
    partition: tuple[Sequence[int], Sequence[int]],
) -> int:
    if len(indices) != 6:
        raise ValueError("pure-six invariant needs six indices")
    first, second = partition
    return epsilon3(*(indices[i] for i in first)) * epsilon3(
        *(indices[i] for i in second)
    )


@lru_cache(maxsize=1)
def pure_six_gram() -> tuple[tuple[int, ...], ...]:
    parts = pure_six_partitions()
    gram = [[0] * 10 for _ in range(10)]
    for indices in itertools.product(range(N), repeat=6):
        values = [pure_six_invariant(indices, part) for part in parts]
        for row, left in enumerate(values):
            if left:
                for column, right in enumerate(values):
                    gram[row][column] += left * right
    return tuple(tuple(row) for row in gram)


@lru_cache(maxsize=1)
def pure_six_gram_pseudoinverse() -> ExactMatrix:
    """Exact Moore-Penrose inverse; the tight-frame identity is G^2=72G."""
    return tuple(
        tuple(Fraction(value, 72 * 72) for value in row)
        for row in pure_six_gram()
    )


@lru_cache(maxsize=1)
def pure_six_coefficient_projector() -> ExactMatrix:
    return tuple(
        tuple(Fraction(value, 72) for value in row)
        for row in pure_six_gram()
    )


@dataclass(frozen=True)
class PureSixDeltaBranch:
    coefficient: Fraction
    permutation: tuple[int, ...]

    @property
    def occurrence_pairs(self) -> tuple[tuple[int, int], ...]:
        return tuple(enumerate(self.permutation))


@lru_cache(maxsize=1)
def pure_six_delta_branches() -> tuple[PureSixDeltaBranch, ...]:
    """Expand A G+ A^T into aggregated exact determinant-delta branches."""
    parts = pure_six_partitions()
    pinv = pure_six_gram_pseudoinverse()
    permutations = tuple(itertools.permutations(range(3)))
    aggregated: dict[tuple[int, ...], Fraction] = {}
    for row, (left_a, left_b) in enumerate(parts):
        for column, (right_a, right_b) in enumerate(parts):
            base = pinv[row][column]
            if not base:
                continue
            for sigma in permutations:
                for tau in permutations:
                    target = [-1] * 6
                    for index in range(3):
                        target[left_a[index]] = right_a[sigma[index]]
                        target[left_b[index]] = right_b[tau[index]]
                    key = tuple(target)
                    value = base * permutation_sign(sigma) * permutation_sign(tau)
                    aggregated[key] = aggregated.get(key, Fraction(0)) + value
    return tuple(
        PureSixDeltaBranch(value, permutation)
        for permutation, value in sorted(aggregated.items())
        if value
    )


def pure_six_dsu_terms(
    occurrences: Sequence[int],
) -> tuple[tuple[Fraction, tuple[tuple[int, int], ...]], ...]:
    """Map exact pure-six delta branches to interleaved State partition slots."""
    if len(occurrences) != 6 or len(set(occurrences)) != 6:
        raise ValueError("pure-six endpoint adapter needs six distinct occurrences")
    positions = tuple(map(int, occurrences))
    return tuple(
        (
            branch.coefficient,
            tuple(
                (2 * positions[row], 2 * positions[column] + 1)
                for row, column in branch.occurrence_pairs
            ),
        )
        for branch in pure_six_delta_branches()
    )


def pure_six_exact_gates() -> Mapping[str, Any]:
    gram = fraction_matrix(pure_six_gram())
    pinv = pure_six_gram_pseudoinverse()
    projector = pure_six_coefficient_projector()
    gram_squared = fraction_matrix_multiply(gram, gram)
    scaled_gram = tuple(tuple(72 * value for value in row) for row in gram)
    gram_pinv = fraction_matrix_multiply(gram, pinv)
    pinv_gram = fraction_matrix_multiply(pinv, gram)
    return MappingProxyType({
        "partition_count": len(pure_six_partitions()),
        "gram_rank": fraction_matrix_rank(gram),
        "tight_frame": gram_squared == scaled_gram,
        "mp_GGpG": fraction_matrix_multiply(gram_pinv, gram) == gram,
        "mp_pGpGp": fraction_matrix_multiply(pinv_gram, pinv) == pinv,
        "projector_symmetric": projector == tuple(zip(*projector)),
        "projector_idempotent": fraction_matrix_multiply(projector, projector) == projector,
        "projector_trace": sum(projector[i][i] for i in range(10)),
        "delta_branch_count": len(pure_six_delta_branches()),
        "dsu_term_count": len(pure_six_dsu_terms((7, 3, 11, 2, 5, 13))),
    })


def _accumulate_partition(
    output: dict[tuple[int, ...], Fraction],
    partition: Sequence[int],
    pairs: Iterable[tuple[int, int]],
    coefficient: Fraction,
) -> None:
    if coefficient:
        output[merge_classes(partition, pairs)] += coefficient


def contract_link_partition(
    partition: Sequence[int],
    u_occurrences: Sequence[int],
    ubar_occurrences: Sequence[int],
    router: ExactHaarRouter = DEFAULT_HAAR_ROUTER,
    provenance: Mapping[str, str] | None = None,
) -> dict[tuple[int, ...], Fraction]:
    """Contract one link through an exact audited Haar projector.

    The router is consulted before any contraction work.  Every admitted
    family, including both pure-six orientations, stays exact.
    """
    try:
        family = router.require_exact(len(u_occurrences), len(ubar_occurrences))
    except ForbiddenHaarFamily as error:
        raise ForbiddenHaarFamily(str(error), provenance) from None
    if family is None:
        return {}
    output: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)

    if family in {
        HaarFamily.BALANCED_11,
        HaarFamily.BALANCED_22,
        HaarFamily.BALANCED_33,
    }:
        degree = len(u_occurrences)
        permutations, inverse = balanced_weingarten(degree)
        for sigma_index, sigma in enumerate(permutations):
            for tau_index, tau in enumerate(permutations):
                pairs: list[tuple[int, int]] = []
                for position in range(degree):
                    pairs.append((
                        2 * u_occurrences[position],
                        2 * ubar_occurrences[sigma[position]],
                    ))
                    pairs.append((
                        2 * u_occurrences[position] + 1,
                        2 * ubar_occurrences[tau[position]] + 1,
                    ))
                _accumulate_partition(
                    output, partition, pairs, inverse[sigma_index][tau_index]
                )

    elif family in {HaarFamily.DETERMINANT_30, HaarFamily.DETERMINANT_03}:
        occurrences = (
            tuple(u_occurrences)
            if family is HaarFamily.DETERMINANT_30
            else tuple(ubar_occurrences)
        )
        for permutation in itertools.permutations(range(3)):
            pairs = [(
                2 * occurrences[position],
                2 * occurrences[permutation[position]] + 1,
            ) for position in range(3)]
            _accumulate_partition(
                output,
                partition,
                pairs,
                Fraction(permutation_sign(permutation), 6),
            )

    elif family in {HaarFamily.MIXED_41, HaarFamily.MIXED_14}:
        fundamentals = (
            tuple(u_occurrences)
            if family is HaarFamily.MIXED_41
            else tuple(ubar_occurrences)
        )
        antifundamental = (
            ubar_occurrences[0]
            if family is HaarFamily.MIXED_41
            else u_occurrences[0]
        )
        for row_choice in range(4):
            row_rest = [occurrence for index, occurrence in enumerate(fundamentals)
                        if index != row_choice]
            for column_choice in range(4):
                column_rest = [occurrence for index, occurrence in enumerate(fundamentals)
                               if index != column_choice]
                base = MIXED_41_PSEUDOINVERSE[row_choice][column_choice]
                for permutation in itertools.permutations(range(3)):
                    pairs = [
                        (2 * fundamentals[row_choice], 2 * antifundamental),
                        (2 * fundamentals[column_choice] + 1, 2 * antifundamental + 1),
                    ]
                    pairs.extend((
                        2 * row_rest[position],
                        2 * column_rest[permutation[position]] + 1,
                    ) for position in range(3))
                    _accumulate_partition(
                        output,
                        partition,
                        pairs,
                        base * permutation_sign(permutation),
                    )
    elif family in PURE_SIX_FAMILIES:
        occurrences = (
            tuple(u_occurrences)
            if family is HaarFamily.PURE_SIX_60
            else tuple(ubar_occurrences)
        )
        for coefficient, pairs in pure_six_dsu_terms(occurrences):
            _accumulate_partition(output, partition, pairs, coefficient)
    else:
        raise AssertionError(f"unhandled exact Haar family {family}")

    return {merged: coefficient for merged, coefficient in output.items() if coefficient}


def combine_bra_ket(
    left: State, right: State
) -> tuple[tuple[tuple[int, bool], ...], tuple[int, ...]]:
    bra_occurrences = tuple((link, not is_u) for link, is_u in left.occ)
    shift = max(left.part) + 1 if left.part else 0
    return (
        bra_occurrences + right.occ,
        canon(left.part + tuple(label + shift for label in right.part)),
    )


_HAAR_CACHE: dict[tuple[State, State], Fraction] = {}


def haar_inner(
    left: State,
    right: State,
    router: ExactHaarRouter = DEFAULT_HAAR_ROUTER,
) -> Fraction:
    """Exact Haar inner product of two color-partition states."""
    key = (left, right)
    if router is DEFAULT_HAAR_ROUTER and key in _HAAR_CACHE:
        return _HAAR_CACHE[key]
    occurrences, partition = combine_bra_ket(left, right)
    by_link: dict[int, dict[bool, list[int]]] = defaultdict(
        lambda: {True: [], False: []}
    )
    for index, (link, is_u) in enumerate(occurrences):
        by_link[link][is_u].append(index)
    partitions: dict[tuple[int, ...], Fraction] = {partition: Fraction(1)}
    for link in sorted(by_link):
        next_partitions: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
        for current, coefficient in partitions.items():
            contracted = contract_link_partition(
                current,
                by_link[link][True],
                by_link[link][False],
                router,
                MappingProxyType({
                    "operation": "exact-haar-inner",
                    "source_state": repr(left),
                    "target_state": repr(right),
                    "link": str(link),
                    "occurrence_family": str((
                        len(by_link[link][True]), len(by_link[link][False])
                    )),
                    "configuration": "marked-cluster-phase3",
                }),
            )
            for merged, local_coefficient in contracted.items():
                next_partitions[merged] += coefficient * local_coefficient
        partitions = {item: coefficient for item, coefficient in next_partitions.items()
                      if coefficient}
        if not partitions:
            break
    total = sum((
        coefficient * Fraction(N ** len(set(item)), 1)
        for item, coefficient in partitions.items()
    ), Fraction(0))
    if router is DEFAULT_HAAR_ROUTER:
        _HAAR_CACHE[key] = total
    return total


def closure(seed_state: State, max_states: int = 100) -> list[State]:
    """Generate the finite exact H0 closure of a seed state."""
    factor, seed = simplify_unitarity(seed_state)
    if factor != 1:
        raise ValueError("closure seed must be unit-normalized after free unitarity")
    states = [seed]
    seen = {seed}
    queue: deque[State] = deque((seed,))
    while queue:
        current = queue.popleft()
        for candidate in h0_action(current):
            if candidate in seen:
                continue
            seen.add(candidate)
            states.append(candidate)
            queue.append(candidate)
            if len(states) > max_states:
                raise ExactEngineError("unexpectedly large H0 closure")
    return states


def closure_matrices(
    seed_state: State,
    router: ExactHaarRouter = DEFAULT_HAAR_ROUTER,
) -> tuple[list[State], sp.Matrix, sp.Matrix, list[int], sp.Matrix, sp.Matrix]:
    """Build exact action, Gram quotient, and metric-Hermitian H0 matrices."""
    if sp is None:
        raise ExactEngineError(
            "SymPy is required only for Gram-quotient/resolvent construction; "
            "Google Colab includes it"
        )
    basis = closure(seed_state)
    index = {state: position for position, state in enumerate(basis)}
    dimension = len(basis)
    action = sp.zeros(dimension)
    for column, state in enumerate(basis):
        for result, coefficient in h0_action(state).items():
            action[index[result], column] += sp.Rational(
                coefficient.numerator, coefficient.denominator
            )
    gram = sp.zeros(dimension)
    for row in range(dimension):
        for column in range(row, dimension):
            value = haar_inner(basis[row], basis[column], router)
            exact = sp.Rational(value.numerator, value.denominator)
            gram[row, column] = gram[column, row] = exact
    pivots = list(gram.rref()[1])
    if not pivots:
        raise ExactEngineError("Haar Gram matrix has no physical quotient")
    physical_gram = gram.extract(pivots, pivots)
    metric_action = (gram * action).extract(pivots, pivots)
    physical_h0 = sp.simplify(physical_gram.inv() * metric_action)
    return basis, action, gram, pivots, physical_gram, physical_h0


def reduced_resolvent_on_state(
    seed_state: State,
    power: int = 1,
    reference_energy: Fraction = REFERENCE_E0,
    router: ExactHaarRouter = DEFAULT_HAAR_ROUTER,
) -> tuple[dict[State, Fraction], dict[str, Any]]:
    """Apply Q(E0-H0)^(-power)Q by exact rational linear algebra."""
    if int(power) < 1:
        raise ValueError("resolvent power must be a positive integer")
    basis, _action, gram, pivots, physical_gram, physical_h0 = closure_matrices(
        seed_state, router
    )
    energy = sp.Rational(reference_energy.numerator, reference_energy.denominator)
    metric_coordinates = sp.Matrix([gram[index, 0] for index in pivots])
    coordinates = sp.simplify(physical_gram.inv() * metric_coordinates)
    null_basis = (physical_h0 - energy * sp.eye(len(pivots))).nullspace()
    if null_basis:
        zero_modes = sp.Matrix.hstack(*null_basis)
        zero_projector = sp.simplify(
            zero_modes
            * (zero_modes.T * physical_gram * zero_modes).inv()
            * zero_modes.T
            * physical_gram
        )
    else:
        zero_projector = sp.zeros(len(pivots))
    complement = sp.eye(len(pivots)) - zero_projector
    denominator = energy * sp.eye(len(pivots)) - physical_h0
    resolvent = sp.simplify(
        complement * (denominator + zero_projector).inv() * complement
    )
    resolved = sp.simplify((resolvent ** int(power)) * coordinates)
    output: dict[State, Fraction] = defaultdict(Fraction)
    for row, pivot in enumerate(pivots):
        coefficient = sp.factor(resolved[row])
        if coefficient:
            output[basis[pivot]] += as_fraction(coefficient)
    metadata = {
        "closure_dim": len(basis),
        "gram_rank": len(pivots),
        "spectrum": physical_h0.eigenvals(),
        "E0_nullity": len(null_basis),
    }
    return dict(output), metadata


# -----------------------------------------------------------------------------
# Phase 2: concrete open-cubic geometry and exact face-insertion half histories
# -----------------------------------------------------------------------------

Coordinate = tuple[int, int, int]
FaceSupport = frozenset[int]
ExactStateVector = Mapping[State, Fraction]
LabelledStateVector = Mapping[FaceSupport, ExactStateVector]


@dataclass(frozen=True, order=True)
class LatticeLink:
    """An unoriented positive-axis link in an open cubic cell complex."""

    anchor: Coordinate
    axis: int

    def __post_init__(self) -> None:
        if len(self.anchor) != 3 or self.axis not in (0, 1, 2):
            raise ValueError("a cubic link needs a 3-vector anchor and axis 0,1,2")


@dataclass(frozen=True)
class PlaquetteFace:
    """Concrete plaquette with exact oriented integer-link boundary."""

    face_id: int
    anchor: Coordinate
    axes: tuple[int, int]
    steps: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        first, second = self.axes
        if not (0 <= first < second <= 2):
            raise ValueError("plaquette axes must satisfy 0 <= a < b <= 2")
        if len(self.steps) != 4 or {direction for _link, direction in self.steps} - {-1, 1}:
            raise ValueError("a plaquette requires four exactly oriented boundary links")

    @property
    def links(self) -> frozenset[int]:
        return frozenset(link for link, _direction in self.steps)


@dataclass(frozen=True)
class OpenCubicPatch:
    """Finite non-periodic face patch used only through explicit embeddings."""

    links: tuple[LatticeLink, ...]
    faces: tuple[PlaquetteFace, ...]
    adjacency: Mapping[int, frozenset[int]]

    def __post_init__(self) -> None:
        face_ids = {face.face_id for face in self.faces}
        if face_ids != set(range(len(self.faces))):
            raise ValueError("face ids must be consecutive from zero")
        normalized = {
            int(face): frozenset(map(int, neighbors))
            for face, neighbors in self.adjacency.items()
        }
        if set(normalized) != face_ids:
            raise ValueError("adjacency must contain every concrete face")
        for face, neighbors in normalized.items():
            if face in neighbors or any(face not in normalized[n] for n in neighbors):
                raise ValueError("face adjacency must be irreflexive and symmetric")
        object.__setattr__(self, "adjacency", MappingProxyType(normalized))

    def face(self, face_id: int) -> PlaquetteFace:
        return self.faces[int(face_id)]


def _coordinate_shift(anchor: Coordinate, axis: int) -> Coordinate:
    shifted = list(anchor)
    shifted[int(axis)] += 1
    return tuple(shifted)  # type: ignore[return-value]


def build_open_cubic_patch(
    face_specs: Iterable[tuple[Coordinate, int, int]],
) -> OpenCubicPatch:
    """Build a deterministic open patch; no periodic identification is allowed."""
    specs = tuple(sorted({
        (tuple(map(int, anchor)), int(first), int(second))
        for anchor, first, second in face_specs
    }))
    if not specs:
        raise ValueError("an open patch needs at least one plaquette")
    raw_boundaries: list[tuple[LatticeLink, ...]] = []
    for anchor, first, second in specs:
        if not (0 <= first < second <= 2):
            raise ValueError("face specification axes must satisfy a < b")
        along_first = _coordinate_shift(anchor, first)
        along_second = _coordinate_shift(anchor, second)
        raw_boundaries.append((
            LatticeLink(anchor, first),
            LatticeLink(along_first, second),
            LatticeLink(along_second, first),
            LatticeLink(anchor, second),
        ))
    links = tuple(sorted(set(itertools.chain.from_iterable(raw_boundaries))))
    link_id = {link: index for index, link in enumerate(links)}
    faces = tuple(
        PlaquetteFace(
            face_id,
            anchor,
            (first, second),
            (
                (link_id[boundary[0]], +1),
                (link_id[boundary[1]], +1),
                (link_id[boundary[2]], -1),
                (link_id[boundary[3]], -1),
            ),
        )
        for face_id, ((anchor, first, second), boundary) in enumerate(
            zip(specs, raw_boundaries)
        )
    )
    adjacency: dict[int, set[int]] = {face.face_id: set() for face in faces}
    incident_faces: dict[int, list[int]] = defaultdict(list)
    for face in faces:
        for link in face.links:
            incident_faces[link].append(face.face_id)
    for incident in incident_faces.values():
        for left, right in itertools.combinations(sorted(incident), 2):
            adjacency[left].add(right)
            adjacency[right].add(left)
    return OpenCubicPatch(
        links,
        faces,
        MappingProxyType({face: frozenset(neighbors) for face, neighbors in adjacency.items()}),
    )


@dataclass(frozen=True)
class RootedOpenCluster:
    patch: OpenCubicPatch
    root: int
    support: FaceSupport

    def __post_init__(self) -> None:
        support = frozenset(map(int, self.support))
        if self.root not in support:
            raise ValueError("a rooted cluster must contain its root face")
        if not support.issubset(range(len(self.patch.faces))):
            raise ValueError("cluster contains a face outside its open patch")
        if not connected_in_adjacency(support, self.patch.adjacency):
            raise ValueError("cluster must be link-connected")
        object.__setattr__(self, "support", support)

    @property
    def exposed_links(self) -> frozenset[int]:
        counts: dict[int, int] = defaultdict(int)
        for face_id in self.support:
            for link in self.patch.face(face_id).links:
                counts[link] += 1
        return frozenset(link for link, count in counts.items() if count == 1)


def enumerate_rooted_open_clusters(
    patch: OpenCubicPatch,
    root: int,
    max_faces: int,
) -> tuple[RootedOpenCluster, ...]:
    """Enumerate literal concrete rooted link-connected subsets of a patch."""
    root = int(root)
    if root not in range(len(patch.faces)):
        raise ValueError("root is outside the patch")
    if int(max_faces) < 1:
        raise ValueError("max_faces must be positive")
    cap = min(int(max_faces), len(patch.faces))
    seen: set[FaceSupport] = {frozenset({root})}
    frontier: set[FaceSupport] = {frozenset({root})}
    for _size in range(1, cap):
        next_frontier: set[FaceSupport] = set()
        for support in frontier:
            boundary = set().union(*(patch.adjacency[face] for face in support)) - set(support)
            for face in boundary:
                expanded = frozenset((*support, int(face)))
                if expanded not in seen:
                    seen.add(expanded)
                    next_frontier.add(expanded)
        frontier = next_frontier
        if not frontier:
            break
    ordered = tuple(sorted(seen, key=lambda item: (len(item), tuple(sorted(item)))))
    return tuple(RootedOpenCluster(patch, root, support) for support in ordered)


def iter_rooted_connected_supports(
    patch: OpenCubicPatch,
    root: int,
    max_faces: int,
) -> Iterable[FaceSupport]:
    """Enumerate each concrete rooted connected support once with bounded memory.

    This is the finite-graph Redelmeier recursion.  At each recursion level a
    candidate is permanently excluded from later sibling branches after its
    branch is exhausted.  Every connected support has a unique first-added
    candidate at that branch, so no global ``seen`` set is needed.
    """
    root, max_faces = int(root), int(max_faces)
    if root not in range(len(patch.faces)):
        raise ValueError("root is outside the patch")
    if max_faces < 1:
        raise ValueError("max_faces must be positive")

    def visit(
        support: FaceSupport,
        candidates: tuple[int, ...],
        forbidden: frozenset[int],
    ) -> Iterable[FaceSupport]:
        yield support
        if len(support) >= max_faces:
            return
        remaining = list(candidates)
        locally_forbidden = set(forbidden)
        while remaining:
            face = remaining.pop(0)
            expanded = frozenset((*support, face))
            next_candidates = set(remaining)
            next_candidates.update(
                neighbor
                for neighbor in patch.adjacency[face]
                if neighbor not in expanded and neighbor not in locally_forbidden
            )
            yield from visit(
                expanded,
                tuple(sorted(next_candidates)),
                frozenset(locally_forbidden),
            )
            locally_forbidden.add(face)

    yield from visit(
        frozenset({root}),
        tuple(sorted(patch.adjacency[root])),
        frozenset(),
    )


def require_complete_rooted_ball(
    patch: OpenCubicPatch,
    root: int,
    max_faces: int,
) -> Mapping[int, int]:
    """Prove that every graph neighbor needed through ``max_faces`` exists."""
    root, max_faces = int(root), int(max_faces)
    distance = {root: 0}
    queue = deque((root,))
    while queue:
        face = queue.popleft()
        if distance[face] >= max_faces - 1:
            continue
        for neighbor in patch.adjacency[face]:
            if neighbor not in distance:
                distance[neighbor] = distance[face] + 1
                queue.append(neighbor)
    incomplete = {
        face: len(patch.adjacency[face])
        for face, depth in distance.items()
        if depth < max_faces - 1 and len(patch.adjacency[face]) != 12
    }
    if incomplete:
        raise ProductionNotReady(
            f"open patch does not contain the complete rooted cubic ball: {incomplete}"
        )
    return MappingProxyType(distance)


def streaming_rooted_support_census(
    patch: OpenCubicPatch,
    root: int,
    max_faces: int,
    *,
    progress_every: int = 0,
) -> Mapping[str, Any]:
    """Count and hash a Redelmeier support stream without retaining it."""
    if type(progress_every) is not int or progress_every < 0:
        raise ValueError("progress_every must be a nonnegative exact integer")
    require_complete_rooted_ball(patch, root, max_faces)
    digest = hashlib.sha256()
    histogram = [0] * (int(max_faces) + 1)
    count = 0
    started = time.monotonic()
    for support in iter_rooted_connected_supports(patch, root, max_faces):
        ordered = tuple(sorted(support))
        size = len(ordered)
        histogram[size] += 1
        count += 1
        digest.update(size.to_bytes(1, "big"))
        for face in ordered:
            digest.update(int(face).to_bytes(8, "big", signed=False))
        if progress_every and count % progress_every == 0:
            print(
                f"[GEOMETRY] root={root} supports={count:,} "
                f"elapsed={time.monotonic() - started:.1f}s",
                file=sys.stderr,
                flush=True,
            )
    return MappingProxyType({
        "algorithm": ROOTED_SUPPORT_STREAM_ALGORITHM,
        "root_face": int(root),
        "max_faces": int(max_faces),
        "cluster_count": count,
        "size_histogram": MappingProxyType({
            size: histogram[size]
            for size in range(1, int(max_faces) + 1)
            if histogram[size]
        }),
        "support_stream_sha256": digest.hexdigest(),
    })


def build_full_t1_rooted_ball(
    max_faces: int = FOURTH_ORDER_MAX_MARKED_FACES,
) -> tuple[OpenCubicPatch, Mapping[int, int]]:
    """Build the exact open union of graph balls around the three origin roots.

    Nodes out to graph distance ``max_faces-1`` are retained.  Consequently
    every proper interior node has all twelve infinite-cubic link-sharing
    neighbors, which is the mechanical condition used by the literal rooted
    embedding certificate.  No periodic identification is introduced.
    """
    max_faces = int(max_faces)
    if max_faces < 1:
        raise ValueError("max_faces must be positive")
    graph_radius = max_faces - 1
    coordinate_radius = graph_radius + 1
    box_specs = tuple(
        ((x, y, z), first, second)
        for x in range(-coordinate_radius, coordinate_radius + 1)
        for y in range(-coordinate_radius, coordinate_radius + 1)
        for z in range(-coordinate_radius, coordinate_radius + 1)
        for first, second in T1_POLARIZATION_PLANES
    )
    box = build_open_cubic_patch(box_specs)
    box_by_spec = {
        (face.anchor, face.axes): face.face_id for face in box.faces
    }
    roots = {
        pol: box_by_spec[((0, 0, 0), axes)]
        for pol, axes in enumerate(T1_POLARIZATION_PLANES)
    }
    retained: set[int] = set()
    for root in roots.values():
        distance = {root: 0}
        queue = deque((root,))
        while queue:
            face = queue.popleft()
            retained.add(face)
            if distance[face] >= graph_radius:
                continue
            for neighbor in box.adjacency[face]:
                if neighbor not in distance:
                    distance[neighbor] = distance[face] + 1
                    queue.append(neighbor)
    retained_specs = tuple(
        (box.face(face).anchor, *box.face(face).axes) for face in sorted(retained)
    )
    patch = build_open_cubic_patch(retained_specs)
    patch_by_spec = {
        (face.anchor, face.axes): face.face_id for face in patch.faces
    }
    roots_by_pol = MappingProxyType({
        pol: patch_by_spec[((0, 0, 0), axes)]
        for pol, axes in enumerate(T1_POLARIZATION_PLANES)
    })
    return patch, roots_by_pol


def phase3_geometry_preflight(
    max_faces: int = O4_TRIALITY_CANDIDATE_MAX_FACES,
) -> Mapping[str, Any]:
    """Validate the sealed 609-row candidate sweep with zero physics."""
    if not __debug__:
        raise ProductionNotReady("optimized Python (-O) is forbidden for certificate gates")
    started = time.monotonic()
    tracing_was_active = tracemalloc.is_tracing()
    if not tracing_was_active:
        tracemalloc.start()
    if type(max_faces) is not int or max_faces != O4_TRIALITY_CANDIDATE_MAX_FACES:
        raise ValueError("candidate preflight maximum is the sealed exact integer six")
    patch, roots, coverages, candidate = (
        build_o4_triality_candidate_full_t1_coverage()
    )
    stable = {
        "schema": "HODGE-SU3-PHASE3-TRIALITY-CANDIDATE-PREFLIGHT-v3",
        "algorithm": "SEALED-STAGE0-TRIALITY-CANDIDATE-CLOSURE-v1",
        "necessary_not_sufficient": True,
        "candidate_observed_max_faces": max_faces,
        "endpoint_folded_label_firewall": FOURTH_ORDER_MAX_MARKED_FACES,
        "patch_face_count": len(patch.faces),
        "roots": {
            str(pol): {
                "root_face": root,
                "root_axes": list(patch.face(root).axes),
                "cluster_count": len(coverages[pol].embeddings),
                "support_sha256": candidate["per_polarization_support_sha256"][str(pol)],
            }
            for pol, root in roots.items()
        },
        "total_exact_cluster_evaluations": 609,
        "physics_contractions_run": 0,
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "candidate_coverage_certificate_sha256": candidate["certificate_sha256"],
        "source_authority_sha256": {
            key: value["sha256"] for key, value in SOURCE_AUTHORITIES.items()
        },
    }
    preflight_sha = hashlib.sha256(
        json.dumps(stable, sort_keys=True, separators=(",", ":"), allow_nan=False).encode(
            "utf-8"
        )
    ).hexdigest()
    _current_traced, peak_traced = tracemalloc.get_traced_memory()
    if not tracing_was_active:
        tracemalloc.stop()
    return MappingProxyType({
        **stable,
        "preflight_sha256": preflight_sha,
        "elapsed_seconds": f"{time.monotonic() - started:.3f}",
        "python_tracemalloc_peak_bytes": peak_traced,
    })


def normalize_state_vector(vector: Mapping[State, Any]) -> dict[State, Fraction]:
    output: dict[State, Fraction] = defaultdict(Fraction)
    for state, coefficient in vector.items():
        output[state] += as_fraction(coefficient)
    return {state: coefficient for state, coefficient in output.items() if coefficient}


def multiply_state_vector_by_trace(
    vector: Mapping[State, Any],
    traced_face: State,
) -> dict[State, Fraction]:
    """Exact v10a6 ``multiply_vec``: tensor, simplify, retain every Fraction."""
    output: dict[State, Fraction] = defaultdict(Fraction)
    for state, coefficient in normalize_state_vector(vector).items():
        factor, product = simplify_unitarity(tensor_product(state, traced_face))
        output[product] += coefficient * factor
    return {state: coefficient for state, coefficient in output.items() if coefficient}


def exact_vector_inner(
    left: Mapping[State, Any],
    right: Mapping[State, Any],
) -> Fraction:
    left_exact, right_exact = normalize_state_vector(left), normalize_state_vector(right)
    return sum((
        left_coefficient * right_coefficient * haar_inner(left_state, right_state)
        for left_state, left_coefficient in left_exact.items()
        for right_state, right_coefficient in right_exact.items()
    ), Fraction(0))


@lru_cache(maxsize=None)
def _resolved_seed_cached(
    state: State,
    power: int,
    reference_energy: Fraction,
) -> tuple[tuple[State, Fraction], ...]:
    resolved, _metadata = reduced_resolvent_on_state(
        state,
        power=int(power),
        reference_energy=reference_energy,
    )
    return tuple(sorted(resolved.items(), key=lambda item: repr(item[0])))


def exact_resolvent_vector(
    vector: Mapping[State, Any],
    *,
    power: int = 1,
    reference_energy: Fraction = REFERENCE_E0,
) -> dict[State, Fraction]:
    output: dict[State, Fraction] = defaultdict(Fraction)
    reference_energy = as_fraction(reference_energy)
    for state, coefficient in normalize_state_vector(vector).items():
        for resolved_state, resolved_coefficient in _resolved_seed_cached(
            state, int(power), reference_energy
        ):
            output[resolved_state] += coefficient * resolved_coefficient
    return {state: coefficient for state, coefficient in output.items() if coefficient}


class PerturbativeSector(Enum):
    P = "P"
    Q1 = "Q1"
    Q2 = "Q2"


class ExactFaceInsertionBuilder:
    """Build W=-M from exact plaquette traces; W has no Q2 entry point."""

    def __init__(self, patch: OpenCubicPatch) -> None:
        self.patch = patch
        self._traces = {
            (face.face_id, sign): trace_state(
                face.steps if sign > 0 else tuple(
                    (link, -direction) for link, direction in reversed(face.steps)
                )
            )
            for face in patch.faces
            for sign in (-1, +1)
        }

    def source_axial(self, root: int) -> dict[State, Fraction]:
        """Unnormalised |p>-|pbar>; all bilinears later carry exact factor 1/2."""
        return normalize_state_vector({
            self._traces[(int(root), +1)]: Fraction(+1),
            self._traces[(int(root), -1)]: Fraction(-1),
        })

    def insert_face(
        self,
        vector: Mapping[State, Any],
        face_id: int,
        sign: int,
    ) -> dict[State, Fraction]:
        if int(face_id) not in range(len(self.patch.faces)) or int(sign) not in (-1, +1):
            raise ValueError("face insertion requires an in-patch face and sign +/-1")
        return multiply_state_vector_by_trace(vector, self._traces[(int(face_id), int(sign))])

    def apply_w(
        self,
        vector: Mapping[State, Any],
        allowed_faces: Iterable[int],
        *,
        source_sector: PerturbativeSector,
    ) -> dict[State, Fraction]:
        if source_sector is PerturbativeSector.Q2:
            raise WOnQ2Forbidden("W(Q2) is impossible in the exact face builder")
        if source_sector not in (PerturbativeSector.P, PerturbativeSector.Q1):
            raise IllegalScheduleTransition("W accepts only P or Q1")
        output: dict[State, Fraction] = defaultdict(Fraction)
        for face_id in sorted(set(map(int, allowed_faces))):
            for sign in (-1, +1):
                # Canonical project convention H=H0-uM, hence W=-M.
                for state, coefficient in self.insert_face(vector, face_id, sign).items():
                    output[state] -= coefficient
        return {state: coefficient for state, coefficient in output.items() if coefficient}


def normalize_labelled_vector(
    vector: Mapping[FaceSupport, Mapping[State, Any]],
) -> dict[FaceSupport, dict[State, Fraction]]:
    return {
        frozenset(map(int, support)): exact
        for support, states in vector.items()
        if (exact := normalize_state_vector(states))
    }


def apply_w_labelled(
    builder: ExactFaceInsertionBuilder,
    vector: LabelledStateVector,
    allowed_faces: Iterable[int],
    *,
    source_sector: PerturbativeSector,
) -> dict[FaceSupport, dict[State, Fraction]]:
    if source_sector is PerturbativeSector.Q2:
        raise WOnQ2Forbidden("W(Q2) is impossible before any face contraction")
    output: dict[FaceSupport, dict[State, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    for support, states in normalize_labelled_vector(vector).items():
        for face_id in sorted(set(map(int, allowed_faces))):
            target_support = frozenset(set(support) | {face_id})
            for sign in (-1, +1):
                for state, coefficient in builder.insert_face(states, face_id, sign).items():
                    output[target_support][state] -= coefficient
    return {
        support: normalize_state_vector(states)
        for support, states in output.items()
        if normalize_state_vector(states)
    }


def apply_resolvent_labelled(
    vector: LabelledStateVector,
    *,
    power: int = 1,
    reference_energy: Fraction = REFERENCE_E0,
) -> dict[FaceSupport, dict[State, Fraction]]:
    return {
        support: resolved
        for support, states in normalize_labelled_vector(vector).items()
        if (resolved := exact_resolvent_vector(
            states, power=int(power), reference_energy=reference_energy
        ))
    }


def labelled_inner(
    left: LabelledStateVector,
    right: LabelledStateVector,
    *,
    normalization: Fraction = Fraction(1),
) -> Mapping[FaceSupport, Fraction]:
    output: dict[FaceSupport, Fraction] = defaultdict(Fraction)
    normalization = as_fraction(normalization)
    for left_support, left_states in normalize_labelled_vector(left).items():
        for right_support, right_states in normalize_labelled_vector(right).items():
            support = frozenset(set(left_support) | set(right_support))
            output[support] += normalization * exact_vector_inner(left_states, right_states)
    return MappingProxyType({support: value for support, value in output.items() if value})


@dataclass(frozen=True)
class ExactGlobalBlockElements:
    """Real exact Krylov block elements plus algebraic adjoints.

    ``PQ1`` means P -> Q1 and ``Q1Q2`` means Q1 -> Q2.  Their adjoints are
    copied only after exact real-Hermitian equality is established; W is never
    evaluated on Q2.
    """

    PP: Fraction
    PQ1: Fraction
    Q1P: Fraction
    Q1Q1: Fraction
    Q1Q2: Fraction
    Q2Q1: Fraction

    def __post_init__(self) -> None:
        for name in ("PP", "PQ1", "Q1P", "Q1Q1", "Q1Q2", "Q2Q1"):
            object.__setattr__(self, name, as_fraction(getattr(self, name)))
        if self.PQ1 != self.Q1P or self.Q1Q2 != self.Q2Q1:
            raise ValueError("exact real block adjoints must agree")


@dataclass(frozen=True)
class ExactHalfHistory:
    P_state: LabelledStateVector
    W1_state: LabelledStateVector
    R1_state: LabelledStateVector
    W2_state: LabelledStateVector
    R2_state: LabelledStateVector
    RR1_state: LabelledStateVector
    RRR1_state: LabelledStateVector
    schedule_trace: tuple[str, ...]
    blocks: ExactGlobalBlockElements


def _sum_ledger(ledger: Mapping[FaceSupport, Fraction]) -> Fraction:
    return sum((as_fraction(value) for value in ledger.values()), Fraction(0))


def build_exact_half_history(
    builder: ExactFaceInsertionBuilder,
    source: LabelledStateVector,
    allowed_faces: Iterable[int],
    *,
    reference_energy: Fraction,
    normalization: Fraction,
    resolvent_callback: Callable[
        [LabelledStateVector, Fraction], dict[FaceSupport, dict[State, Fraction]]
    ] | None = None,
) -> ExactHalfHistory:
    """Construct the only legal P->W1->R1->W2->R2 half history exactly."""
    allowed = frozenset(map(int, allowed_faces))
    source_exact = normalize_labelled_vector(source)
    if resolvent_callback is None:
        resolvent_callback = lambda value, energy: apply_resolvent_labelled(
            value, reference_energy=energy
        )
    schedule: CanonicalFourthOrderSchedule[LabelledStateVector] = (
        CanonicalFourthOrderSchedule(
            lambda value: apply_w_labelled(
                builder, value, allowed, source_sector=PerturbativeSector.P
            ),
            lambda value: resolvent_callback(value, as_fraction(reference_energy)),
            lambda value: apply_w_labelled(
                builder, value, allowed, source_sector=PerturbativeSector.Q1
            ),
            lambda value: resolvent_callback(value, as_fraction(reference_energy)),
        )
    )
    w1 = schedule.first_w(P(source_exact))
    r1 = schedule.first_resolvent(w1)
    w2 = schedule.second_w(r1)
    r2 = schedule.second_resolvent(w2)
    rr1 = resolvent_callback(r1.payload, as_fraction(reference_energy))
    rrr1 = resolvent_callback(rr1, as_fraction(reference_energy))
    norm = as_fraction(normalization)
    pp = _sum_ledger(labelled_inner(source_exact, w1.payload, normalization=norm))
    pq1 = _sum_ledger(labelled_inner(r1.payload, w1.payload, normalization=norm))
    q1q1 = _sum_ledger(labelled_inner(r1.payload, w2.payload, normalization=norm))
    q1q2 = _sum_ledger(labelled_inner(r2.payload, w2.payload, normalization=norm))
    blocks = ExactGlobalBlockElements(pp, pq1, pq1, q1q1, q1q2, q1q2)
    return ExactHalfHistory(
        source_exact, w1.payload, r1.payload, w2.payload, r2.payload,
        rr1, rrr1, schedule.trace, blocks,
    )


# Literal concrete rooted incidence recursion from the v10a.21 construction.
Support = frozenset[int]


def connected_in_adjacency(
    cluster: Iterable[int],
    adjacency: Mapping[int, Iterable[int]],
) -> bool:
    concrete = frozenset(map(int, cluster))
    if not concrete:
        return False
    reached = {next(iter(concrete))}
    queue = deque(reached)
    while queue:
        face = queue.popleft()
        for neighbor in adjacency.get(face, ()):
            neighbor = int(neighbor)
            if neighbor in concrete and neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    return reached == set(concrete)


def rooted_connected_subsets_of(
    cluster: Iterable[int],
    root: int,
    connected: Callable[[Support], bool],
) -> tuple[Support, ...]:
    concrete = frozenset(map(int, cluster))
    root = int(root)
    if root not in concrete:
        return ()
    rest = tuple(sorted(set(concrete) - {root}))
    subsets: list[Support] = []
    for mask in range(1 << len(rest)):
        subset = {root}
        for index, face in enumerate(rest):
            if (mask >> index) & 1:
                subset.add(face)
        frozen = frozenset(subset)
        if connected(frozen):
            subsets.append(frozen)
    return tuple(subsets)


def rooted_union_convolution(
    left: Mapping[Support, Fraction],
    right: Mapping[Support, Fraction],
) -> Mapping[Support, Fraction]:
    output: dict[Support, Fraction] = defaultdict(Fraction)
    for left_support, left_weight in left.items():
        for right_support, right_weight in right.items():
            output[frozenset(set(left_support) | set(right_support))] += (
                as_fraction(left_weight) * as_fraction(right_weight)
            )
    return MappingProxyType({support: weight for support, weight in output.items() if weight})


def exact_ledger(
    ledger: Mapping[Support, Any],
) -> Mapping[Support, Fraction]:
    output: dict[Support, Fraction] = defaultdict(Fraction)
    for support, value in ledger.items():
        output[frozenset(map(int, support))] += as_fraction(value)
    return MappingProxyType({support: value for support, value in output.items() if value})


def ledger_linear_combination(
    *terms: tuple[Any, Mapping[Support, Any]],
) -> Mapping[Support, Fraction]:
    output: dict[Support, Fraction] = defaultdict(Fraction)
    for scalar, ledger in terms:
        scalar_exact = as_fraction(scalar)
        for support, value in exact_ledger(ledger).items():
            output[support] += scalar_exact * value
    return MappingProxyType({support: value for support, value in output.items() if value})


@dataclass(frozen=True)
class ExactLowerOrderLedgers:
    """Independent n=1,2,3 Rayleigh-Schrödinger support ledgers."""

    A: Mapping[Support, Fraction]
    E2: Mapping[Support, Fraction]
    Sigma3: Mapping[Support, Fraction]
    N: Mapping[Support, Fraction]
    AN: Mapping[Support, Fraction]
    E3: Mapping[Support, Fraction]

    def __post_init__(self) -> None:
        for name in ("A", "E2", "Sigma3", "N", "AN", "E3"):
            object.__setattr__(self, name, exact_ledger(getattr(self, name)))
        expected_an = rooted_union_convolution(self.A, self.N)
        expected_e3 = ledger_linear_combination((1, self.Sigma3), (-1, expected_an))
        if dict(self.AN) != dict(expected_an) or dict(self.E3) != dict(expected_e3):
            raise ValueError("lower-order ledgers fail exact E3=Sigma3-A union N")


@dataclass(frozen=True)
class ExactFourthOrderLedgers:
    """Support-labelled D,N,J,C and every union-convolved folded term."""

    A: Mapping[Support, Fraction]
    E2: Mapping[Support, Fraction]
    N: Mapping[Support, Fraction]
    C: Mapping[Support, Fraction]
    J: Mapping[Support, Fraction]
    D: Mapping[Support, Fraction]
    E2N: Mapping[Support, Fraction]
    AC: Mapping[Support, Fraction]
    AAJ: Mapping[Support, Fraction]
    E4: Mapping[Support, Fraction]

    def __post_init__(self) -> None:
        for name in ("A", "E2", "N", "C", "J", "D", "E2N", "AC", "AAJ", "E4"):
            object.__setattr__(self, name, exact_ledger(getattr(self, name)))
        e2n = rooted_union_convolution(self.E2, self.N)
        ac = rooted_union_convolution(self.A, self.C)
        aaj = rooted_union_convolution(
            rooted_union_convolution(self.A, self.A), self.J
        )
        e4 = ledger_linear_combination(
            (1, self.D), (-1, e2n), (-2, ac), (1, aaj)
        )
        if (
            dict(self.E2N) != dict(e2n)
            or dict(self.AC) != dict(ac)
            or dict(self.AAJ) != dict(aaj)
            or dict(self.E4) != dict(e4)
        ):
            raise ValueError("fourth-order ledgers fail exact union-convolved fold")


@dataclass(frozen=True)
class ExactClusterEvaluation:
    cluster: RootedOpenCluster
    marked_history: ExactHalfHistory
    vacuum_history: ExactHalfHistory
    marked_lower: ExactLowerOrderLedgers
    vacuum_lower: ExactLowerOrderLedgers
    marked_fourth: ExactFourthOrderLedgers
    vacuum_fourth: ExactFourthOrderLedgers
    gap_fourth: Mapping[Support, Fraction]

    def __post_init__(self) -> None:
        object.__setattr__(self, "gap_fourth", exact_ledger(self.gap_fourth))
        expected = ledger_linear_combination(
            (1, self.marked_fourth.E4), (-1, self.vacuum_fourth.E4)
        )
        if dict(self.gap_fourth) != dict(expected):
            raise ValueError("cluster gap is not marked minus vacuum support-by-support")


def lower_order_ledgers_from_history(
    history: ExactHalfHistory,
    *,
    normalization: Fraction,
) -> ExactLowerOrderLedgers:
    norm = as_fraction(normalization)
    a = labelled_inner(history.P_state, history.W1_state, normalization=norm)
    e2 = labelled_inner(history.W1_state, history.R1_state, normalization=norm)
    sigma3 = labelled_inner(history.R1_state, history.W2_state, normalization=norm)
    n_ledger = labelled_inner(history.R1_state, history.R1_state, normalization=norm)
    an = rooted_union_convolution(a, n_ledger)
    e3 = ledger_linear_combination((1, sigma3), (-1, an))
    return ExactLowerOrderLedgers(a, e2, sigma3, n_ledger, an, e3)


def fourth_order_ledgers_from_history(
    history: ExactHalfHistory,
    *,
    normalization: Fraction,
) -> ExactFourthOrderLedgers:
    norm = as_fraction(normalization)
    a = labelled_inner(history.P_state, history.W1_state, normalization=norm)
    e2 = labelled_inner(history.W1_state, history.R1_state, normalization=norm)
    n_ledger = labelled_inner(history.R1_state, history.R1_state, normalization=norm)
    c_ledger = labelled_inner(history.RR1_state, history.W2_state, normalization=norm)
    j_ledger = labelled_inner(history.W1_state, history.RRR1_state, normalization=norm)
    d_ledger = labelled_inner(history.W2_state, history.R2_state, normalization=norm)
    e2n = rooted_union_convolution(e2, n_ledger)
    ac = rooted_union_convolution(a, c_ledger)
    aaj = rooted_union_convolution(rooted_union_convolution(a, a), j_ledger)
    e4 = ledger_linear_combination(
        (1, d_ledger), (-1, e2n), (-2, ac), (1, aaj)
    )
    return ExactFourthOrderLedgers(
        a, e2, n_ledger, c_ledger, j_ledger, d_ledger, e2n, ac, aaj, e4
    )


def evaluate_exact_marked_vacuum_cluster(
    builder: ExactFaceInsertionBuilder,
    cluster: RootedOpenCluster,
) -> ExactClusterEvaluation:
    """Evaluate one concrete cluster from exact face insertions and resolvents.

    This is intentionally local.  It does not infer embedding multiplicities and
    cannot seal a global coefficient by itself.
    """
    if builder.patch is not cluster.patch:
        raise ValueError("cluster and face builder must share the same concrete patch")
    marked_source = {
        frozenset({cluster.root}): builder.source_axial(cluster.root)
    }
    marked_history = build_exact_half_history(
        builder,
        marked_source,
        cluster.support,
        reference_energy=REFERENCE_E0,
        normalization=Fraction(1, 2),
    )
    vacuum_source = {frozenset(): {EMPTY_STATE: Fraction(1)}}
    vacuum_history = build_exact_half_history(
        builder,
        vacuum_source,
        cluster.support,
        reference_energy=Fraction(0),
        normalization=Fraction(1),
    )
    marked_lower = lower_order_ledgers_from_history(
        marked_history, normalization=Fraction(1, 2)
    )
    vacuum_lower = lower_order_ledgers_from_history(
        vacuum_history, normalization=Fraction(1)
    )
    marked_fourth = fourth_order_ledgers_from_history(
        marked_history, normalization=Fraction(1, 2)
    )
    vacuum_fourth = fourth_order_ledgers_from_history(
        vacuum_history, normalization=Fraction(1)
    )
    # The vacuum has a=0 exactly; failing this is a physical construction error.
    if vacuum_lower.A:
        raise ExactEngineError("vacuum first-order ledger must vanish exactly")
    gap = ledger_linear_combination(
        (1, marked_fourth.E4), (-1, vacuum_fourth.E4)
    )
    return ExactClusterEvaluation(
        cluster, marked_history, vacuum_history, marked_lower, vacuum_lower,
        marked_fourth, vacuum_fourth, gap,
    )


@dataclass(frozen=True)
class RootedIncidenceResult:
    clusters: tuple[Support, ...]
    raw: Mapping[Support, Fraction]
    omega: Mapping[Support, Fraction]


def rooted_incidence_transform(
    minimal_ledger: Mapping[Support, Fraction],
    root: int,
    connected: Callable[[Support], bool],
) -> RootedIncidenceResult:
    """Downward-close concrete supports and apply literal recursive subtraction."""
    minimal = {
        frozenset(map(int, support)): as_fraction(weight)
        for support, weight in minimal_ledger.items()
        if as_fraction(weight)
    }
    if any(root not in support or not connected(support) for support in minimal):
        raise ValueError("every nonzero minimal support must be rooted and connected")
    cluster_set: set[Support] = set()
    for cluster in minimal:
        cluster_set.update(rooted_connected_subsets_of(cluster, root, connected))
    clusters = tuple(sorted(cluster_set, key=lambda support: (len(support), tuple(sorted(support)))))
    raw: dict[Support, Fraction] = {}
    for cluster in clusters:
        raw[cluster] = sum(
            (weight for support, weight in minimal.items() if support.issubset(cluster)),
            Fraction(0),
        )
    omega: dict[Support, Fraction] = {}
    for cluster in clusters:
        value = raw[cluster]
        for subset in rooted_connected_subsets_of(cluster, root, connected):
            if subset != cluster:
                value -= omega[subset]
        omega[cluster] = value
    if any(omega[cluster] != minimal.get(cluster, Fraction(0)) for cluster in clusters):
        raise AssertionError("exact rooted incidence transform failed recovery")
    return RootedIncidenceResult(
        clusters,
        MappingProxyType(raw),
        MappingProxyType(omega),
    )


@dataclass(frozen=True)
class RootedRawMobiusResult:
    """Independent literal Möbius reduction of actually evaluated raw clusters."""

    clusters: tuple[Support, ...]
    raw: Mapping[Support, Fraction]
    omega: Mapping[Support, Fraction]


def rooted_mobius_from_raw(
    raw_cluster_values: Mapping[Support, Any],
    cluster_poset: Iterable[Support],
    root: int,
    connected: Callable[[Support], bool],
) -> RootedRawMobiusResult:
    """Subtract proper rooted connected subclusters from independent raw data."""
    clusters = tuple(sorted(
        {frozenset(map(int, support)) for support in cluster_poset},
        key=lambda support: (len(support), tuple(sorted(support))),
    ))
    raw_input = {
        frozenset(map(int, support)): as_fraction(value)
        for support, value in raw_cluster_values.items()
    }
    if set(raw_input) != set(clusters):
        missing = set(clusters) - set(raw_input)
        extra = set(raw_input) - set(clusters)
        raise ValueError(f"raw cluster ledger mismatch; missing={missing}, extra={extra}")
    for cluster in clusters:
        if root not in cluster or not connected(cluster):
            raise ValueError("the raw cluster poset must be rooted and connected")
        required = set(rooted_connected_subsets_of(cluster, root, connected))
        absent = required - set(clusters)
        if absent:
            raise ValueError(f"raw cluster poset is not downward closed: {absent}")
    omega: dict[Support, Fraction] = {}
    for cluster in clusters:
        value = raw_input[cluster]
        for subset in rooted_connected_subsets_of(cluster, root, connected):
            if subset != cluster:
                value -= omega[subset]
        omega[cluster] = value
    reconstructed = {
        cluster: sum((
            omega[subset]
            for subset in rooted_connected_subsets_of(cluster, root, connected)
        ), Fraction(0))
        for cluster in clusters
    }
    if reconstructed != raw_input:
        raise AssertionError("literal rooted Möbius round-trip failed")
    return RootedRawMobiusResult(
        clusters,
        MappingProxyType(dict(raw_input)),
        MappingProxyType(omega),
    )


@dataclass(frozen=True)
class RootedEmbedding:
    """Literal injective face map and exact integer multiplicity."""

    face_map: tuple[tuple[int, int], ...]
    canonical_root: int
    concrete_root: int
    multiplicity: int = 1

    def __post_init__(self) -> None:
        mapping = tuple((int(source), int(target)) for source, target in self.face_map)
        if len({source for source, _target in mapping}) != len(mapping):
            raise ValueError("embedding source faces must be unique")
        if len({target for _source, target in mapping}) != len(mapping):
            raise ValueError("embedding must be injective")
        if (int(self.canonical_root), int(self.concrete_root)) not in mapping:
            raise ValueError("embedding must map the canonical root explicitly")
        if int(self.multiplicity) < 1:
            raise ValueError("embedding multiplicity must be positive")
        object.__setattr__(self, "face_map", tuple(sorted(mapping)))
        object.__setattr__(self, "canonical_root", int(self.canonical_root))
        object.__setattr__(self, "concrete_root", int(self.concrete_root))
        object.__setattr__(self, "multiplicity", int(self.multiplicity))

    @property
    def canonical_support(self) -> Support:
        return frozenset(source for source, _target in self.face_map)

    @property
    def concrete_support(self) -> Support:
        return frozenset(target for _source, target in self.face_map)

    def validate_on_patch(self, patch: OpenCubicPatch) -> None:
        mapping = dict(self.face_map)
        valid_faces = set(range(len(patch.faces)))
        if not self.canonical_support.issubset(valid_faces):
            raise ValueError("embedding source leaves the concrete patch")
        if not self.concrete_support.issubset(valid_faces):
            raise ValueError("embedding target leaves the concrete patch")
        for left, right in itertools.combinations(mapping, 2):
            source_adjacent = right in patch.adjacency[left]
            target_adjacent = mapping[right] in patch.adjacency[mapping[left]]
            if source_adjacent != target_adjacent:
                raise ValueError("embedding does not preserve the induced link graph")


_COVERAGE_VERIFICATION_TOKEN = object()


@dataclass(frozen=True)
class EmbeddingCoverageCertificate:
    """Caller-supplied coverage proof; synthetic coverage can never seal m4."""

    embeddings: tuple[RootedEmbedding, ...]
    max_faces: int
    complete: bool
    physical: bool
    authority_sha256: str
    _mechanical_witness: object | None = None

    def __post_init__(self) -> None:
        if int(self.max_faces) < 1:
            raise ValueError("coverage max_faces must be positive")
        digest = str(self.authority_sha256).lower()
        if self.physical and (len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest)):
            raise ValueError("physical coverage requires a 64-hex authority hash")
        object.__setattr__(self, "embeddings", tuple(self.embeddings))
        object.__setattr__(self, "max_faces", int(self.max_faces))
        object.__setattr__(self, "authority_sha256", digest)
        if self._mechanical_witness not in (None, _COVERAGE_VERIFICATION_TOKEN):
            raise ValueError("unknown embedding-coverage witness")

    @property
    def mechanically_verified(self) -> bool:
        return self._mechanical_witness is _COVERAGE_VERIFICATION_TOKEN


def certify_complete_identity_embeddings(
    patch: OpenCubicPatch,
    root: int,
    max_faces: int,
    authority_sha256: str,
) -> EmbeddingCoverageCertificate:
    """Mechanically certify a full rooted adjacency ball without symmetry fitting.

    Every face at graph distance strictly below ``max_faces-1`` must have all
    twelve cubic shared-edge neighbors in the patch.  Then every connected
    rooted cluster with at most ``max_faces`` faces is present.  This deliberately
    uses one literal identity embedding per concrete cluster: no orbit factor is
    guessed or inferred from a target.
    """
    root, max_faces = int(root), int(max_faces)
    clusters = enumerate_rooted_open_clusters(patch, root, max_faces)
    require_complete_rooted_ball(patch, root, max_faces)
    embeddings = tuple(
        RootedEmbedding(
            tuple((face, face) for face in sorted(cluster.support)),
            root,
            root,
            1,
        )
        for cluster in clusters
    )
    certificate = EmbeddingCoverageCertificate(
        embeddings,
        max_faces,
        complete=True,
        physical=True,
        authority_sha256=authority_sha256,
        _mechanical_witness=_COVERAGE_VERIFICATION_TOKEN,
    )
    for embedding in certificate.embeddings:
        embedding.validate_on_patch(patch)
    return certificate


def embedding_sum(
    omega: Mapping[Support, Any],
    coverage: EmbeddingCoverageCertificate,
) -> Fraction:
    exact = {frozenset(map(int, support)): as_fraction(value) for support, value in omega.items()}
    total = Fraction(0)
    for embedding in coverage.embeddings:
        if embedding.canonical_support not in exact:
            raise ValueError(
                f"embedding references absent canonical cluster {embedding.canonical_support}"
            )
        total += embedding.multiplicity * exact[embedding.canonical_support]
    return total


def _json_exact(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, frozenset):
        return sorted(value)
    if isinstance(value, Mapping):
        return {str(key): _json_exact(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json_exact(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    raise TypeError(f"checkpoint value is not deterministic JSON: {type(value).__name__}")


class Phase2CheckpointJournal:
    """Deterministic heartbeat/checkpoint chain with no wall-clock dependence."""

    def __init__(self, retention_limit: int | None = None) -> None:
        if retention_limit is not None and int(retention_limit) < 1:
            raise ValueError("journal retention_limit must be positive")
        self._events: list[Mapping[str, Any]] = []
        self._digest = "0" * 64
        self._event_count = 0
        self._retention_limit = (
            None if retention_limit is None else int(retention_limit)
        )

    @property
    def digest(self) -> str:
        return self._digest

    @property
    def events(self) -> tuple[Mapping[str, Any], ...]:
        return tuple(self._events)

    def heartbeat(
        self,
        stage: str,
        *,
        support: Support | None = None,
        detail: Mapping[str, Any] | None = None,
    ) -> Mapping[str, Any]:
        event = {
            "sequence": self._event_count + 1,
            "stage": str(stage),
            "support": sorted(support) if support is not None else None,
            "detail": _json_exact(dict(detail or {})),
            "previous_sha256": self._digest,
        }
        encoded = json.dumps(event, sort_keys=True, separators=(",", ":")).encode("utf-8")
        self._digest = hashlib.sha256(encoded).hexdigest()
        frozen = MappingProxyType({**event, "event_sha256": self._digest})
        self._event_count += 1
        self._events.append(frozen)
        if (
            self._retention_limit is not None
            and len(self._events) > self._retention_limit
        ):
            del self._events[:len(self._events) - self._retention_limit]
        return frozen

    def checkpoint(self, status: str) -> Mapping[str, Any]:
        return MappingProxyType({
            "status": str(status),
            "event_count": self._event_count,
            "last_event_sha256": self._digest,
            "last_stage": self._events[-1]["stage"] if self._events else None,
        })


@dataclass(frozen=True)
class Phase2AssemblyResult:
    mobius: RootedRawMobiusResult
    embedded_coefficient: Fraction
    coverage: EmbeddingCoverageCertificate
    checkpoint: Mapping[str, Any]
    _physical_witness: object | None

    def __post_init__(self) -> None:
        object.__setattr__(self, "embedded_coefficient", as_fraction(self.embedded_coefficient))
        object.__setattr__(self, "checkpoint", MappingProxyType(dict(self.checkpoint)))
        if self._physical_witness not in (None, _PHYSICAL_EVALUATION_TOKEN):
            raise ValueError("unknown physical-evaluation witness")

    @property
    def physical_cluster_evaluations(self) -> bool:
        return self._physical_witness is _PHYSICAL_EVALUATION_TOKEN


_PHYSICAL_EVALUATION_TOKEN = object()


def _assemble_rooted_gap(
    raw_gap: Mapping[Support, Any],
    clusters: Iterable[Support],
    *,
    root: int,
    connected: Callable[[Support], bool],
    coverage: EmbeddingCoverageCertificate,
    journal: Phase2CheckpointJournal,
    physical_token: object | None,
) -> Phase2AssemblyResult:
    """Target-blind global reduction from independently evaluated raw gaps."""
    journal.heartbeat("raw-clusters-complete", detail={"count": len(raw_gap)})
    mobius = rooted_mobius_from_raw(raw_gap, clusters, root, connected)
    journal.heartbeat("literal-mobius-complete", detail={"count": len(mobius.omega)})
    coefficient = embedding_sum(mobius.omega, coverage)
    journal.heartbeat(
        "embedding-sum-complete",
        detail={"coefficient": coefficient, "embedding_count": len(coverage.embeddings)},
    )
    return Phase2AssemblyResult(
        mobius,
        coefficient,
        coverage,
        journal.checkpoint(PHASE2_COMPONENT_STATUS),
        physical_token,
    )


def assemble_rooted_gap_from_raw(
    raw_gap: Mapping[Support, Any],
    clusters: Iterable[Support],
    *,
    root: int,
    connected: Callable[[Support], bool],
    coverage: EmbeddingCoverageCertificate,
    journal: Phase2CheckpointJournal,
) -> Phase2AssemblyResult:
    """Assemble injected/raw ledgers; this public path is always non-physical."""
    return _assemble_rooted_gap(
        raw_gap,
        clusters,
        root=root,
        connected=connected,
        coverage=coverage,
        journal=journal,
        physical_token=None,
    )


class ExactGlobalMarkedVacuumAssembler:
    """Legacy scalar Phase-2 diagnostic; its result is never sealable."""

    def __init__(
        self,
        builder: ExactFaceInsertionBuilder,
        root: int,
        max_faces: int,
        coverage: EmbeddingCoverageCertificate,
        journal: Phase2CheckpointJournal | None = None,
    ) -> None:
        self.builder = builder
        self.root = int(root)
        self.max_faces = int(max_faces)
        self.coverage = coverage
        self.journal = journal or Phase2CheckpointJournal()
        if coverage.max_faces != self.max_faces:
            raise ValueError("coverage and assembler max_faces disagree")
        for embedding in coverage.embeddings:
            embedding.validate_on_patch(builder.patch)

    def clusters(self) -> tuple[RootedOpenCluster, ...]:
        return enumerate_rooted_open_clusters(
            self.builder.patch, self.root, self.max_faces
        )

    def evaluate(self) -> Phase2AssemblyResult:
        clusters = self.clusters()
        raw: dict[Support, Fraction] = {}
        for cluster in clusters:
            self.journal.heartbeat("cluster-start", support=cluster.support)
            evaluation = evaluate_exact_marked_vacuum_cluster(self.builder, cluster)
            raw[cluster.support] = _sum_ledger(evaluation.gap_fourth)
            self.journal.heartbeat(
                "cluster-exact-complete",
                support=cluster.support,
                detail={
                    "gap": raw[cluster.support],
                    "marked_lower_orders": (
                        _sum_ledger(evaluation.marked_lower.A),
                        _sum_ledger(evaluation.marked_lower.E2),
                        _sum_ledger(evaluation.marked_lower.E3),
                    ),
                    "vacuum_lower_orders": (
                        _sum_ledger(evaluation.vacuum_lower.A),
                        _sum_ledger(evaluation.vacuum_lower.E2),
                        _sum_ledger(evaluation.vacuum_lower.E3),
                    ),
                },
            )
        supports = tuple(cluster.support for cluster in clusters)
        connected = lambda support: connected_in_adjacency(
            support, self.builder.patch.adjacency
        )
        return _assemble_rooted_gap(
            raw,
            supports,
            root=self.root,
            connected=connected,
            coverage=self.coverage,
            journal=self.journal,
            physical_token=_PHYSICAL_EVALUATION_TOKEN,
        )


# -----------------------------------------------------------------------------
# Phase 3: action-decorated full-T1 endpoints and translated operator folds
# -----------------------------------------------------------------------------

EndpointMatrix = Mapping[tuple[int, int], Fraction]


def face_polarization(patch: OpenCubicPatch, face_id: int) -> int:
    """Return the fixed v24c T1 polarization index of a concrete plaquette."""
    axes = patch.face(int(face_id)).axes
    try:
        return T1_POLARIZATION_PLANES.index(axes)
    except ValueError as error:  # pragma: no cover - OpenCubicPatch forbids this.
        raise ValueError(f"face {face_id} has no T1 polarization: axes={axes}") from error


def face_translation_vector(
    patch: OpenCubicPatch,
    source_face: int,
    target_face: int,
) -> Coordinate:
    """Exact open-lattice translation between equally polarized plaquettes."""
    source, target = patch.face(int(source_face)), patch.face(int(target_face))
    if source.axes != target.axes:
        raise ValueError("a face translation cannot change T1 polarization")
    return tuple(
        int(target.anchor[axis]) - int(source.anchor[axis]) for axis in range(3)
    )  # type: ignore[return-value]


def translate_face_open(
    patch: OpenCubicPatch,
    face_id: int,
    displacement: Coordinate,
) -> int:
    """Translate one face inside an explicit open patch, failing at its boundary."""
    face = patch.face(int(face_id))
    translated_anchor = tuple(
        int(face.anchor[axis]) + int(displacement[axis]) for axis in range(3)
    )
    matches = tuple(
        candidate.face_id
        for candidate in patch.faces
        if candidate.anchor == translated_anchor and candidate.axes == face.axes
    )
    if len(matches) != 1:
        raise ProductionNotReady(
            "translated endpoint/support leaves the certified open patch: "
            f"face={face_id}, displacement={tuple(displacement)}"
        )
    return matches[0]


def translate_support_open(
    patch: OpenCubicPatch,
    support: Iterable[int],
    displacement: Coordinate,
) -> FaceSupport:
    return frozenset(
        translate_face_open(patch, face_id, displacement) for face_id in support
    )


@dataclass(frozen=True)
class ActionHistoryLabel:
    """One half-history label retaining the ordered W-insertion ancestry."""

    root_face: int | None
    action_faces: tuple[int, ...] = ()

    def __post_init__(self) -> None:
        if self.root_face is not None and type(self.root_face) is not int:
            raise TypeError("history root face must be an exact integer")
        if any(type(face) is not int for face in self.action_faces):
            raise TypeError("history action faces must be exact integers")
        root = self.root_face
        actions = tuple(self.action_faces)
        if len(actions) > 2:
            raise WOnQ2Forbidden(
                "a half history cannot contain a third W insertion (W on Q2)"
            )
        object.__setattr__(self, "root_face", root)
        object.__setattr__(self, "action_faces", actions)

    @property
    def support(self) -> FaceSupport:
        faces = set(self.action_faces)
        if self.root_face is not None:
            faces.add(self.root_face)
        return frozenset(faces)


ActionLabelledStateVector = Mapping[ActionHistoryLabel, ExactStateVector]


def normalize_action_vector(
    vector: Mapping[ActionHistoryLabel, Mapping[State, Any]],
) -> dict[ActionHistoryLabel, dict[State, Fraction]]:
    return {
        label: exact
        for label, states in vector.items()
        if (exact := normalize_state_vector(states))
    }


def apply_w_action_labelled(
    builder: ExactFaceInsertionBuilder,
    vector: ActionLabelledStateVector,
    allowed_faces: Iterable[int],
    *,
    source_sector: PerturbativeSector,
) -> dict[ActionHistoryLabel, dict[State, Fraction]]:
    """Apply W=-M while retaining both legal insertion faces in order."""
    if source_sector is PerturbativeSector.Q2:
        raise WOnQ2Forbidden("W(Q2) is impossible before any face contraction")
    expected_depth = 0 if source_sector is PerturbativeSector.P else 1
    output: dict[ActionHistoryLabel, dict[State, Fraction]] = defaultdict(
        lambda: defaultdict(Fraction)
    )
    for label, states in normalize_action_vector(vector).items():
        if len(label.action_faces) != expected_depth:
            raise IllegalScheduleTransition(
                f"{source_sector.value} W received history depth "
                f"{len(label.action_faces)}, expected {expected_depth}"
            )
        for face_id in sorted(set(map(int, allowed_faces))):
            target = ActionHistoryLabel(
                label.root_face, label.action_faces + (face_id,)
            )
            for sign in (-1, +1):
                for state, coefficient in builder.insert_face(
                    states, face_id, sign
                ).items():
                    output[target][state] -= coefficient
    return {
        label: normalize_state_vector(states)
        for label, states in output.items()
        if normalize_state_vector(states)
    }


def apply_resolvent_action_labelled(
    vector: ActionLabelledStateVector,
    *,
    power: int = 1,
    reference_energy: Fraction = REFERENCE_E0,
) -> dict[ActionHistoryLabel, dict[State, Fraction]]:
    return {
        label: resolved
        for label, states in normalize_action_vector(vector).items()
        if (resolved := exact_resolvent_vector(
            states, power=int(power), reference_energy=reference_energy
        ))
    }


@dataclass(frozen=True)
class ExactDecoratedHalfHistory:
    P_state: ActionLabelledStateVector
    W1_state: ActionLabelledStateVector
    R1_state: ActionLabelledStateVector
    W2_state: ActionLabelledStateVector
    R2_state: ActionLabelledStateVector
    RR1_state: ActionLabelledStateVector
    RRR1_state: ActionLabelledStateVector
    schedule_trace: tuple[str, ...]


def build_exact_decorated_half_history(
    builder: ExactFaceInsertionBuilder,
    root_face: int | None,
    source_state: Mapping[State, Any],
    allowed_faces: Iterable[int],
    *,
    reference_energy: Fraction,
) -> ExactDecoratedHalfHistory:
    """Build the two-W half history with insertion ancestry retained exactly."""
    allowed = frozenset(map(int, allowed_faces))
    if root_face is not None and int(root_face) not in allowed:
        raise ValueError("a marked half-history root must lie in allowed_faces")
    source: ActionLabelledStateVector = {
        ActionHistoryLabel(root_face, ()): normalize_state_vector(source_state)
    }
    schedule: CanonicalFourthOrderSchedule[ActionLabelledStateVector] = (
        CanonicalFourthOrderSchedule(
            lambda value: apply_w_action_labelled(
                builder, value, allowed, source_sector=PerturbativeSector.P
            ),
            lambda value: apply_resolvent_action_labelled(
                value, reference_energy=as_fraction(reference_energy)
            ),
            lambda value: apply_w_action_labelled(
                builder, value, allowed, source_sector=PerturbativeSector.Q1
            ),
            lambda value: apply_resolvent_action_labelled(
                value, reference_energy=as_fraction(reference_energy)
            ),
        )
    )
    w1 = schedule.first_w(P(source))
    r1 = schedule.first_resolvent(w1)
    w2 = schedule.second_w(r1)
    r2 = schedule.second_resolvent(w2)
    rr1 = apply_resolvent_action_labelled(
        r1.payload, reference_energy=as_fraction(reference_energy)
    )
    rrr1 = apply_resolvent_action_labelled(
        rr1, reference_energy=as_fraction(reference_energy)
    )
    return ExactDecoratedHalfHistory(
        source, w1.payload, r1.payload, w2.payload, r2.payload,
        rr1, rrr1, schedule.trace,
    )


@dataclass(frozen=True)
class EndpointSupportKey:
    """A concrete full-T1 endpoint contribution with all P/action ancestry."""

    support: FaceSupport
    bra_face: int
    ket_face: int
    bra_pol: int
    ket_pol: int
    action_segments: tuple[tuple[int, ...], ...]
    factors: tuple[str, ...]
    route: str = "direct"
    intermediate_faces: tuple[int, ...] = ()
    intermediate_pols: tuple[int, ...] = ()

    def __post_init__(self) -> None:
        integer_fields = (
            tuple(self.support)
            + (self.bra_face, self.ket_face, self.bra_pol, self.ket_pol)
            + tuple(itertools.chain.from_iterable(self.action_segments))
            + tuple(self.intermediate_faces)
            + tuple(self.intermediate_pols)
        )
        if any(type(value) is not int for value in integer_fields):
            raise TypeError("endpoint faces, actions, and polarizations must be exact integers")
        support = frozenset(self.support)
        bra, ket = self.bra_face, self.ket_face
        bra_pol, ket_pol = self.bra_pol, self.ket_pol
        segments = tuple(tuple(segment) for segment in self.action_segments)
        factors = tuple(map(str, self.factors))
        intermediates = tuple(self.intermediate_faces)
        intermediate_pols = tuple(self.intermediate_pols)
        route = str(self.route)
        if bra_pol not in range(3) or ket_pol not in range(3):
            raise ValueError("endpoint polarizations must be 0,1,2")
        if any(pol not in range(3) for pol in intermediate_pols):
            raise ValueError("intermediate polarizations must be 0,1,2")
        if len(intermediates) != len(intermediate_pols):
            raise ValueError("each intermediate P face needs its polarization")
        if not factors:
            raise ValueError("endpoint contribution needs operator-factor provenance")
        if route not in ("direct", "folded"):
            raise ValueError("endpoint route must be direct or folded")
        if route == "direct" and intermediates:
            raise ValueError("a direct endpoint contribution cannot carry a P cut")
        actions = tuple(itertools.chain.from_iterable(segments))
        if len(actions) > 4:
            raise WOnQ2Forbidden("an O(u^4) endpoint contribution has at most four W actions")
        expected_support = frozenset((bra, ket, *intermediates, *actions))
        if support != expected_support:
            raise ValueError(
                "decorated support must equal endpoints, P cuts, and W actions exactly"
            )
        cap = (
            DIRECT_FOURTH_ORDER_MAX_MARKED_FACES
            if route == "direct"
            else FOURTH_ORDER_MAX_MARKED_FACES
        )
        if len(support) > cap:
            raise ValueError(
                f"{route} O(u^4) endpoint support exceeds the exact cap {cap}"
            )
        object.__setattr__(self, "support", support)
        object.__setattr__(self, "bra_face", bra)
        object.__setattr__(self, "ket_face", ket)
        object.__setattr__(self, "bra_pol", bra_pol)
        object.__setattr__(self, "ket_pol", ket_pol)
        object.__setattr__(self, "action_segments", segments)
        object.__setattr__(self, "factors", factors)
        object.__setattr__(self, "route", route)
        object.__setattr__(self, "intermediate_faces", intermediates)
        object.__setattr__(self, "intermediate_pols", intermediate_pols)

    @property
    def action_faces(self) -> tuple[int, ...]:
        return tuple(itertools.chain.from_iterable(self.action_segments))

    @property
    def history_depth(self) -> int:
        return len(self.action_faces)

    def transpose(self) -> "EndpointSupportKey":
        return EndpointSupportKey(
            self.support,
            self.ket_face,
            self.bra_face,
            self.ket_pol,
            self.bra_pol,
            tuple(reversed(self.action_segments)),
            tuple(reversed(self.factors)),
            self.route,
            tuple(reversed(self.intermediate_faces)),
            tuple(reversed(self.intermediate_pols)),
        )


EndpointLedger = Mapping[EndpointSupportKey, Fraction]


def exact_endpoint_ledger(ledger: Mapping[EndpointSupportKey, Any]) -> EndpointLedger:
    output: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    for key, value in ledger.items():
        if not isinstance(key, EndpointSupportKey):
            raise TypeError("endpoint ledgers require EndpointSupportKey keys")
        output[key] += as_fraction(value)
    return MappingProxyType({key: value for key, value in output.items() if value})


def endpoint_inner(
    patch: OpenCubicPatch,
    bra_face: int,
    ket_face: int,
    left: ActionLabelledStateVector,
    right: ActionLabelledStateVector,
    *,
    factor: str,
    normalization: Fraction = Fraction(1, 2),
) -> EndpointLedger:
    """Contract one ordered bra/ket pair and retain every action support."""
    bra_face, ket_face = int(bra_face), int(ket_face)
    output: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    for left_label, left_states in normalize_action_vector(left).items():
        if left_label.root_face != bra_face:
            raise ValueError("left decorated history root does not match bra endpoint")
        for right_label, right_states in normalize_action_vector(right).items():
            if right_label.root_face != ket_face:
                raise ValueError("right decorated history root does not match ket endpoint")
            value = as_fraction(normalization) * exact_vector_inner(
                left_states, right_states
            )
            if not value:
                continue
            support = frozenset(left_label.support | right_label.support)
            key = EndpointSupportKey(
                support,
                bra_face,
                ket_face,
                face_polarization(patch, bra_face),
                face_polarization(patch, ket_face),
                (left_label.action_faces, right_label.action_faces),
                (str(factor),),
            )
            output[key] += value
    return exact_endpoint_ledger(output)


def transpose_endpoint_ledger(ledger: EndpointLedger) -> EndpointLedger:
    return exact_endpoint_ledger({key.transpose(): value for key, value in ledger.items()})


def endpoint_ledger_linear_combination(
    *terms: tuple[Any, EndpointLedger],
) -> EndpointLedger:
    output: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    for scalar, ledger in terms:
        scalar_exact = as_fraction(scalar)
        for key, value in exact_endpoint_ledger(ledger).items():
            output[key] += scalar_exact * value
    return exact_endpoint_ledger(output)


def aggregate_endpoint_matrix(ledger: EndpointLedger) -> EndpointMatrix:
    output: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for key, value in exact_endpoint_ledger(ledger).items():
        output[(key.bra_face, key.ket_face)] += value
    return MappingProxyType({key: value for key, value in output.items() if value})


def _matrix_entry(matrix: EndpointMatrix, bra: int, ket: int) -> Fraction:
    return as_fraction(matrix.get((int(bra), int(ket)), Fraction(0)))


def require_endpoint_hermitian(
    ledger: EndpointLedger,
    faces: Iterable[int],
    name: str,
) -> None:
    matrix = aggregate_endpoint_matrix(ledger)
    for bra in faces:
        for ket in faces:
            if _matrix_entry(matrix, bra, ket) != _matrix_entry(matrix, ket, bra):
                raise ExactEngineError(f"{name} failed exact endpoint Hermiticity")


def require_scalar_endpoint_identity(
    ledger: EndpointLedger,
    faces: Iterable[int],
    name: str,
) -> Fraction:
    concrete = tuple(sorted(set(map(int, faces))))
    matrix = aggregate_endpoint_matrix(ledger)
    diagonal = tuple(_matrix_entry(matrix, face, face) for face in concrete)
    if not diagonal or len(set(diagonal)) != 1:
        raise ExactEngineError(f"{name} is not an exact scalar identity")
    if any(
        _matrix_entry(matrix, bra, ket)
        for bra in concrete for ket in concrete if bra != ket
    ):
        raise ExactEngineError(f"{name} has an exact nonzero off-diagonal entry")
    return diagonal[0]


@dataclass(frozen=True)
class EndpointCompositionResult:
    ledger: EndpointLedger
    audited_paths: tuple[tuple[int, int, int], ...]
    matched_record_products: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "ledger", exact_endpoint_ledger(self.ledger))
        object.__setattr__(
            self,
            "audited_paths",
            tuple(tuple(map(int, path)) for path in self.audited_paths),
        )
        object.__setattr__(
            self, "matched_record_products", int(self.matched_record_products)
        )


def compose_endpoint_ledgers(
    left: EndpointLedger,
    right: EndpointLedger,
    endpoint_faces: Iterable[int],
) -> EndpointCompositionResult:
    """Exact matrix product through every concrete intermediate P endpoint.

    The endpoint set is the translation-expanded finite patch.  Thus matching
    ``left.ket_face == right.bra_face`` is precisely the open-lattice version
    of v24c's translation of the second anchored segment onto the concrete
    intermediate face; its polarization is checked independently.
    """
    faces = tuple(sorted(set(map(int, endpoint_faces))))
    left_index: dict[tuple[int, int], list[tuple[EndpointSupportKey, Fraction]]] = (
        defaultdict(list)
    )
    right_index: dict[tuple[int, int], list[tuple[EndpointSupportKey, Fraction]]] = (
        defaultdict(list)
    )
    for key, value in exact_endpoint_ledger(left).items():
        left_index[(key.bra_face, key.ket_face)].append((key, value))
    for key, value in exact_endpoint_ledger(right).items():
        right_index[(key.bra_face, key.ket_face)].append((key, value))
    output: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    audited: list[tuple[int, int, int]] = []
    matched = 0
    for bra, intermediate, ket in itertools.product(faces, repeat=3):
        audited.append((bra, intermediate, ket))
        for left_key, left_value in left_index.get((bra, intermediate), ()):
            for right_key, right_value in right_index.get((intermediate, ket), ()):
                if left_key.ket_pol != right_key.bra_pol:
                    raise ExactEngineError(
                        "matched intermediate endpoint changed T1 polarization"
                    )
                matched += 1
                support = frozenset(left_key.support | right_key.support)
                key = EndpointSupportKey(
                    support,
                    bra,
                    ket,
                    left_key.bra_pol,
                    right_key.ket_pol,
                    left_key.action_segments + right_key.action_segments,
                    left_key.factors + right_key.factors,
                    "folded",
                    left_key.intermediate_faces
                    + (intermediate,)
                    + right_key.intermediate_faces,
                    left_key.intermediate_pols
                    + (left_key.ket_pol,)
                    + right_key.intermediate_pols,
                )
                output[key] += left_value * right_value
    expected = tuple(itertools.product(faces, repeat=3))
    if tuple(audited) != expected:
        raise AssertionError("endpoint composition did not audit the full ordered cube")
    return EndpointCompositionResult(
        exact_endpoint_ledger(output), tuple(audited), matched
    )


def translate_anchored_endpoint_ledger(
    patch: OpenCubicPatch,
    ledger: EndpointLedger,
    new_ket_face: int,
) -> EndpointLedger:
    """Translate an anchored kernel to a concrete ket endpoint, v24c-style."""
    translated: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    for key, value in exact_endpoint_ledger(ledger).items():
        displacement = face_translation_vector(patch, key.ket_face, new_ket_face)
        new_bra = translate_face_open(patch, key.bra_face, displacement)
        new_intermediates = tuple(
            translate_face_open(patch, face, displacement)
            for face in key.intermediate_faces
        )
        new_segments = tuple(
            tuple(translate_face_open(patch, face, displacement) for face in segment)
            for segment in key.action_segments
        )
        new_support = translate_support_open(patch, key.support, displacement)
        new_key = EndpointSupportKey(
            new_support,
            new_bra,
            int(new_ket_face),
            key.bra_pol,
            key.ket_pol,
            new_segments,
            key.factors,
            key.route,
            new_intermediates,
            key.intermediate_pols,
        )
        translated[new_key] += value
    return exact_endpoint_ledger(translated)


@dataclass(frozen=True)
class ExactFullT1Moments:
    endpoint_faces: tuple[int, ...]
    A: EndpointLedger
    K2: EndpointLedger
    N: EndpointLedger
    J: EndpointLedger
    C1: EndpointLedger
    D: EndpointLedger
    Sigma3: EndpointLedger
    audited_endpoint_pairs: tuple[tuple[int, int], ...]
    a_scalar: Fraction

    def __post_init__(self) -> None:
        faces = tuple(sorted(set(map(int, self.endpoint_faces))))
        expected_pairs = tuple(itertools.product(faces, repeat=2))
        if tuple(self.audited_endpoint_pairs) != expected_pairs:
            raise ValueError("full-T1 moments did not audit every ordered endpoint pair")
        object.__setattr__(self, "endpoint_faces", faces)
        for name, depth in (
            ("A", 1), ("K2", 2), ("N", 2), ("J", 2),
            ("C1", 3), ("D", 4), ("Sigma3", 3),
        ):
            ledger = exact_endpoint_ledger(getattr(self, name))
            for key in ledger:
                if key.route != "direct" or key.history_depth != depth:
                    raise ValueError(
                        f"{name} has a non-direct or wrong-depth endpoint record"
                    )
                if key.bra_face not in faces or key.ket_face not in faces:
                    raise ValueError(f"{name} endpoint leaves the audited P space")
            object.__setattr__(self, name, ledger)
        # PVP must be diagonal before support folds use it as the exact scalar aI.
        if any(key.bra_face != key.ket_face for key in self.A):
            raise ExactEngineError("PVP contains a nonzero support-resolved hopping")
        scalar = require_scalar_endpoint_identity(self.A, faces, "PVP")
        if scalar != as_fraction(self.a_scalar):
            raise ValueError("stored PVP scalar disagrees with the exact endpoint matrix")
        object.__setattr__(self, "a_scalar", scalar)
        for name in ("A", "K2", "N", "J", "D"):
            require_endpoint_hermitian(getattr(self, name), faces, name)


def _full_t1_moment(
    patch: OpenCubicPatch,
    histories: Mapping[int, ExactDecoratedHalfHistory],
    left_attribute: str,
    right_attribute: str,
    factor: str,
) -> EndpointLedger:
    output: dict[EndpointSupportKey, Fraction] = defaultdict(Fraction)
    for bra, ket in itertools.product(sorted(histories), repeat=2):
        contracted = endpoint_inner(
            patch,
            bra,
            ket,
            getattr(histories[bra], left_attribute),
            getattr(histories[ket], right_attribute),
            factor=factor,
            normalization=Fraction(1, 2),
        )
        for key, value in contracted.items():
            output[key] += value
    return exact_endpoint_ledger(output)


def build_exact_full_t1_moments(
    builder: ExactFaceInsertionBuilder,
    histories: Mapping[int, ExactDecoratedHalfHistory],
) -> ExactFullT1Moments:
    """Build every ordered full-T1 endpoint moment; no transpose is guessed."""
    faces = tuple(sorted(map(int, histories)))
    if not faces or set(faces) - set(range(len(builder.patch.faces))):
        raise ValueError("full-T1 histories must be keyed by concrete patch faces")
    for face in faces:
        source_labels = tuple(histories[face].P_state)
        if source_labels != (ActionHistoryLabel(face, ()),):
            raise ValueError("each full-T1 half history needs its own concrete P root")
    a = _full_t1_moment(builder.patch, histories, "P_state", "W1_state", "A")
    k2 = _full_t1_moment(builder.patch, histories, "W1_state", "R1_state", "K2")
    n_ledger = _full_t1_moment(builder.patch, histories, "R1_state", "R1_state", "N")
    j_ledger = _full_t1_moment(builder.patch, histories, "R1_state", "RR1_state", "J")
    c1 = _full_t1_moment(builder.patch, histories, "R1_state", "R2_state", "C1")
    d_ledger = _full_t1_moment(builder.patch, histories, "W2_state", "R2_state", "D")
    sigma3 = _full_t1_moment(
        builder.patch, histories, "R1_state", "W2_state", "Sigma3"
    )
    audited_pairs = tuple(itertools.product(faces, repeat=2))
    a_scalar = require_scalar_endpoint_identity(a, faces, "PVP")
    return ExactFullT1Moments(
        faces, a, k2, n_ledger, j_ledger, c1, d_ledger, sigma3,
        audited_pairs, a_scalar,
    )


@dataclass(frozen=True)
class ExactEndpointFourthOrderLedgers:
    moments: ExactFullT1Moments
    AN: EndpointLedger
    E3: EndpointLedger
    K2N: EndpointLedger
    NK2: EndpointLedger
    AC1: EndpointLedger
    C1tA: EndpointLedger
    AAJ: EndpointLedger
    H4: EndpointLedger
    audited_fold_paths: tuple[tuple[int, int, int], ...]

    def __post_init__(self) -> None:
        for name in ("AN", "E3", "K2N", "NK2", "AC1", "C1tA", "AAJ", "H4"):
            object.__setattr__(self, name, exact_endpoint_ledger(getattr(self, name)))
        expected = tuple(itertools.product(self.moments.endpoint_faces, repeat=3))
        if tuple(self.audited_fold_paths) != expected:
            raise ValueError("folded ledgers did not audit every intermediate endpoint")
        for key in self.H4:
            if key.history_depth != 4:
                raise ValueError("every H4 contribution must contain exactly four W actions")
            if len(key.support) > FOURTH_ORDER_MAX_MARKED_FACES:
                raise ValueError("H4 decorated support exceeded seven faces")
        require_endpoint_hermitian(self.H4, self.moments.endpoint_faces, "H4")


def build_exact_endpoint_fourth_order_ledgers(
    moments: ExactFullT1Moments,
) -> ExactEndpointFourthOrderLedgers:
    """Assemble H2/H3/H4 by literal endpoint operator convolution."""
    faces = moments.endpoint_faces
    an = compose_endpoint_ledgers(moments.A, moments.N, faces)
    e3 = endpoint_ledger_linear_combination((1, moments.Sigma3), (-1, an.ledger))
    k2n = compose_endpoint_ledgers(moments.K2, moments.N, faces)
    nk2 = compose_endpoint_ledgers(moments.N, moments.K2, faces)
    ac1 = compose_endpoint_ledgers(moments.A, moments.C1, faces)
    c1ta = compose_endpoint_ledgers(transpose_endpoint_ledger(moments.C1), moments.A, faces)
    aa = compose_endpoint_ledgers(moments.A, moments.A, faces)
    aaj = compose_endpoint_ledgers(aa.ledger, moments.J, faces)
    h4 = endpoint_ledger_linear_combination(
        (1, moments.D),
        (-1, ac1.ledger),
        (-1, c1ta.ledger),
        (Fraction(-1, 2), k2n.ledger),
        (Fraction(-1, 2), nk2.ledger),
        (1, aaj.ledger),
    )
    expected = tuple(itertools.product(faces, repeat=3))
    for name, result in (
        ("AN", an), ("K2N", k2n), ("NK2", nk2),
        ("AC1", ac1), ("C1tA", c1ta), ("AAJ", aaj),
    ):
        if result.audited_paths != expected:
            raise AssertionError(f"{name} skipped a concrete intermediate endpoint")
    return ExactEndpointFourthOrderLedgers(
        moments, an.ledger, e3, k2n.ledger, nk2.ledger, ac1.ledger,
        c1ta.ledger, aaj.ledger, h4, expected,
    )


_ENDPOINT_PHYSICAL_TOKEN = object()
LOWER_ORDER_GAP_REGRESSION: tuple[Fraction, Fraction, Fraction] = (
    Fraction(1), Fraction(11, 306), Fraction(-109151, 249696)
)


def _endpoint_key_payload(key: EndpointSupportKey) -> Mapping[str, Any]:
    return {
        "support": sorted(key.support),
        "bra_face": key.bra_face,
        "ket_face": key.ket_face,
        "bra_pol": key.bra_pol,
        "ket_pol": key.ket_pol,
        "action_segments": [list(segment) for segment in key.action_segments],
        "factors": list(key.factors),
        "route": key.route,
        "intermediate_faces": list(key.intermediate_faces),
        "intermediate_pols": list(key.intermediate_pols),
    }


def endpoint_ledger_sha256(named_ledgers: Mapping[str, EndpointLedger]) -> str:
    rows: list[Mapping[str, Any]] = []
    for name in sorted(named_ledgers):
        ledger = exact_endpoint_ledger(named_ledgers[name])
        ordered = sorted(
            ledger.items(),
            key=lambda item: json.dumps(
                _endpoint_key_payload(item[0]), sort_keys=True, separators=(",", ":")
            ),
        )
        for key, value in ordered:
            rows.append({
                "ledger": name,
                "key": _endpoint_key_payload(key),
                "value": _json_exact(value),
            })
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def runtime_script_sha256() -> str:
    raw_path = Path(__file__)
    sealed_fd_text = os.environ.get(SEALED_SOURCE_FD_ENV)
    if sealed_fd_text is not None:
        if (
            os.name != "posix"
            or not sealed_fd_text.isascii()
            or not sealed_fd_text.isdecimal()
            or str(int(sealed_fd_text)) != sealed_fd_text
        ):
            raise ProductionNotReady("sealed runtime source descriptor is malformed")
        source_path = Path("/proc/self/fd") / sealed_fd_text
        if raw_path != source_path or not source_path.is_file():
            raise ProductionNotReady(
                "runtime __file__ is not the inherited sealed source descriptor"
            )
    else:
        source_path = raw_path.resolve()
        if not source_path.is_file():
            raise ProductionNotReady("runtime script source is not readable")
    return hashlib.sha256(source_path.read_bytes()).hexdigest()


def _auth_canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def resume_authentication_context_sha256(runtime_sha256: str) -> str:
    """Bind the secret resume domain to this script and sealed geometry authority."""
    if type(runtime_sha256) is not str or runtime_sha256 != runtime_sha256.lower():
        raise ValueError("resume authentication runtime binding must be lowercase text")
    runtime = runtime_sha256
    if len(runtime) != 64 or any(ch not in "0123456789abcdef" for ch in runtime):
        raise ValueError("resume authentication runtime binding is not SHA256")
    payload = {
        "schema": RESUME_AUTH_SCHEMA,
        "runtime_script_sha256": runtime,
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "candidate_coverage_certificate_sha256": (
            O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256
        ),
        "candidate_preflight_sha256": O4_TRIALITY_CANDIDATE_PREFLIGHT_SHA256,
        "physical_cluster_evaluations": 609,
        "source_authority_sha256": {
            key: value["sha256"] for key, value in SOURCE_AUTHORITIES.items()
        },
    }
    return hashlib.sha256(_auth_canonical_bytes(payload)).hexdigest()


def _resume_hmac_sha256(
    key: bytes,
    domain: str,
    payload: Any,
) -> str:
    if type(key) is not bytes or len(key) != 32:
        raise ValueError("resume authentication key must be exactly 32 bytes")
    message = (
        b"HODGE-SU3-RESUME-HMAC-v1\x00"
        + domain.encode("ascii")
        + b"\x00"
        + _auth_canonical_bytes(payload)
    )
    return hmac.new(key, message, hashlib.sha256).hexdigest()


def derive_resume_authentication_key(
    recovery_secret: str,
    resume_salt_hex: str,
    resume_run_id: str,
    authentication_context_sha256: str,
) -> bytes:
    """Derive the 32-byte resume HMAC key from a generated 256-bit secret."""
    if (
        type(recovery_secret) is not str
        or not recovery_secret.startswith(RECOVERY_SECRET_PREFIX)
        or len(recovery_secret) != len(RECOVERY_SECRET_PREFIX) + 64
    ):
        raise ValueError("recovery secret must use the generated 256-bit format")
    secret_hex = recovery_secret[len(RECOVERY_SECRET_PREFIX):]
    if any(ch not in "0123456789abcdef" for ch in secret_hex):
        raise ValueError("recovery secret must use lowercase hexadecimal entropy")
    exact_tokens: list[str] = []
    for label, token in (
        ("salt", resume_salt_hex),
        ("run id", resume_run_id),
        ("context", authentication_context_sha256),
    ):
        if (
            type(token) is not str
            or token != token.lower()
            or len(token) != 64
            or any(ch not in "0123456789abcdef" for ch in token)
        ):
            raise ValueError(f"resume {label} must be exact lowercase 32-byte hex")
        exact_tokens.append(token)
    kdf_salt = RESUME_KDF_DOMAIN + b"".join(
        bytes.fromhex(token) for token in exact_tokens
    )
    return hashlib.pbkdf2_hmac(
        "sha256",
        recovery_secret.encode("ascii"),
        kdf_salt,
        RESUME_KDF_ITERATIONS,
        dklen=32,
    )


@dataclass(frozen=True, repr=False)
class ResumeAuthentication:
    key: bytes = field(repr=False)
    resume_salt_hex: str
    resume_run_id: str
    authentication_context_sha256: str
    invocation_nonce: str
    certificate_output_fd: int | None = None

    def __post_init__(self) -> None:
        if type(self.key) is not bytes or len(self.key) != 32:
            raise ValueError("resume authentication key must be exactly 32 bytes")
        for label, token in (
            ("salt", self.resume_salt_hex),
            ("run id", self.resume_run_id),
            ("context", self.authentication_context_sha256),
            ("invocation nonce", self.invocation_nonce),
        ):
            if type(token) is not str or token != token.lower():
                raise ValueError(
                    f"resume authentication {label} must be lowercase hexadecimal text"
                )
            exact = token
            if len(exact) != 64 or any(ch not in "0123456789abcdef" for ch in exact):
                raise ValueError(f"resume authentication {label} must be 32-byte hex")
            object.__setattr__(
                self,
                {
                    "salt": "resume_salt_hex",
                    "run id": "resume_run_id",
                    "context": "authentication_context_sha256",
                    "invocation nonce": "invocation_nonce",
                }[label],
                exact,
            )
        if self.certificate_output_fd is not None and (
            type(self.certificate_output_fd) is not int
            or self.certificate_output_fd < 0
        ):
            raise ValueError("certificate output descriptor must be an exact nonnegative int")


def _sealed_memfd_candidates(name: str) -> tuple[int, ...]:
    if os.name != "posix" or not Path("/proc/self/fd").is_dir():
        return ()
    matches: list[int] = []
    for entry in Path("/proc/self/fd").iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            target = os.readlink(entry)
        except OSError:
            continue
        if f"memfd:{name}" in target:
            matches.append(int(entry.name))
    return tuple(sorted(matches))


def load_resume_authentication_from_sealed_fd() -> ResumeAuthentication:
    """Read the one inherited sealed secret bundle without argv/env/path exposure."""
    candidates = _sealed_memfd_candidates(RESUME_AUTH_MEMFD_NAME)
    if len(candidates) != 1:
        raise ProductionNotReady(
            "physical resume requires exactly one inherited sealed authentication fd"
        )
    fd = candidates[0]
    try:
        import fcntl

        required = (
            fcntl.F_SEAL_WRITE
            | fcntl.F_SEAL_SHRINK
            | fcntl.F_SEAL_GROW
            | fcntl.F_SEAL_SEAL
        )
        if int(fcntl.fcntl(fd, fcntl.F_GET_SEALS)) != required:
            raise ProductionNotReady("resume authentication fd is not irreversibly sealed")
        raw = os.pread(fd, 4097, 0)
        if not raw or len(raw) > 4096:
            raise ProductionNotReady("resume authentication bundle has invalid size")
        bundle = _strict_json_loads(raw.decode("utf-8"))
        if type(bundle) is not dict or set(bundle) != {
            "schema", "key_hex", "resume_salt_hex", "resume_run_id",
            "authentication_context_sha256", "invocation_nonce",
            "certificate_output_fd",
        }:
            raise ProductionNotReady("resume authentication bundle schema changed")
        if bundle["schema"] != RESUME_AUTH_SCHEMA:
            raise ProductionNotReady("resume authentication bundle version changed")
        key_hex = bundle["key_hex"]
        if (
            type(key_hex) is not str
            or len(key_hex) != 64
            or any(ch not in "0123456789abcdef" for ch in key_hex)
        ):
            raise ProductionNotReady("resume authentication key encoding is invalid")
        authentication = ResumeAuthentication(
            bytes.fromhex(key_hex),
            bundle["resume_salt_hex"],
            bundle["resume_run_id"],
            bundle["authentication_context_sha256"],
            bundle["invocation_nonce"],
            bundle["certificate_output_fd"],
        )
    except (OSError, UnicodeError, ValueError) as error:
        raise ProductionNotReady("resume authentication fd cannot be decoded") from error
    finally:
        try:
            os.close(fd)
        except OSError:
            pass
    output_candidates = _sealed_memfd_candidates(CERTIFICATE_OUTPUT_MEMFD_NAME)
    if (
        authentication.certificate_output_fd is None
        or output_candidates != (authentication.certificate_output_fd,)
    ):
        raise ProductionNotReady("authenticated certificate output fd is missing or ambiguous")
    try:
        import fcntl

        output_fd = authentication.certificate_output_fd
        if (
            int(fcntl.fcntl(output_fd, fcntl.F_GET_SEALS)) != 0
            or os.fstat(output_fd).st_size != 0
        ):
            raise ProductionNotReady(
                "authenticated certificate output fd was not supplied empty and unsealed"
            )
    except OSError as error:
        raise ProductionNotReady(
            "authenticated certificate output fd cannot be inspected"
        ) from error
    return authentication


def emit_authenticated_certificate_to_memfd(
    authentication: ResumeAuthentication,
    encoded_certificate: bytes,
) -> None:
    """Write final bytes once to the inherited output memfd and seal them."""
    fd = authentication.certificate_output_fd
    if fd is None or len(encoded_certificate) == 0 or len(encoded_certificate) > 64 << 20:
        raise ProductionNotReady("authenticated certificate output is unavailable or oversized")
    candidates = _sealed_memfd_candidates(CERTIFICATE_OUTPUT_MEMFD_NAME)
    if candidates != (fd,):
        raise ProductionNotReady("authenticated certificate output descriptor changed")
    try:
        import fcntl

        if int(fcntl.fcntl(fd, fcntl.F_GET_SEALS)) != 0:
            raise ProductionNotReady("certificate output fd was sealed before construction")
        os.ftruncate(fd, 0)
        offset = 0
        while offset < len(encoded_certificate):
            written = os.pwrite(fd, encoded_certificate[offset:], offset)
            if written <= 0:
                raise OSError("short write to authenticated certificate memfd")
            offset += written
        os.fsync(fd)
        required = (
            fcntl.F_SEAL_WRITE
            | fcntl.F_SEAL_SHRINK
            | fcntl.F_SEAL_GROW
            | fcntl.F_SEAL_SEAL
        )
        fcntl.fcntl(fd, fcntl.F_ADD_SEALS, required)
        if int(fcntl.fcntl(fd, fcntl.F_GET_SEALS)) != required:
            raise ProductionNotReady("certificate output fd seals are incomplete")
    except OSError as error:
        raise ProductionNotReady("authenticated certificate output failed") from error


def clear_exact_cluster_working_caches() -> None:
    """Bound RAM between independent concrete-cluster evaluations."""
    _HAAR_CACHE.clear()
    _resolved_seed_cached.cache_clear()
    if sp is not None:
        try:
            sp.core.cache.clear_cache()
        except AttributeError:  # pragma: no cover - version-specific SymPy API.
            pass


@dataclass(frozen=True)
class EndpointCoverageCertificate:
    """Mechanical certificate for one translation-expanded cluster P space."""

    cluster_support: FaceSupport
    endpoint_faces: tuple[int, ...]
    audited_endpoint_pairs: tuple[tuple[int, int], ...]
    audited_fold_paths: tuple[tuple[int, int, int], ...]
    polarization_pairs: tuple[tuple[int, int], ...]
    polarization_triples: tuple[tuple[int, int, int], ...]
    direct_support_histogram: Mapping[int, int]
    folded_support_histogram: Mapping[int, int]
    ledger_sha256: str
    certificate_sha256: str
    complete: bool
    _physical_witness: object | None = None

    def __post_init__(self) -> None:
        support = frozenset(map(int, self.cluster_support))
        faces = tuple(sorted(set(map(int, self.endpoint_faces))))
        pairs = tuple(tuple(map(int, pair)) for pair in self.audited_endpoint_pairs)
        triples = tuple(tuple(map(int, path)) for path in self.audited_fold_paths)
        expected_pairs = tuple(itertools.product(faces, repeat=2))
        expected_triples = tuple(itertools.product(faces, repeat=3))
        if faces != tuple(sorted(support)):
            raise ValueError("endpoint coverage must include every cluster P face")
        if pairs != expected_pairs or triples != expected_triples:
            raise ValueError("endpoint coverage omitted an ordered pair or P-cut path")
        direct_hist = {int(size): int(count) for size, count in self.direct_support_histogram.items()}
        folded_hist = {int(size): int(count) for size, count in self.folded_support_histogram.items()}
        if any(size > DIRECT_FOURTH_ORDER_MAX_MARKED_FACES for size in direct_hist):
            raise ValueError("direct endpoint census exceeds six marked faces")
        if any(size > FOURTH_ORDER_MAX_MARKED_FACES for size in folded_hist):
            raise ValueError("folded endpoint census exceeds seven marked faces")
        digest = str(self.ledger_sha256).lower()
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ValueError("endpoint coverage needs the exact ledger SHA256")
        certificate_digest = str(self.certificate_sha256).lower()
        if len(certificate_digest) != 64 or any(
            ch not in "0123456789abcdef" for ch in certificate_digest
        ):
            raise ValueError("endpoint coverage needs the structural certificate SHA256")
        if self._physical_witness not in (None, _ENDPOINT_PHYSICAL_TOKEN):
            raise ValueError("unknown endpoint physical witness")
        object.__setattr__(self, "cluster_support", support)
        object.__setattr__(self, "endpoint_faces", faces)
        object.__setattr__(self, "audited_endpoint_pairs", pairs)
        object.__setattr__(self, "audited_fold_paths", triples)
        object.__setattr__(self, "direct_support_histogram", MappingProxyType(direct_hist))
        object.__setattr__(self, "folded_support_histogram", MappingProxyType(folded_hist))
        object.__setattr__(self, "ledger_sha256", digest)
        object.__setattr__(self, "certificate_sha256", certificate_digest)

    @property
    def physical(self) -> bool:
        return self._physical_witness is _ENDPOINT_PHYSICAL_TOKEN


def certify_endpoint_cluster_coverage(
    patch: OpenCubicPatch,
    cluster: RootedOpenCluster,
    moments: ExactFullT1Moments,
    fourth: ExactEndpointFourthOrderLedgers,
    *,
    physical_token: object | None,
) -> EndpointCoverageCertificate:
    """Bind all endpoint moments and folded paths to one exact cluster digest."""
    faces = tuple(sorted(cluster.support))
    if moments.endpoint_faces != faces:
        raise ValueError("moment P space differs from the concrete cluster support")
    if fourth.moments is not moments:
        raise ValueError("fourth-order ledger is not bound to the supplied moments")
    if physical_token not in (None, _ENDPOINT_PHYSICAL_TOKEN):
        raise ValueError("unknown endpoint certificate witness")
    named = {
        "A": moments.A,
        "K2": moments.K2,
        "N": moments.N,
        "J": moments.J,
        "C1": moments.C1,
        "D": moments.D,
        "Sigma3": moments.Sigma3,
        "AN": fourth.AN,
        "E3": fourth.E3,
        "K2N": fourth.K2N,
        "NK2": fourth.NK2,
        "AC1": fourth.AC1,
        "C1tA": fourth.C1tA,
        "AAJ": fourth.AAJ,
        "H4": fourth.H4,
    }
    direct_hist: dict[int, int] = defaultdict(int)
    folded_hist: dict[int, int] = defaultdict(int)
    for ledger in named.values():
        for key in ledger:
            if not key.support.issubset(cluster.support):
                raise ValueError("endpoint contribution leaves its concrete cluster")
            if face_polarization(patch, key.bra_face) != key.bra_pol:
                raise ValueError("bra endpoint polarization provenance is false")
            if face_polarization(patch, key.ket_face) != key.ket_pol:
                raise ValueError("ket endpoint polarization provenance is false")
            for face, pol in zip(key.intermediate_faces, key.intermediate_pols):
                if face_polarization(patch, face) != pol:
                    raise ValueError("intermediate P-cut polarization provenance is false")
            histogram = direct_hist if key.route == "direct" else folded_hist
            histogram[len(key.support)] += 1
    pol_by_face = {face: face_polarization(patch, face) for face in faces}
    pol_pairs = tuple(sorted({
        (pol_by_face[bra], pol_by_face[ket])
        for bra, ket in moments.audited_endpoint_pairs
    }))
    pol_triples = tuple(sorted({
        (pol_by_face[bra], pol_by_face[mid], pol_by_face[ket])
        for bra, mid, ket in fourth.audited_fold_paths
    }))
    ledger_digest = endpoint_ledger_sha256(named)
    structural_payload = {
        "cluster_support": list(faces),
        "endpoint_pairs": [list(pair) for pair in moments.audited_endpoint_pairs],
        "fold_paths": [list(path) for path in fourth.audited_fold_paths],
        "polarization_pairs": [list(pair) for pair in pol_pairs],
        "polarization_triples": [list(path) for path in pol_triples],
        "direct_support_histogram": dict(sorted(direct_hist.items())),
        "folded_support_histogram": dict(sorted(folded_hist.items())),
        "ledger_sha256": ledger_digest,
    }
    certificate_digest = hashlib.sha256(
        json.dumps(
            structural_payload, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")
    ).hexdigest()
    return EndpointCoverageCertificate(
        cluster.support,
        faces,
        moments.audited_endpoint_pairs,
        fourth.audited_fold_paths,
        pol_pairs,
        pol_triples,
        MappingProxyType(dict(direct_hist)),
        MappingProxyType(dict(folded_hist)),
        ledger_digest,
        certificate_digest,
        complete=True,
        _physical_witness=physical_token,
    )


def endpoint_row_sums_by_polarization(
    patch: OpenCubicPatch,
    ledger: EndpointLedger,
    bra_face: int,
) -> tuple[Fraction, Fraction, Fraction]:
    matrix = aggregate_endpoint_matrix(ledger)
    output = [Fraction(0), Fraction(0), Fraction(0)]
    for ket in sorted({key.ket_face for key in ledger}):
        output[face_polarization(patch, ket)] += _matrix_entry(
            matrix, int(bra_face), ket
        )
    return tuple(output)  # type: ignore[return-value]


@dataclass(frozen=True)
class ExactEndpointClusterEvaluation:
    cluster: RootedOpenCluster
    moments: ExactFullT1Moments
    fourth: ExactEndpointFourthOrderLedgers
    marked_rows_by_order: tuple[tuple[Fraction, Fraction, Fraction], ...]
    vacuum_by_order: tuple[Fraction, Fraction, Fraction, Fraction]
    gap_rows_by_order: tuple[tuple[Fraction, Fraction, Fraction], ...]
    coverage: EndpointCoverageCertificate

    def __post_init__(self) -> None:
        if len(self.marked_rows_by_order) != 4 or len(self.gap_rows_by_order) != 4:
            raise ValueError("cluster evaluation needs orders one through four")
        root_pol = face_polarization(self.cluster.patch, self.cluster.root)
        expected: list[tuple[Fraction, Fraction, Fraction]] = []
        for order, marked in enumerate(self.marked_rows_by_order):
            row = tuple(as_fraction(value) for value in marked)
            if len(row) != 3:
                raise ValueError("full-T1 row must have three output polarizations")
            gap = list(row)
            gap[root_pol] -= as_fraction(self.vacuum_by_order[order])
            expected.append(tuple(gap))  # type: ignore[arg-type]
        normalized_gap = tuple(
            tuple(as_fraction(value) for value in row)
            for row in self.gap_rows_by_order
        )
        if normalized_gap != tuple(expected):
            raise ValueError("full-T1 gap row is not marked minus diagonal vacuum")
        if not self.coverage.physical or not self.coverage.complete:
            raise ValueError("physical cluster evaluation needs physical endpoint coverage")
        object.__setattr__(
            self, "marked_rows_by_order",
            tuple(tuple(as_fraction(value) for value in row) for row in self.marked_rows_by_order),
        )
        object.__setattr__(
            self, "vacuum_by_order",
            tuple(as_fraction(value) for value in self.vacuum_by_order),
        )
        object.__setattr__(self, "gap_rows_by_order", normalized_gap)


def evaluate_exact_endpoint_marked_vacuum_cluster(
    builder: ExactFaceInsertionBuilder,
    cluster: RootedOpenCluster,
) -> ExactEndpointClusterEvaluation:
    """Heavy user-run path: exact full-T1 marked block and independent vacuum."""
    if builder.patch is not cluster.patch:
        raise ValueError("cluster and exact face builder must share the patch")
    histories = {
        face: build_exact_decorated_half_history(
            builder,
            face,
            builder.source_axial(face),
            cluster.support,
            reference_energy=REFERENCE_E0,
        )
        for face in sorted(cluster.support)
    }
    moments = build_exact_full_t1_moments(builder, histories)
    fourth = build_exact_endpoint_fourth_order_ledgers(moments)
    marked_rows = (
        endpoint_row_sums_by_polarization(builder.patch, moments.A, cluster.root),
        endpoint_row_sums_by_polarization(builder.patch, moments.K2, cluster.root),
        endpoint_row_sums_by_polarization(builder.patch, fourth.E3, cluster.root),
        endpoint_row_sums_by_polarization(builder.patch, fourth.H4, cluster.root),
    )
    vacuum_source = {frozenset(): {EMPTY_STATE: Fraction(1)}}
    vacuum_history = build_exact_half_history(
        builder,
        vacuum_source,
        cluster.support,
        reference_energy=Fraction(0),
        normalization=Fraction(1),
    )
    vacuum_lower = lower_order_ledgers_from_history(
        vacuum_history, normalization=Fraction(1)
    )
    vacuum_fourth = fourth_order_ledgers_from_history(
        vacuum_history, normalization=Fraction(1)
    )
    vacuum = (
        _sum_ledger(vacuum_lower.A),
        _sum_ledger(vacuum_lower.E2),
        _sum_ledger(vacuum_lower.E3),
        _sum_ledger(vacuum_fourth.E4),
    )
    if vacuum[0] != 0:
        raise ExactEngineError("vacuum first-order coefficient must vanish exactly")
    root_pol = face_polarization(builder.patch, cluster.root)
    gap_rows = []
    for order, row in enumerate(marked_rows):
        gap = list(row)
        gap[root_pol] -= vacuum[order]
        gap_rows.append(tuple(gap))
    certificate = certify_endpoint_cluster_coverage(
        builder.patch,
        cluster,
        moments,
        fourth,
        physical_token=_ENDPOINT_PHYSICAL_TOKEN,
    )
    return ExactEndpointClusterEvaluation(
        cluster,
        moments,
        fourth,
        marked_rows,
        vacuum,
        tuple(gap_rows),
        certificate,
    )


def _exact_gamma_scalar(
    gamma: Sequence[Sequence[Any]],
    name: str,
) -> Fraction:
    if len(gamma) != 3 or any(len(row) != 3 for row in gamma):
        raise ValueError(f"{name} must be a 3x3 full-T1 Gamma block")
    exact = tuple(tuple(as_fraction(value) for value in row) for row in gamma)
    if any(exact[row][column] for row in range(3) for column in range(3) if row != column):
        raise ExactEngineError(f"{name} has a nonzero cross-polarization Gamma entry")
    diagonal = tuple(exact[index][index] for index in range(3))
    if len(set(diagonal)) != 1:
        raise ExactEngineError(f"{name} Gamma diagonal is not cubic/scalar")
    return diagonal[0]


@dataclass(frozen=True)
class Phase3AssemblyResult:
    mobius_by_channel: Mapping[tuple[int, int, int], RootedRawMobiusResult]
    gamma_by_order: tuple[tuple[tuple[Fraction, ...], ...], ...]
    lower_coefficients: tuple[Fraction, Fraction, Fraction]
    coefficient: Fraction
    coverages: Mapping[int, EmbeddingCoverageCertificate]
    endpoint_certificate_sha256: str
    runtime_script_sha256: str
    authenticated_resume_manifest: Mapping[str, Any]
    checkpoint: Mapping[str, Any]
    _physical_witness: object | None

    def __post_init__(self) -> None:
        gamma = tuple(
            tuple(tuple(as_fraction(value) for value in row) for row in matrix)
            for matrix in self.gamma_by_order
        )
        if len(gamma) != 4:
            raise ValueError("Phase3 result needs Gamma blocks for orders one through four")
        derived = tuple(_exact_gamma_scalar(matrix, f"order-{index + 1}") for index, matrix in enumerate(gamma))
        lower = tuple(as_fraction(value) for value in self.lower_coefficients)
        if lower != derived[:3] or as_fraction(self.coefficient) != derived[3]:
            raise ValueError("stored coefficients disagree with exact Gamma blocks")
        if self._physical_witness not in (None, _ENDPOINT_PHYSICAL_TOKEN):
            raise ValueError("unknown Phase3 physical witness")
        coverages = dict(self.coverages)
        if set(coverages) != {0, 1, 2}:
            raise ValueError("Phase3 result needs exactly three T1 coverage certificates")
        mobius = dict(self.mobius_by_channel)
        expected_channels = {
            (order, input_pol, output_pol)
            for order in range(1, 5)
            for input_pol in range(3)
            for output_pol in range(3)
        }
        if set(mobius) != expected_channels:
            raise ValueError("Phase3 result omitted an order/polarization Möbius channel")
        for (order, input_pol, output_pol), reduced in mobius.items():
            cluster_set = set(reduced.clusters)
            expected_clusters = {
                embedding.canonical_support
                for embedding in coverages[input_pol].embeddings
            }
            if (
                cluster_set != expected_clusters
                or set(reduced.raw) != cluster_set
                or set(reduced.omega) != cluster_set
            ):
                raise ValueError("Möbius channel and physical embedding universe disagree")
            for cluster in reduced.clusters:
                reconstructed = sum((
                    as_fraction(value)
                    for support, value in reduced.omega.items()
                    if support.issubset(cluster)
                ), Fraction(0))
                if reconstructed != as_fraction(reduced.raw[cluster]):
                    raise ValueError("Möbius channel failed its exact raw round trip")
            if embedding_sum(reduced.omega, coverages[input_pol]) != gamma[
                order - 1
            ][input_pol][output_pol]:
                raise ValueError("Gamma entry is not the exact embedded Möbius sum")
        digest = str(self.endpoint_certificate_sha256).lower()
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ValueError("Phase3 endpoint certificate chain needs SHA256")
        runtime_digest = str(self.runtime_script_sha256).lower()
        if len(runtime_digest) != 64 or any(
            ch not in "0123456789abcdef" for ch in runtime_digest
        ):
            raise ValueError("Phase3 result needs its runtime script SHA256")
        resume_manifest = dict(self.authenticated_resume_manifest)
        expected_resume_keys = {
            "schema", "configuration_sha256", "runtime_script_sha256",
            "authentication_context_sha256", "resume_run_id",
            "candidate_manifest_sha256", "row_count", "entries",
            "manifest_sha256", "manifest_hmac_sha256",
            "row_manifest_sha256", "row_manifest_hmac_sha256",
            "invocation_nonce", "current_run_sha256",
            "fresh_cluster_evaluations", "resumed_cluster_evaluations",
            "current_run_hmac_sha256",
        }
        if set(resume_manifest) != expected_resume_keys:
            raise ValueError("Phase3 authenticated resume manifest schema changed")
        entries = resume_manifest["entries"]
        if (
            resume_manifest["schema"]
            != "HODGE-SU3-AUTHENTICATED-ROW-MANIFEST-v1"
            or resume_manifest["runtime_script_sha256"] != runtime_digest
            or resume_manifest["candidate_manifest_sha256"]
            != O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
            or resume_manifest["row_count"] != 609
            or type(entries) is not list
            or len(entries) != 609
            or type(resume_manifest["fresh_cluster_evaluations"]) is not int
            or type(resume_manifest["resumed_cluster_evaluations"]) is not int
            or resume_manifest["fresh_cluster_evaluations"] < 0
            or resume_manifest["resumed_cluster_evaluations"] < 0
            or resume_manifest["fresh_cluster_evaluations"]
            + resume_manifest["resumed_cluster_evaluations"] != 609
            or resume_manifest["manifest_sha256"]
            != resume_manifest["row_manifest_sha256"]
            or resume_manifest["manifest_hmac_sha256"]
            != resume_manifest["row_manifest_hmac_sha256"]
        ):
            raise ValueError("Phase3 authenticated resume manifest invariants failed")
        entry_keys = [
            (entry.get("input_pol"), entry.get("support_json"))
            for entry in entries
            if type(entry) is dict
        ]
        if (
            len(entry_keys) != 609
            or entry_keys != sorted(entry_keys)
            or len(set(entry_keys)) != 609
            or any(
                set(entry) != {
                    "input_pol", "support_json", "record_hmac_sha256"
                }
                for entry in entries
            )
            or any(
                type(entry["record_hmac_sha256"]) is not str
                or len(entry["record_hmac_sha256"]) != 64
                for entry in entries
            )
        ):
            raise ValueError("Phase3 authenticated row manifest entries are invalid")
        for key in (
            "configuration_sha256", "authentication_context_sha256",
            "resume_run_id", "invocation_nonce", "manifest_sha256",
            "manifest_hmac_sha256", "current_run_sha256",
            "current_run_hmac_sha256",
        ):
            token = resume_manifest[key]
            if type(token) is not str or len(token) != 64 or any(
                ch not in "0123456789abcdef" for ch in token
            ):
                raise ValueError(f"Phase3 resume manifest {key} is not SHA256")
        manifest_payload = {
            key: resume_manifest[key]
            for key in (
                "schema", "configuration_sha256", "runtime_script_sha256",
                "authentication_context_sha256", "resume_run_id",
                "candidate_manifest_sha256", "row_count", "entries",
            )
        }
        if hashlib.sha256(_auth_canonical_bytes(manifest_payload)).hexdigest() != (
            resume_manifest["manifest_sha256"]
        ):
            raise ValueError("Phase3 public row-manifest SHA256 does not reproduce")
        current_run_payload = {
            "schema": AUTHENTICATED_EXECUTION_ATTESTATION_SCHEMA,
            "configuration_sha256": resume_manifest["configuration_sha256"],
            "runtime_script_sha256": runtime_digest,
            "authentication_context_sha256": resume_manifest[
                "authentication_context_sha256"
            ],
            "resume_run_id": resume_manifest["resume_run_id"],
            "invocation_nonce": resume_manifest["invocation_nonce"],
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "row_manifest_sha256": resume_manifest["row_manifest_sha256"],
            "row_manifest_hmac_sha256": resume_manifest[
                "row_manifest_hmac_sha256"
            ],
            "fresh_cluster_evaluations": resume_manifest[
                "fresh_cluster_evaluations"
            ],
            "resumed_cluster_evaluations": resume_manifest[
                "resumed_cluster_evaluations"
            ],
        }
        if hashlib.sha256(_auth_canonical_bytes(current_run_payload)).hexdigest() != (
            resume_manifest["current_run_sha256"]
        ):
            raise ValueError("Phase3 current-run attestation SHA256 does not reproduce")
        object.__setattr__(self, "gamma_by_order", gamma)
        object.__setattr__(self, "lower_coefficients", lower)
        object.__setattr__(self, "coefficient", as_fraction(self.coefficient))
        object.__setattr__(self, "coverages", MappingProxyType(coverages))
        object.__setattr__(self, "checkpoint", MappingProxyType(dict(self.checkpoint)))
        object.__setattr__(self, "endpoint_certificate_sha256", digest)
        object.__setattr__(self, "runtime_script_sha256", runtime_digest)
        object.__setattr__(
            self,
            "authenticated_resume_manifest",
            MappingProxyType(resume_manifest),
        )
        object.__setattr__(self, "mobius_by_channel", MappingProxyType(mobius))

    @property
    def physical_cluster_evaluations(self) -> bool:
        return self._physical_witness is _ENDPOINT_PHYSICAL_TOKEN


def phase3_configuration_sha256(
    patch: OpenCubicPatch,
    roots_by_pol: Mapping[int, int],
    coverages: Mapping[int, EmbeddingCoverageCertificate],
    max_faces: int,
) -> str:
    """Bind resume data to the exact concrete geometry and coverage authorities."""
    def embedding_universe_sha256(
        coverage: EmbeddingCoverageCertificate,
    ) -> str:
        digest = hashlib.sha256()
        for embedding in coverage.embeddings:
            encoded = json.dumps(
                {
                    "face_map": [list(pair) for pair in embedding.face_map],
                    "canonical_root": embedding.canonical_root,
                    "concrete_root": embedding.concrete_root,
                    "multiplicity": embedding.multiplicity,
                },
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ).encode("utf-8")
            digest.update(len(encoded).to_bytes(8, "big"))
            digest.update(encoded)
        return digest.hexdigest()

    payload = {
        "schema": "HODGE-SU3-PHASE3-TRIALITY-CANDIDATE-CONFIG-v2",
        "max_faces": int(max_faces),
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "candidate_physics_evaluation_count": 609,
        "roots_by_pol": {str(pol): int(face) for pol, face in sorted(roots_by_pol.items())},
        "faces": [
            {
                "face_id": face.face_id,
                "anchor": list(face.anchor),
                "axes": list(face.axes),
                "steps": [list(step) for step in face.steps],
            }
            for face in patch.faces
        ],
        "adjacency": [
            {
                "face": int(face),
                "neighbors": sorted(map(int, patch.adjacency[face])),
            }
            for face in sorted(patch.adjacency)
        ],
        "coverages": {
            str(pol): {
                "max_faces": coverage.max_faces,
                "complete": coverage.complete,
                "physical": coverage.physical,
                "mechanically_verified": coverage.mechanically_verified,
                "authority_sha256": coverage.authority_sha256,
                "embedding_count": len(coverage.embeddings),
                "embedding_universe_sha256": embedding_universe_sha256(coverage),
            }
            for pol, coverage in sorted(coverages.items())
        },
        "source_authorities": {
            key: value["sha256"] for key, value in SOURCE_AUTHORITIES.items()
        },
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode(
            "utf-8"
        )
    ).hexdigest()


def _strict_json_loads(text: str) -> Any:
    def reject_pairs(pairs: Sequence[tuple[str, Any]]) -> Mapping[str, Any]:
        output: dict[str, Any] = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate JSON key in checkpoint: {key}")
            output[key] = value
        return output

    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON constant in checkpoint: {value}")

    return json.loads(
        text, object_pairs_hook=reject_pairs, parse_constant=reject_constant
    )


CandidateFace = tuple[int, int, int, int, int]
CandidateSupport = tuple[CandidateFace, ...]
CandidateRotation = tuple[tuple[int, int, int], tuple[int, int, int]]
_CANDIDATE_ROOT: CandidateFace = (0, 0, 0, 0, 1)


def _candidate_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def _candidate_face(value: Any) -> CandidateFace:
    if (
        type(value) is not list
        or len(value) != 5
        or any(type(item) is not int for item in value)
    ):
        raise ProductionNotReady("candidate face must contain five exact integers")
    face = tuple(value)
    if not (0 <= face[3] < face[4] <= 2):
        raise ProductionNotReady("candidate face axes are not canonical")
    return face  # type: ignore[return-value]


def _candidate_support(value: Any) -> CandidateSupport:
    if type(value) is not list:
        raise ProductionNotReady("candidate support must be a JSON list")
    support = tuple(sorted({_candidate_face(face) for face in value}))
    if len(support) != len(value) or _CANDIDATE_ROOT not in support:
        raise ProductionNotReady("candidate support is duplicate or omits the marked root")
    return support


@lru_cache(maxsize=1)
def load_o4_triality_candidate_manifest() -> Mapping[str, Any]:
    """Strictly decode the sealed, necessary-not-sufficient Stage0 closure."""
    if not __debug__:
        raise ProductionNotReady("optimized Python (-O) is forbidden for candidate gates")
    try:
        encoded = base64.b85decode(O4_TRIALITY_CANDIDATE_MANIFEST_B85.encode("ascii"))
        raw = gzip.decompress(encoded)
    except (ValueError, OSError) as error:
        raise ProductionNotReady("embedded candidate manifest cannot be decoded") from error
    if hashlib.sha256(raw).hexdigest() != O4_TRIALITY_CANDIDATE_MANIFEST_STABLE_SHA256:
        raise ProductionNotReady("embedded candidate manifest bytes changed")
    manifest = _strict_json_loads(raw.decode("utf-8"))
    exact_keys = {
        "all_candidate_maximal_support_count", "ancestry_sha256", "authority",
        "canonical_size_histogram", "canonical_support_count", "completeness",
        "concrete_decorated_support_count", "concrete_decorated_supports_sha256",
        "concrete_downward_closure_count", "concrete_downward_closure_sha256",
        "concrete_proper_incidence_count", "concrete_proper_incidence_sha256",
        "concrete_size_histogram", "concrete_supports", "counts",
        "embedding_multiplicity_histogram", "manifest_sha256",
        "maximal_candidate_supports", "necessary_not_sufficient", "schema", "supports",
    }
    if type(manifest) is not dict or set(manifest) != exact_keys:
        raise ProductionNotReady("candidate manifest top-level schema changed")
    if (
        manifest["schema"] != "HODGE-SU3-O4-TRIALITY-CANDIDATE-CLOSURE-v1"
        or manifest["necessary_not_sufficient"] is not True
        or manifest["manifest_sha256"] != O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
    ):
        raise ProductionNotReady("candidate manifest identity/scope changed")
    identity_payload = dict(manifest)
    identity_payload.pop("manifest_sha256")
    if hashlib.sha256(_candidate_json_bytes(identity_payload)).hexdigest() != (
        O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
    ):
        raise ProductionNotReady("candidate manifest identity is not reproducible")
    authority = manifest["authority"]
    if authority != {
        "pruning_filter": "corrected Stage0 link-triality only; no Stage1 or amplitudes",
        "stage0_ordered_artifact_sha256": (
            "40138139dfdffdf052e2711862f16548f24bba3da5a995444cbfee0dd18c8ca1"
        ),
        "stage0_source_sha256": (
            "914f5a36f6e66b74275e9cc7cc25a16201b263f008fd4f76ee4746bfcc10a655"
        ),
    }:
        raise ProductionNotReady("candidate manifest authority changed")
    expected_counts = {
        "words": 4221,
        "stage0_published_sign_histories": 33738,
        "stage0_invalid_published_sign_histories": 68,
        "stage0_missing_recomputed_sign_histories": 32,
        "corrected_triality_sign_histories": 33702,
        "corrected_c_orbits": 16851,
        "concrete_signed_histories": 264822,
        "signed_history_symmetry_orbits": 33111,
        "resolved_prefix_p_returns": 161574,
    }
    if any(manifest["counts"].get(key) != value for key, value in expected_counts.items()):
        raise ProductionNotReady("candidate manifest triality/history census changed")
    completeness = manifest["completeness"]
    if (
        completeness.get("ambiguous_prefix_cut_count") != 0
        or completeness.get("resolved_cut_adds_new_face_count") != 0
        or completeness.get("physical_amplitudes_or_stage1_filters_used") is not False
        or completeness.get("closure_before_link_connectivity_filter") is not True
        or completeness.get("quotient_after_concrete_downward_closure") is not True
        or completeness.get("candidate_formula_upper_bound") != 9
        or completeness.get("observed_exhaustive_maximum") != 6
        or completeness.get("rooted_rotation_sign_transport_verified_per_history")
        is not True
        or completeness.get("triality_sign_masks_recomputed_after_canonical_geometry")
        is not True
    ):
        raise ProductionNotReady("candidate manifest completeness firewall changed")

    supports = tuple(_candidate_support(row) for row in manifest["concrete_supports"])
    expected_order = tuple(sorted(supports, key=lambda row: (len(row), row)))
    if (
        supports != expected_order
        or len(set(supports)) != 203
        or manifest["concrete_downward_closure_count"] != 203
    ):
        raise ProductionNotReady("candidate concrete closure is not the sealed 203 rows")
    specs = tuple(sorted(set(itertools.chain.from_iterable(supports))))
    patch = build_open_cubic_patch((face[:3], face[3], face[4]) for face in specs)
    face_id = {(*face.anchor, *face.axes): face.face_id for face in patch.faces}
    id_supports = tuple(
        frozenset(face_id[face] for face in support) for support in supports
    )
    root_id = face_id[_CANDIDATE_ROOT]
    if any(
        not connected_in_adjacency(support, patch.adjacency) or root_id not in support
        for support in id_supports
    ):
        raise ProductionNotReady("candidate closure contains a non-rooted/non-link support")
    histogram = dict(sorted(Counter(map(len, supports)).items()))
    if histogram != {1: 1, 2: 12, 3: 158, 4: 20, 5: 10, 6: 2}:
        raise ProductionNotReady("candidate concrete size histogram changed")
    closure_digest = hashlib.sha256()
    for support in supports:
        encoded_support = _candidate_json_bytes([list(face) for face in support])
        closure_digest.update(len(encoded_support).to_bytes(8, "big"))
        closure_digest.update(encoded_support)
    if closure_digest.hexdigest() != manifest["concrete_downward_closure_sha256"]:
        raise ProductionNotReady("candidate concrete closure digest changed")

    incidence_digest = hashlib.sha256()
    incidence_count = 0
    for parent in supports:
        parent_set = frozenset(parent)
        for child in supports:
            if frozenset(child) < parent_set:
                encoded_edge = _candidate_json_bytes({
                    "parent": [list(face) for face in parent],
                    "child": [list(face) for face in child],
                })
                incidence_digest.update(len(encoded_edge).to_bytes(8, "big"))
                incidence_digest.update(encoded_edge)
                incidence_count += 1
    if (
        incidence_count != 724
        or manifest["concrete_proper_incidence_count"] != 724
        or incidence_digest.hexdigest()
        != "6d8729df01236c447b2863973f4de5caa9725d8fc871cfcd95deb2d752bdc4d4"
        or incidence_digest.hexdigest() != manifest["concrete_proper_incidence_sha256"]
    ):
        raise ProductionNotReady("candidate concrete Möbius incidence changed")
    for parent in id_supports:
        expected_subsets = set(rooted_connected_subsets_of(
            parent,
            root_id,
            lambda subset: connected_in_adjacency(subset, patch.adjacency),
        ))
        if not expected_subsets.issubset(set(id_supports)):
            raise ProductionNotReady("candidate closure is not literally downward closed")

    maximal = manifest["maximal_candidate_supports"]
    if (
        type(maximal) is not list
        or len(maximal) != 1107
        or sum(row.get("signed_history_count", 0) for row in maximal) != 264822
    ):
        raise ProductionNotReady("maximal-support history multiplicities changed")
    audit_images: set[CandidateSupport] = set()
    for row in manifest["supports"]:
        if set(row) != {
            "embedding_multiplicity", "images", "size", "stabilizer_size", "support"
        }:
            raise ProductionNotReady("candidate orbit-audit schema changed")
        images = tuple(_candidate_support(image) for image in row["images"])
        if (
            row["embedding_multiplicity"] != len(images)
            or row["stabilizer_size"] * len(images) != 8
        ):
            raise ProductionNotReady("candidate orbit/stabilizer census changed")
        audit_images.update(images)
    if audit_images != set(supports):
        raise ProductionNotReady("candidate orbit audit does not cover the concrete closure")
    return MappingProxyType(manifest)


def _candidate_permutation_parity(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def _candidate_proper_rotations() -> tuple[CandidateRotation, ...]:
    rotations = tuple(
        (permutation, signs)
        for permutation in itertools.permutations(range(3))
        for signs in itertools.product((-1, 1), repeat=3)
        if _candidate_permutation_parity(permutation)
        * signs[0] * signs[1] * signs[2] == 1
    )
    if len(rotations) != 24 or len(set(rotations)) != 24:
        raise AssertionError("proper cubic rotation construction failed")
    return rotations


def _candidate_compose_rotations(
    first: CandidateRotation, second: CandidateRotation
) -> CandidateRotation:
    """Return ``second after first`` in the source-axis convention."""
    first_permutation, first_signs = first
    second_permutation, second_signs = second
    return (
        tuple(second_permutation[first_permutation[axis]] for axis in range(3)),
        tuple(
            first_signs[axis] * second_signs[first_permutation[axis]]
            for axis in range(3)
        ),
    )  # type: ignore[return-value]


def _validate_candidate_rotation_group(probes: Iterable[CandidateFace]) -> None:
    rotations = _candidate_proper_rotations()
    rotation_set = set(rotations)
    identity: CandidateRotation = ((0, 1, 2), (1, 1, 1))
    if identity not in rotation_set:
        raise ProductionNotReady("proper cubic group omits identity")
    for rotation in rotations:
        inverses = tuple(
            candidate for candidate in rotations
            if _candidate_compose_rotations(rotation, candidate) == identity
            and _candidate_compose_rotations(candidate, rotation) == identity
        )
        if len(inverses) != 1:
            raise ProductionNotReady("proper cubic rotation has no unique inverse")
    exact_probes = tuple(sorted(set(probes)))
    for first in rotations:
        for second in rotations:
            composed = _candidate_compose_rotations(first, second)
            if composed not in rotation_set:
                raise ProductionNotReady("proper cubic rotations are not closed")
            for face in exact_probes:
                sequential = _candidate_transform_face_raw(
                    _candidate_transform_face_raw(face, first), second
                )
                direct = _candidate_transform_face_raw(face, composed)
                if sequential != direct:
                    raise ProductionNotReady("proper cubic raw action failed exact composition")
    stabilizer = tuple(
        rotation for rotation in rotations
        if _candidate_rooted_transform_face(_CANDIDATE_ROOT, rotation)
        == _CANDIDATE_ROOT
    )
    if len(stabilizer) != 8:
        raise ProductionNotReady("marked xy root stabilizer is not exact order eight")
    for first in stabilizer:
        for second in stabilizer:
            composed = _candidate_compose_rotations(first, second)
            if composed not in stabilizer:
                raise ProductionNotReady("marked-root stabilizer is not closed")
            for face in exact_probes:
                sequential = _candidate_rooted_transform_face(
                    _candidate_rooted_transform_face(face, first), second
                )
                direct = _candidate_rooted_transform_face(face, composed)
                if sequential != direct:
                    raise ProductionNotReady("rooted stabilizer failed exact composition")


def _candidate_transform_face_raw(
    face: CandidateFace, rotation: CandidateRotation
) -> CandidateFace:
    permutation, signs = rotation
    anchor = [0, 0, 0]
    for source_axis in range(3):
        anchor[permutation[source_axis]] += signs[source_axis] * face[source_axis]
    first, second = face[3], face[4]
    if signs[first] < 0:
        anchor[permutation[first]] -= 1
    if signs[second] < 0:
        anchor[permutation[second]] -= 1
    axes = tuple(sorted((permutation[first], permutation[second])))
    return (anchor[0], anchor[1], anchor[2], axes[0], axes[1])


def _candidate_rooted_transform_face(
    face: CandidateFace, rotation: CandidateRotation
) -> CandidateFace:
    transformed = _candidate_transform_face_raw(face, rotation)
    transformed_root = _candidate_transform_face_raw(_CANDIDATE_ROOT, rotation)
    return (
        transformed[0] - transformed_root[0],
        transformed[1] - transformed_root[1],
        transformed[2] - transformed_root[2],
        transformed[3],
        transformed[4],
    )


def build_o4_triality_candidate_full_t1_coverage() -> tuple[
    OpenCubicPatch,
    Mapping[int, int],
    Mapping[int, EmbeddingCoverageCertificate],
    Mapping[str, Any],
]:
    """Rotate the sealed 203-row xy closure into three literal T1 sweeps."""
    manifest = load_o4_triality_candidate_manifest()
    base_supports = tuple(
        _candidate_support(row) for row in manifest["concrete_supports"]
    )
    _validate_candidate_rotation_group(itertools.chain.from_iterable(base_supports))
    rotations = _candidate_proper_rotations()
    rotation_by_pol: dict[int, CandidateRotation] = {}
    supports_by_pol_spec: dict[int, tuple[CandidateSupport, ...]] = {}
    for pol, plane in enumerate(T1_POLARIZATION_PLANES):
        candidates = tuple(
            rotation for rotation in rotations
            if _candidate_rooted_transform_face(_CANDIDATE_ROOT, rotation)[3:] == plane
        )
        if len(candidates) != 8:
            raise ProductionNotReady("T1 plane does not have eight cubic root rotations")
        coset_images = {
            tuple(sorted({
                tuple(sorted(
                    _candidate_rooted_transform_face(face, candidate)
                    for face in support
                ))
                for support in base_supports
            }, key=lambda row: (len(row), row)))
            for candidate in candidates
        }
        if len(coset_images) != 1:
            raise ProductionNotReady(
                "rotations to one T1 plane disagree on the concrete candidate closure"
            )
        rotation = min(candidates)
        rotation_by_pol[pol] = rotation
        rotated = tuple(sorted({
            tuple(sorted(
                _candidate_rooted_transform_face(face, rotation) for face in support
            ))
            for support in base_supports
        }, key=lambda row: (len(row), row)))
        if len(rotated) != 203 or Counter(map(len, rotated)) != Counter(map(len, base_supports)):
            raise ProductionNotReady("rotated T1 candidate closure changed count/histogram")
        supports_by_pol_spec[pol] = rotated
    all_specs = tuple(sorted(set(itertools.chain.from_iterable(
        itertools.chain.from_iterable(supports_by_pol_spec.values())
    ))))
    patch = build_open_cubic_patch((face[:3], face[3], face[4]) for face in all_specs)
    ids = {(*face.anchor, *face.axes): face.face_id for face in patch.faces}
    roots = MappingProxyType({
        pol: ids[(0, 0, 0, *plane)]
        for pol, plane in enumerate(T1_POLARIZATION_PLANES)
    })
    coverages: dict[int, EmbeddingCoverageCertificate] = {}
    per_pol_digest: dict[str, str] = {}
    for pol in range(3):
        supports = tuple(
            frozenset(ids[face] for face in support)
            for support in supports_by_pol_spec[pol]
        )
        root = roots[pol]
        if any(
            root not in support
            or not connected_in_adjacency(support, patch.adjacency)
            for support in supports
        ):
            raise ProductionNotReady("rotated T1 closure is not rooted/link-connected")
        incidence_count = sum(
            child < parent for parent in supports for child in supports
        )
        if incidence_count != 724:
            raise ProductionNotReady("rotated T1 closure changed literal incidence")
        digest = hashlib.sha256()
        for support in supports_by_pol_spec[pol]:
            encoded = _candidate_json_bytes([list(face) for face in support])
            digest.update(len(encoded).to_bytes(8, "big"))
            digest.update(encoded)
        per_pol_digest[str(pol)] = digest.hexdigest()
        embeddings = tuple(
            RootedEmbedding(
                tuple((face, face) for face in sorted(support)), root, root, 1
            )
            for support in supports
        )
        coverage = EmbeddingCoverageCertificate(
            embeddings,
            O4_TRIALITY_CANDIDATE_MAX_FACES,
            complete=True,
            physical=True,
            authority_sha256=O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            _mechanical_witness=_COVERAGE_VERIFICATION_TOKEN,
        )
        for embedding in coverage.embeddings:
            embedding.validate_on_patch(patch)
        coverages[pol] = coverage
    certificate_payload = {
        "schema": "HODGE-SU3-O4-TRIALITY-CANDIDATE-FULL-T1-v1",
        "necessary_not_sufficient": True,
        "manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "base_concrete_support_count": 203,
        "physical_cluster_evaluation_count": 609,
        "proper_incidence_per_polarization": 724,
        "per_polarization_support_sha256": per_pol_digest,
        "rotations": {
            str(pol): [list(rotation_by_pol[pol][0]), list(rotation_by_pol[pol][1])]
            for pol in range(3)
        },
        "physics_contractions_run": 0,
    }
    certificate_payload["certificate_sha256"] = hashlib.sha256(
        _candidate_json_bytes(certificate_payload)
    ).hexdigest()
    if (
        certificate_payload["certificate_sha256"]
        != O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256
    ):
        raise ProductionNotReady("full-T1 candidate coverage certificate changed")
    return patch, roots, MappingProxyType(coverages), MappingProxyType(certificate_payload)


def _fraction_from_token(token: Any) -> Fraction:
    if type(token) is not str or token.count("/") != 1:
        raise ValueError("checkpoint exact values must be numerator/denominator strings")
    numerator_text, denominator_text = token.split("/", 1)
    if not numerator_text or not denominator_text:
        raise ValueError("malformed exact Fraction checkpoint token")
    try:
        numerator, denominator = int(numerator_text), int(denominator_text)
    except ValueError as error:
        raise ValueError("malformed exact Fraction checkpoint token") from error
    if denominator <= 0:
        raise ValueError("checkpoint Fraction denominator must be positive")
    value = Fraction(numerator, denominator)
    if f"{value.numerator}/{value.denominator}" != token:
        raise ValueError("checkpoint Fraction token is not canonical")
    return value


class Phase3SQLiteCheckpoint:
    """Transactional exact resume store authenticated by a user-derived key."""

    SCHEMA = "HODGE-SU3-PHASE3-AUTHENTICATED-SQLITE-v3"

    def __init__(
        self,
        path: str | Path,
        *,
        configuration_sha256: str,
        runtime_sha256: str,
        authentication: ResumeAuthentication,
    ) -> None:
        self.path = Path(path)
        if (
            type(configuration_sha256) is not str
            or configuration_sha256 != configuration_sha256.lower()
            or type(runtime_sha256) is not str
            or runtime_sha256 != runtime_sha256.lower()
        ):
            raise ValueError("checkpoint bindings must be exact lowercase SHA256 text")
        self.configuration_sha256 = configuration_sha256
        self.runtime_sha256 = runtime_sha256
        if not isinstance(authentication, ResumeAuthentication):
            raise ProductionNotReady("checkpoint requires user-secret resume authentication")
        self.authentication = authentication
        self._authentication_key = authentication.key
        for name, digest in (
            ("configuration", self.configuration_sha256),
            ("runtime", self.runtime_sha256),
        ):
            if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
                raise ValueError(f"checkpoint {name} binding is not SHA256")
        expected_context = resume_authentication_context_sha256(self.runtime_sha256)
        if authentication.authentication_context_sha256 != expected_context:
            raise ProductionNotReady(
                "resume authentication is bound to another script/geometry authority"
            )
        self._immutable_meta = {
            "schema": self.SCHEMA,
            "configuration_sha256": self.configuration_sha256,
            "runtime_script_sha256": self.runtime_sha256,
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "authentication_context_sha256": authentication.authentication_context_sha256,
            "resume_salt_hex": authentication.resume_salt_hex,
            "resume_run_id": authentication.resume_run_id,
        }
        self._header_verifier = _resume_hmac_sha256(
            self._authentication_key,
            "checkpoint-header-verifier",
            self._immutable_meta,
        )
        existed = self.path.exists()
        if existed:
            if not self.path.is_file():
                raise ProductionNotReady("checkpoint path exists but is not a regular file")
            # Wrong keys, old schemas, corrupt rows, and copied databases are rejected
            # through a genuinely read-only SQLite handle before any writable handle,
            # journal PRAGMA, CREATE, or metadata update is attempted.
            wal_path = self.path.with_name(self.path.name + "-wal")
            shm_path = self.path.with_name(self.path.name + "-shm")
            if wal_path.exists() or shm_path.exists():
                raise ProductionNotReady(
                    "authenticated DELETE-journal checkpoint has forbidden WAL/SHM sidecars"
                )
            journal_path = self.path.with_name(self.path.name + "-journal")
            if journal_path.exists():
                journal_info = os.lstat(journal_path)
                if (
                    journal_path.is_symlink()
                    or not stat.S_ISREG(journal_info.st_mode)
                    or journal_info.st_nlink != 1
                    or journal_info.st_dev != os.stat(self.path.parent).st_dev
                    or journal_info.st_size > (512 << 20)
                ):
                    raise ProductionNotReady("checkpoint rollback journal is not a regular file")
                original_db_sha = hashlib.sha256(self.path.read_bytes()).hexdigest()
                original_journal_sha = hashlib.sha256(journal_path.read_bytes()).hexdigest()
                # Recover only a private copy first. SQLite may mutate/remove the
                # copied rollback journal, while wrong secrets and forged rows leave
                # the original database and its journal byte-for-byte untouched.
                with tempfile.TemporaryDirectory(prefix="hodge-m4-auth-recovery-") as temp:
                    copied_path = Path(temp) / self.path.name
                    copied_journal = copied_path.with_name(copied_path.name + "-journal")
                    shutil.copyfile(self.path, copied_path)
                    shutil.copyfile(journal_path, copied_journal)
                    copied = sqlite3.connect(str(copied_path), timeout=60.0)
                    self.connection = copied
                    try:
                        self._validate_existing_database()
                    finally:
                        copied.close()
                if (
                    hashlib.sha256(self.path.read_bytes()).hexdigest() != original_db_sha
                    or not journal_path.is_file()
                    or hashlib.sha256(journal_path.read_bytes()).hexdigest()
                    != original_journal_sha
                ):
                    raise ProductionNotReady(
                        "checkpoint changed during authenticated rollback recovery"
                    )
                # The recovered copy authenticated the exact original DB+journal
                # byte pair. It is now safe to let SQLite recover the original,
                # immediately followed by the same exact HMAC/schema validation.
                self.connection = sqlite3.connect(str(self.path), timeout=60.0)
                try:
                    self._validate_existing_database()
                except BaseException:
                    self.connection.close()
                    raise
            else:
                read_only_uri = self.path.resolve().as_uri() + "?mode=ro"
                read_only = sqlite3.connect(read_only_uri, uri=True, timeout=60.0)
                self.connection = read_only
                try:
                    self._validate_existing_database()
                finally:
                    read_only.close()
                self.connection = sqlite3.connect(str(self.path), timeout=60.0)
                try:
                    self.connection.execute("PRAGMA query_only=ON")
                    self._validate_existing_database()
                    self.connection.execute("PRAGMA query_only=OFF")
                except BaseException:
                    self.connection.close()
                    raise
        else:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            try:
                descriptor = os.open(
                    self.path,
                    os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                    0o600,
                )
            except FileExistsError as error:
                raise ProductionNotReady(
                    "checkpoint appeared during initialization; choose a new versioned path"
                ) from error
            else:
                os.close(descriptor)
            self.connection = sqlite3.connect(str(self.path), timeout=60.0)
        journal_mode = str(
            self.connection.execute("PRAGMA journal_mode=DELETE").fetchone()[0]
        ).lower()
        if journal_mode != "delete":
            self.connection.close()
            raise ProductionNotReady(
                "checkpoint filesystem cannot provide SQLite DELETE journaling"
            )
        self.connection.execute("PRAGMA synchronous=FULL")
        if not existed:
            self.connection.execute(
                "CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
            )
            self.connection.execute(
                """CREATE TABLE cluster_results (
                       input_pol INTEGER NOT NULL,
                       support_json TEXT NOT NULL,
                       gap_json TEXT NOT NULL,
                       endpoint_certificate_sha256 TEXT NOT NULL,
                       record_hmac_sha256 TEXT NOT NULL,
                       PRIMARY KEY (input_pol, support_json)
                   )"""
            )
            expected_meta = {
                **self._immutable_meta,
                "key_verifier_hmac_sha256": self._header_verifier,
                "final_manifest_row_count": "0",
                "final_manifest_sha256": "",
                "final_manifest_hmac_sha256": "",
            }
            self.connection.executemany(
                "INSERT INTO meta(key,value) VALUES(?,?)", expected_meta.items()
            )
            self.connection.commit()

    @property
    def _expected_meta_keys(self) -> set[str]:
        return set(self._immutable_meta) | {
            "key_verifier_hmac_sha256",
            "final_manifest_row_count",
            "final_manifest_sha256",
            "final_manifest_hmac_sha256",
        }

    def _validate_existing_database(self) -> None:
        integrity = self.connection.execute("PRAGMA integrity_check(1)").fetchone()
        if integrity != ("ok",):
            raise ProductionNotReady("checkpoint SQLite integrity check failed")
        schema_objects = tuple(
            (
                object_type,
                name,
                table_name,
                None if sql is None else " ".join(str(sql).split()),
            )
            for object_type, name, table_name, sql in self.connection.execute(
                """SELECT type,name,tbl_name
                            ,sql FROM sqlite_master
                    WHERE type IN ('table','index','view','trigger')
                    ORDER BY type,name"""
            )
        )
        if schema_objects != (
            ("index", "sqlite_autoindex_cluster_results_1", "cluster_results", None),
            ("index", "sqlite_autoindex_meta_1", "meta", None),
            (
                "table", "cluster_results", "cluster_results",
                "CREATE TABLE cluster_results ( input_pol INTEGER NOT NULL, "
                "support_json TEXT NOT NULL, gap_json TEXT NOT NULL, "
                "endpoint_certificate_sha256 TEXT NOT NULL, "
                "record_hmac_sha256 TEXT NOT NULL, "
                "PRIMARY KEY (input_pol, support_json) )",
            ),
            (
                "table", "meta", "meta",
                "CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)",
            ),
        ):
            raise ProductionNotReady("checkpoint authenticated table schema changed")
        meta_columns = tuple(
            (row[1], str(row[2]).upper(), row[3], row[5])
            for row in self.connection.execute("PRAGMA table_info(meta)")
        )
        row_columns = tuple(
            (row[1], str(row[2]).upper(), row[3], row[5])
            for row in self.connection.execute("PRAGMA table_info(cluster_results)")
        )
        if meta_columns != (
            ("key", "TEXT", 0, 1),
            ("value", "TEXT", 1, 0),
        ) or row_columns != (
            ("input_pol", "INTEGER", 1, 1),
            ("support_json", "TEXT", 1, 2),
            ("gap_json", "TEXT", 1, 0),
            ("endpoint_certificate_sha256", "TEXT", 1, 0),
            ("record_hmac_sha256", "TEXT", 1, 0),
        ):
            raise ProductionNotReady("checkpoint authenticated column schema changed")
        metadata_rows = tuple(self.connection.execute("SELECT key,value FROM meta"))
        if any(type(key) is not str or type(value) is not str for key, value in metadata_rows):
            raise ProductionNotReady("checkpoint metadata contains non-text values")
        existing = dict(metadata_rows)
        if len(existing) != len(metadata_rows) or set(existing) != self._expected_meta_keys:
            raise ProductionNotReady("checkpoint authenticated metadata schema changed")
        if any(existing[key] != value for key, value in self._immutable_meta.items()):
            raise ProductionNotReady(
                "checkpoint metadata does not match this script/configuration/run"
            )
        if not hmac.compare_digest(
            existing["key_verifier_hmac_sha256"], self._header_verifier
        ):
            raise ProductionNotReady(
                "checkpoint recovery secret is wrong or authenticated header was forged; "
                "use the saved secret or choose a new versioned checkpoint path"
            )
        final_values = (
            existing["final_manifest_row_count"],
            existing["final_manifest_sha256"],
            existing["final_manifest_hmac_sha256"],
        )
        if final_values != ("0", "", "") and (
            final_values[0] != "609"
            or any(
                type(token) is not str
                or len(token) != 64
                or any(ch not in "0123456789abcdef" for ch in token)
                for token in final_values[1:]
            )
        ):
            raise ProductionNotReady("checkpoint final manifest metadata is malformed")
        rows = self._validated_rows()
        if len(rows) > 609:
            raise ProductionNotReady("checkpoint contains more than 609 authenticated rows")
        if final_values != ("0", "", ""):
            if len(rows) != 609:
                raise ProductionNotReady("checkpoint final manifest claims an incomplete row set")
            payload = self._manifest_payload_from_rows(rows)
            observed_sha = hashlib.sha256(_auth_canonical_bytes(payload)).hexdigest()
            observed_hmac = _resume_hmac_sha256(
                self._authentication_key, "final-row-manifest", payload
            )
            if (
                final_values[1] != observed_sha
                or not hmac.compare_digest(final_values[2], observed_hmac)
            ):
                raise ProductionNotReady("checkpoint final row manifest authentication failed")

    @staticmethod
    def support_json(support: Iterable[int]) -> str:
        values = tuple(support)
        if (
            not values
            or any(type(value) is not int or value < 0 for value in values)
            or len(values) != len(set(values))
        ):
            raise ValueError(
                "checkpoint support needs distinct exact nonnegative face integers"
            )
        return json.dumps(sorted(values), separators=(",", ":"))

    def _record_payload(
        self,
        input_pol: int,
        support_json: str,
        gap_json: str,
        endpoint_certificate_sha256: str,
    ) -> Mapping[str, Any]:
        if type(input_pol) is not int or input_pol not in (0, 1, 2):
            raise ValueError("checkpoint input polarization must be exact 0, 1, or 2")
        if type(support_json) is not str or type(gap_json) is not str:
            raise ValueError("checkpoint record JSON fields must be exact text")
        self._validate_support_json(support_json)
        if (
            type(endpoint_certificate_sha256) is not str
            or endpoint_certificate_sha256 != endpoint_certificate_sha256.lower()
            or len(endpoint_certificate_sha256) != 64
            or any(ch not in "0123456789abcdef" for ch in endpoint_certificate_sha256)
        ):
            raise ValueError("checkpoint endpoint certificate must be lowercase SHA256")
        return {
            "schema": self.SCHEMA,
            "resume_run_id": self.authentication.resume_run_id,
            "authentication_context_sha256": (
                self.authentication.authentication_context_sha256
            ),
            "configuration_sha256": self.configuration_sha256,
            "runtime_script_sha256": self.runtime_sha256,
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "input_pol": input_pol,
            "support_json": support_json,
            "gap_json": gap_json,
            "endpoint_certificate_sha256": endpoint_certificate_sha256,
        }

    def _record_hmac_sha256(
        self,
        input_pol: int,
        support_json: str,
        gap_json: str,
        endpoint_certificate_sha256: str,
    ) -> str:
        return _resume_hmac_sha256(
            self._authentication_key,
            "cluster-result",
            self._record_payload(
                input_pol, support_json, gap_json, endpoint_certificate_sha256
            ),
        )

    @staticmethod
    def _validate_support_json(support_json: str) -> tuple[int, ...]:
        decoded = _strict_json_loads(support_json)
        if (
            type(decoded) is not list
            or not decoded
            or any(type(value) is not int or value < 0 for value in decoded)
            or decoded != sorted(set(decoded))
            or json.dumps(decoded, separators=(",", ":")) != support_json
        ):
            raise ProductionNotReady("checkpoint support JSON is not canonical")
        return tuple(decoded)

    def _validate_stored_row(
        self,
        input_pol: Any,
        support_json: Any,
        gap_json: Any,
        endpoint_certificate_sha256: Any,
        record_hmac_sha256: Any,
    ) -> tuple[
        int,
        str,
        tuple[tuple[Fraction, Fraction, Fraction], ...],
        str,
        str,
    ]:
        if type(input_pol) is not int or input_pol not in (0, 1, 2):
            raise ProductionNotReady("checkpoint row has invalid input polarization")
        if (
            type(support_json) is not str
            or type(gap_json) is not str
            or type(endpoint_certificate_sha256) is not str
            or type(record_hmac_sha256) is not str
        ):
            raise ProductionNotReady("checkpoint row fields have non-canonical SQLite types")
        support_text = support_json
        self._validate_support_json(support_text)
        gap_text = gap_json
        certificate_sha = endpoint_certificate_sha256
        observed_hmac = record_hmac_sha256
        if certificate_sha != certificate_sha.lower() or observed_hmac != observed_hmac.lower():
            raise ProductionNotReady("checkpoint row digests are not canonical lowercase")
        expected_hmac = self._record_hmac_sha256(
            input_pol, support_text, gap_text, certificate_sha
        )
        if not hmac.compare_digest(observed_hmac, expected_hmac):
            raise ProductionNotReady(
                "checkpoint cluster record failed user-secret HMAC authentication"
            )
        decoded = _strict_json_loads(gap_text)
        if (
            type(decoded) is not list
            or len(decoded) != 4
            or any(
                type(row_values) is not list or len(row_values) != 3
                for row_values in decoded
            )
        ):
            raise ProductionNotReady("checkpoint gap row schema is invalid")
        exact = tuple(
            tuple(_fraction_from_token(value) for value in row_values)
            for row_values in decoded
        )
        if len(certificate_sha) != 64 or any(
            ch not in "0123456789abcdef" for ch in certificate_sha
        ):
            raise ProductionNotReady("checkpoint endpoint certificate SHA256 is invalid")
        if len(observed_hmac) != 64 or any(
            ch not in "0123456789abcdef" for ch in observed_hmac
        ):
            raise ProductionNotReady("checkpoint row HMAC is malformed")
        return input_pol, support_text, exact, certificate_sha, observed_hmac

    def get(
        self,
        input_pol: int,
        support: Iterable[int],
    ) -> tuple[tuple[tuple[Fraction, Fraction, Fraction], ...], str] | None:
        if type(input_pol) is not int or input_pol not in (0, 1, 2):
            raise ValueError("checkpoint input polarization must be exact 0, 1, or 2")
        support_json = self.support_json(support)
        row = self.connection.execute(
            """SELECT input_pol,support_json,gap_json,
                      endpoint_certificate_sha256,record_hmac_sha256
                 FROM cluster_results WHERE input_pol=? AND support_json=?""",
            (input_pol, support_json),
        ).fetchone()
        if row is None:
            return None
        _, observed_support, exact, certificate_sha, _ = self._validate_stored_row(*row)
        if observed_support != support_json:
            raise ProductionNotReady("checkpoint lookup returned a different support")
        return exact, certificate_sha  # type: ignore[return-value]

    def put(
        self,
        input_pol: int,
        support: Iterable[int],
        gap_rows: Sequence[Sequence[Any]],
        endpoint_certificate_sha256: str,
    ) -> None:
        if (
            type(input_pol) is not int
            or input_pol not in (0, 1, 2)
            or type(gap_rows) not in (list, tuple)
            or len(gap_rows) != 4
            or any(type(row) not in (list, tuple) or len(row) != 3 for row in gap_rows)
        ):
            raise ValueError("checkpoint cluster result needs four full-T1 rows")
        support_json = self.support_json(support)
        exact_rows: list[list[Fraction]] = []
        for row in gap_rows:
            exact_row: list[Fraction] = []
            for value in row:
                if isinstance(value, bool) or isinstance(value, float):
                    raise ValueError("checkpoint exact gap values cannot be bool or float")
                exact_row.append(as_fraction(value))
            exact_rows.append(exact_row)
        gap_json = json.dumps(
            [[_json_exact(value) for value in row] for row in exact_rows],
            separators=(",", ":"),
            allow_nan=False,
        )
        if (
            type(endpoint_certificate_sha256) is not str
            or endpoint_certificate_sha256 != endpoint_certificate_sha256.lower()
            or len(endpoint_certificate_sha256) != 64
            or any(ch not in "0123456789abcdef" for ch in endpoint_certificate_sha256)
        ):
            raise ValueError("endpoint certificate must be exact lowercase SHA256")
        certificate_sha = endpoint_certificate_sha256
        record_hmac = self._record_hmac_sha256(
            input_pol, support_json, gap_json, certificate_sha
        )
        self._validate_stored_row(
            input_pol, support_json, gap_json, certificate_sha, record_hmac
        )
        existing = self.get(input_pol, support)
        if existing is not None:
            expected = (
                tuple(tuple(value for value in row) for row in exact_rows),
                certificate_sha,
            )
            if existing != expected:
                raise ProductionNotReady("checkpoint refuses a conflicting cluster result")
            return
        with self.connection:
            self.connection.executemany(
                "UPDATE meta SET value=? WHERE key=?",
                (
                    ("0", "final_manifest_row_count"),
                    ("", "final_manifest_sha256"),
                    ("", "final_manifest_hmac_sha256"),
                ),
            )
            self.connection.execute(
                """INSERT INTO cluster_results(
                       input_pol,support_json,gap_json,
                       endpoint_certificate_sha256,record_hmac_sha256
                   ) VALUES(?,?,?,?,?)""",
                (input_pol, support_json, gap_json, certificate_sha, record_hmac),
            )

    def _validated_rows(self) -> tuple[tuple[int, str, str, str, str], ...]:
        output: list[tuple[int, str, str, str, str]] = []
        rows = self.connection.execute(
            """SELECT input_pol,support_json,gap_json,
                      endpoint_certificate_sha256,record_hmac_sha256
                 FROM cluster_results ORDER BY input_pol,support_json"""
        )
        for row in rows:
            pol, support_text, _exact, certificate_sha, record_hmac = (
                self._validate_stored_row(*row)
            )
            output.append((pol, support_text, str(row[2]), certificate_sha, record_hmac))
        return tuple(output)

    def _manifest_payload_from_rows(
        self,
        rows: Sequence[tuple[int, str, str, str, str]],
    ) -> Mapping[str, Any]:
        entries = [
            {
                "input_pol": pol,
                "support_json": support_json,
                "record_hmac_sha256": record_hmac,
            }
            for pol, support_json, _gap, _certificate, record_hmac in rows
        ]
        return {
            "schema": "HODGE-SU3-AUTHENTICATED-ROW-MANIFEST-v1",
            "configuration_sha256": self.configuration_sha256,
            "runtime_script_sha256": self.runtime_sha256,
            "authentication_context_sha256": (
                self.authentication.authentication_context_sha256
            ),
            "resume_run_id": self.authentication.resume_run_id,
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "row_count": len(rows),
            "entries": entries,
        }

    def completed_keys(self) -> set[tuple[int, str]]:
        return {(pol, support_json) for pol, support_json, *_ in self._validated_rows()}

    def require_exact_keyset(self, expected: Iterable[tuple[int, FaceSupport]]) -> None:
        expected_rows = tuple(expected)
        if any(type(pol) is not int or pol not in (0, 1, 2) for pol, _ in expected_rows):
            raise ValueError("expected checkpoint keyset has invalid polarization")
        expected_keys = {(pol, self.support_json(support)) for pol, support in expected_rows}
        if len(expected_keys) != len(expected_rows):
            raise ValueError("expected checkpoint keyset contains duplicate rows")
        observed = self.completed_keys()
        if observed != expected_keys:
            raise ProductionNotReady(
                "checkpoint keyset is incomplete or contains records outside the sweep"
            )

    def finalize_authenticated_manifest(
        self,
        expected: Iterable[tuple[int, FaceSupport]],
        *,
        fresh_count: int,
        resumed_count: int,
    ) -> Mapping[str, Any]:
        if (
            type(fresh_count) is not int
            or type(resumed_count) is not int
            or fresh_count < 0
            or resumed_count < 0
            or fresh_count + resumed_count != 609
        ):
            raise ProductionNotReady("fresh/resumed authenticated census must total 609")
        expected_rows = tuple(expected)
        if any(type(pol) is not int or pol not in (0, 1, 2) for pol, _ in expected_rows):
            raise ValueError("expected authenticated manifest has invalid polarization")
        expected_keys = {(pol, self.support_json(support)) for pol, support in expected_rows}
        if len(expected_keys) != len(expected_rows):
            raise ValueError("expected authenticated manifest has duplicate keys")
        rows = self._validated_rows()
        observed_keys = {(pol, support_json) for pol, support_json, *_ in rows}
        if len(rows) != 609 or observed_keys != expected_keys:
            raise ProductionNotReady(
                "authenticated checkpoint manifest is not the exact 609-row sweep"
            )
        manifest_payload = self._manifest_payload_from_rows(rows)
        manifest_sha = hashlib.sha256(
            _auth_canonical_bytes(manifest_payload)
        ).hexdigest()
        manifest_hmac = _resume_hmac_sha256(
            self._authentication_key,
            "final-row-manifest",
            manifest_payload,
        )
        current_meta = dict(self.connection.execute("SELECT key,value FROM meta"))
        prior = (
            current_meta["final_manifest_row_count"],
            current_meta["final_manifest_sha256"],
            current_meta["final_manifest_hmac_sha256"],
        )
        expected_final = ("609", manifest_sha, manifest_hmac)
        if prior != ("0", "", "") and prior != expected_final:
            raise ProductionNotReady("stored authenticated final manifest conflicts")
        with self.connection:
            self.connection.executemany(
                "UPDATE meta SET value=? WHERE key=?",
                (
                    ("609", "final_manifest_row_count"),
                    (manifest_sha, "final_manifest_sha256"),
                    (manifest_hmac, "final_manifest_hmac_sha256"),
                ),
            )
        current_run_payload = {
            "schema": AUTHENTICATED_EXECUTION_ATTESTATION_SCHEMA,
            "configuration_sha256": self.configuration_sha256,
            "runtime_script_sha256": self.runtime_sha256,
            "authentication_context_sha256": (
                self.authentication.authentication_context_sha256
            ),
            "resume_run_id": self.authentication.resume_run_id,
            "invocation_nonce": self.authentication.invocation_nonce,
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "row_manifest_sha256": manifest_sha,
            "row_manifest_hmac_sha256": manifest_hmac,
            "fresh_cluster_evaluations": fresh_count,
            "resumed_cluster_evaluations": resumed_count,
        }
        current_run_sha = hashlib.sha256(
            _auth_canonical_bytes(current_run_payload)
        ).hexdigest()
        return MappingProxyType({
            **manifest_payload,
            "manifest_sha256": manifest_sha,
            "manifest_hmac_sha256": manifest_hmac,
            # Keep the execution-attestation names explicit.  The shorter
            # aliases above are retained only inside the authenticated
            # manifest schema; callers must never infer one name from the
            # other without this exact equality being serialized and gated.
            "row_manifest_sha256": manifest_sha,
            "row_manifest_hmac_sha256": manifest_hmac,
            "invocation_nonce": self.authentication.invocation_nonce,
            "fresh_cluster_evaluations": fresh_count,
            "resumed_cluster_evaluations": resumed_count,
            "current_run_sha256": current_run_sha,
            "current_run_hmac_sha256": _resume_hmac_sha256(
                self._authentication_key,
                "current-run-resume-summary",
                current_run_payload,
            ),
        })

    def certificate_hmac_sha256(self, payload: Mapping[str, Any]) -> str:
        return _resume_hmac_sha256(
            self._authentication_key,
            "final-construction-certificate",
            payload,
        )

    def close(self) -> None:
        self.connection.close()


class ExactEndpointMarkedVacuumAssembler:
    """Heavy user-run 609-row conservative-candidate full-T1 assembler."""

    def __init__(
        self,
        builder: ExactFaceInsertionBuilder,
        roots_by_pol: Mapping[int, int],
        coverages: Mapping[int, EmbeddingCoverageCertificate],
        *,
        max_faces: int = O4_TRIALITY_CANDIDATE_MAX_FACES,
        journal: Phase2CheckpointJournal | None = None,
        disk_checkpoint: Phase3SQLiteCheckpoint | None = None,
    ) -> None:
        self.builder = builder
        self.roots_by_pol = {int(pol): int(face) for pol, face in roots_by_pol.items()}
        self.coverages = dict(coverages)
        self.max_faces = int(max_faces)
        self.journal = journal or Phase2CheckpointJournal(retention_limit=1000)
        self.runtime_script_sha256 = runtime_script_sha256()
        self.disk_checkpoint = disk_checkpoint
        if set(self.roots_by_pol) != {0, 1, 2}:
            raise ValueError("Phase3 requires exactly one concrete root for each T1 polarization")
        if set(self.coverages) != {0, 1, 2}:
            raise ValueError("Phase3 requires one embedding certificate per T1 root")
        if self.max_faces != O4_TRIALITY_CANDIDATE_MAX_FACES:
            raise ProductionNotReady(
                "candidate coverage must match its observed six-face maximum"
            )
        for pol, root in self.roots_by_pol.items():
            if face_polarization(builder.patch, root) != pol:
                raise ValueError("root face does not match its declared T1 polarization")
            coverage = self.coverages[pol]
            if coverage.max_faces != self.max_faces:
                raise ValueError(
                    "embedding coverage maximum differs from its sealed candidate keyset"
                )
            if (
                len(coverage.embeddings) != 203
                or coverage.authority_sha256
                != O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
            ):
                raise ProductionNotReady(
                    "Phase3 requires the sealed 203-row candidate closure per T1 root"
                )
            if not (coverage.complete and coverage.physical and coverage.mechanically_verified):
                raise ProductionNotReady("Phase3 requires mechanical physical root coverage")
            if any(embedding.canonical_root != root for embedding in coverage.embeddings):
                raise ValueError("embedding certificate is bound to a different T1 root")
        self.configuration_sha256 = phase3_configuration_sha256(
            builder.patch, self.roots_by_pol, self.coverages, self.max_faces
        )
        if self.disk_checkpoint is not None and (
            self.disk_checkpoint.configuration_sha256 != self.configuration_sha256
            or self.disk_checkpoint.runtime_sha256 != self.runtime_script_sha256
        ):
            raise ProductionNotReady(
                "disk checkpoint is not bound to this exact Phase3 construction"
            )

    def evaluate(self) -> Phase3AssemblyResult:
        if self.disk_checkpoint is None:
            raise ProductionNotReady(
                "physical Phase3 requires a user-secret authenticated checkpoint"
            )
        raw: dict[tuple[int, int, int], dict[Support, Fraction]] = {
            (order, input_pol, output_pol): {}
            for order in range(1, 5)
            for input_pol in range(3)
            for output_pol in range(3)
        }
        endpoint_chain = "0" * 64
        fresh_count = 0
        resumed_count = 0
        cluster_supports: dict[int, tuple[Support, ...]] = {}
        for input_pol in range(3):
            root = self.roots_by_pol[input_pol]
            supports = tuple(
                embedding.canonical_support
                for embedding in self.coverages[input_pol].embeddings
            )
            if len(set(supports)) != len(supports):
                raise ProductionNotReady("physical coverage repeats a concrete rooted cluster")
            cluster_supports[input_pol] = supports
            started = time.monotonic()
            print(
                f"[PHASE3] T1 input polarization {input_pol}: "
                f"{len(supports):,} exact rooted clusters",
                flush=True,
            )
            heartbeat_stride = max(1, len(supports) // 100)
            for cluster_index, support in enumerate(supports, start=1):
                cluster = RootedOpenCluster(self.builder.patch, root, support)
                self.journal.heartbeat(
                    "phase3-cluster-start",
                    support=cluster.support,
                    detail={"input_pol": input_pol},
                )
                resumed = (
                    None
                    if self.disk_checkpoint is None
                    else self.disk_checkpoint.get(input_pol, cluster.support)
                )
                if resumed is None:
                    evaluation = None
                    try:
                        evaluation = evaluate_exact_endpoint_marked_vacuum_cluster(
                            self.builder, cluster
                        )
                        gap_rows = evaluation.gap_rows_by_order
                        endpoint_certificate_sha = (
                            evaluation.coverage.certificate_sha256
                        )
                        endpoint_ledger_sha = evaluation.coverage.ledger_sha256
                        pair_count = len(evaluation.coverage.audited_endpoint_pairs)
                        fold_path_count = len(evaluation.coverage.audited_fold_paths)
                        if self.disk_checkpoint is not None:
                            self.disk_checkpoint.put(
                                input_pol,
                                cluster.support,
                                gap_rows,
                                endpoint_certificate_sha,
                            )
                    finally:
                        evaluation = None
                        clear_exact_cluster_working_caches()
                    resumed_record = False
                    fresh_count += 1
                else:
                    gap_rows, endpoint_certificate_sha = resumed
                    endpoint_ledger_sha = None
                    pair_count = None
                    fold_path_count = None
                    resumed_record = True
                    resumed_count += 1
                endpoint_chain = hashlib.sha256(
                    (endpoint_chain + endpoint_certificate_sha).encode("ascii")
                ).hexdigest()
                for order, row in enumerate(gap_rows, start=1):
                    for output_pol, value in enumerate(row):
                        raw[(order, input_pol, output_pol)][cluster.support] = value
                self.journal.heartbeat(
                    "phase3-cluster-full-t1-complete",
                    support=cluster.support,
                    detail={
                        "input_pol": input_pol,
                        "endpoint_ledger_sha256": endpoint_ledger_sha,
                        "endpoint_certificate_sha256": endpoint_certificate_sha,
                        "pair_count": pair_count,
                        "fold_path_count": fold_path_count,
                        "resumed": resumed_record,
                        "audit_telemetry": (
                            "authenticated-stored-certificate-no-recomputation"
                            if resumed_record
                            else "fresh-exact-endpoint-audit"
                        ),
                    },
                )
                if (
                    cluster_index == 1
                    or cluster_index == len(supports)
                    or cluster_index % heartbeat_stride == 0
                ):
                    elapsed = max(time.monotonic() - started, 1e-9)
                    rate = cluster_index / elapsed
                    eta = (len(supports) - cluster_index) / max(rate, 1e-12)
                    eta_text = (
                        f"fresh-only-ETA~{eta:.1f}s"
                        if resumed_count == 0
                        else "ETA=withheld-for-fresh/resumed-mix"
                    )
                    print(
                        f"[PHASE3] pol={input_pol} {cluster_index:,}/{len(supports):,}; "
                        f"elapsed={elapsed:.1f}s {eta_text}; "
                        f"fresh={fresh_count} resumed={resumed_count}; "
                        f"endpoint_chain={endpoint_chain[:16]}",
                        flush=True,
                    )
        expected_checkpoint_rows = tuple(
            (pol, support)
            for pol, supports in cluster_supports.items()
            for support in supports
        )
        self.disk_checkpoint.require_exact_keyset(expected_checkpoint_rows)
        authenticated_resume_manifest = (
            self.disk_checkpoint.finalize_authenticated_manifest(
                expected_checkpoint_rows,
                fresh_count=fresh_count,
                resumed_count=resumed_count,
            )
        )
        mobius: dict[tuple[int, int, int], RootedRawMobiusResult] = {}
        gamma = [
            [[Fraction(0) for _output in range(3)] for _input in range(3)]
            for _order in range(4)
        ]
        for (order, input_pol, output_pol), ledger in raw.items():
            root = self.roots_by_pol[input_pol]
            reduced = rooted_mobius_from_raw(
                ledger,
                cluster_supports[input_pol],
                root,
                lambda support: connected_in_adjacency(
                    support, self.builder.patch.adjacency
                ),
            )
            mobius[(order, input_pol, output_pol)] = reduced
            gamma[order - 1][input_pol][output_pol] = embedding_sum(
                reduced.omega, self.coverages[input_pol]
            )
        gamma_exact = tuple(
            tuple(tuple(row) for row in matrix) for matrix in gamma
        )
        coefficients = tuple(
            _exact_gamma_scalar(matrix, f"order-{order}")
            for order, matrix in enumerate(gamma_exact, start=1)
        )
        if coefficients[:3] != LOWER_ORDER_GAP_REGRESSION:
            raise ExactEngineError(
                "independently generated lower-order gap ledgers failed the exact "
                f"regression: got={coefficients[:3]!r}"
            )
        self.journal.heartbeat(
            "phase3-full-t1-mobius-complete",
            detail={
                "endpoint_certificate_sha256": endpoint_chain,
                "lower_coefficients": coefficients[:3],
                "m4": coefficients[3],
                "fresh_cluster_evaluations": fresh_count,
                "resumed_cluster_evaluations": resumed_count,
                "authenticated_row_manifest_sha256": (
                    authenticated_resume_manifest["manifest_sha256"]
                ),
                "authenticated_row_manifest_hmac_sha256": (
                    authenticated_resume_manifest["manifest_hmac_sha256"]
                ),
            },
        )
        if runtime_script_sha256() != self.runtime_script_sha256:
            raise ExactEngineError("runtime script bytes changed during the physical sweep")
        return Phase3AssemblyResult(
            MappingProxyType(mobius),
            gamma_exact,
            coefficients[:3],
            coefficients[3],
            MappingProxyType(self.coverages),
            endpoint_chain,
            self.runtime_script_sha256,
            authenticated_resume_manifest,
            self.journal.checkpoint(PHASE3_COMPLETED_STATUS),
            _ENDPOINT_PHYSICAL_TOKEN,
        )


def _atomic_json_write(destination: Path, payload: Mapping[str, Any]) -> None:
    encoded = _auth_canonical_bytes(dict(payload))
    _atomic_bytes_write(destination, encoded)


def _atomic_bytes_write(destination: Path, encoded: bytes) -> None:
    if type(encoded) is not bytes or not encoded:
        raise ValueError("atomic certificate/status write requires nonempty exact bytes")
    destination = Path(destination)
    if destination.exists() and destination.is_symlink():
        raise ProductionNotReady("refusing to replace a symlink destination")
    parent = destination.parent
    if not parent.is_dir():
        raise ProductionNotReady("atomic output parent directory does not exist")
    temporary = parent / (
        f".{destination.name}.hodge-tmp-{secrets.token_hex(16)}"
    )
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor: int | None = None
    try:
        descriptor = os.open(temporary, flags, 0o600)
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ProductionNotReady("atomic output temporary is not a private regular file")
        view = memoryview(encoded)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short atomic output write")
            view = view[written:]
        os.fsync(descriptor)
        if os.fstat(descriptor).st_nlink != 1:
            raise ProductionNotReady("atomic output temporary acquired another hard link")
        os.close(descriptor)
        descriptor = None
        os.replace(temporary, destination)
        if os.name == "posix":
            directory_fd = os.open(parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
            try:
                try:
                    os.fsync(directory_fd)
                except OSError as error:
                    unsupported = {
                        errno.EINVAL,
                        getattr(errno, "ENOTSUP", errno.EINVAL),
                        getattr(errno, "EOPNOTSUPP", errno.EINVAL),
                        getattr(errno, "ENOSYS", errno.EINVAL),
                    }
                    if error.errno not in unsupported:
                        raise
                    print(
                        "[DURABILITY] directory fsync unsupported; file fsync and "
                        "atomic replace completed",
                        flush=True,
                    )
            finally:
                os.close(directory_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if temporary.exists():
            try:
                temporary.unlink()
            except OSError:
                pass


def run_exact_phase3_physical(
    *,
    output_path: str | Path | None = None,
    checkpoint_path: str | Path | None = None,
    authorized_cluster_evaluations: int | None = None,
    authorized_candidate_certificate_sha256: str | None = None,
    resume_authentication: ResumeAuthentication | None = None,
) -> tuple[Phase3AssemblyResult, TargetBlindM4Seal]:
    """Explicit heavy entry point; never called by import, self-test, or notebook setup.

    The sealed 203-row concrete Stage0 triality-candidate closure is rotated
    independently to all three input polarizations (609 authenticated fresh-or-resumed
    evaluations, with exact counts reported separately).
    Exact marked/vacuum evaluation, literal concrete Möbius subtraction, and
    the target-blind seal follow in that order.  The geometry filter is only a
    conservative necessary condition; it contributes no amplitudes.
    """
    if not __debug__:
        raise ProductionNotReady("optimized Python (-O) is forbidden for physical gates")
    if (
        type(authorized_cluster_evaluations) is not int
        or authorized_cluster_evaluations != 609
    ):
        raise ProductionNotReady("the sealed candidate sweep contains exactly 609 clusters")
    if (
        type(authorized_candidate_certificate_sha256) is not str
        or authorized_candidate_certificate_sha256.lower()
        != O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256
    ):
        raise ProductionNotReady("the exact reviewed candidate certificate SHA256 is required")
    authentication = (
        load_resume_authentication_from_sealed_fd()
        if resume_authentication is None
        else resume_authentication
    )
    if not isinstance(authentication, ResumeAuthentication):
        raise ProductionNotReady("physical construction requires authenticated resume keying")
    destination = None if output_path is None else Path(output_path)
    if destination is None or checkpoint_path is None:
        raise ProductionNotReady(
            "physical construction requires persistent checkpoint and certificate paths"
        )
    checkpoint_destination = Path(checkpoint_path)
    if checkpoint_destination.is_symlink() or destination.is_symlink():
        raise ProductionNotReady("checkpoint/certificate symlink paths are forbidden")
    destination_lexical = os.path.normcase(os.path.abspath(destination))
    checkpoint_lexical = os.path.normcase(os.path.abspath(checkpoint_destination))
    if destination_lexical == checkpoint_lexical:
        raise ProductionNotReady("checkpoint and certificate paths must be distinct")
    destination_resolved = os.path.normcase(str(destination.resolve(strict=False)))
    checkpoint_resolved = os.path.normcase(
        str(checkpoint_destination.resolve(strict=False))
    )
    if destination_resolved == checkpoint_resolved or (
        destination.exists()
        and checkpoint_destination.exists()
        and os.path.samefile(destination, checkpoint_destination)
    ):
        raise ProductionNotReady("checkpoint and certificate resolve to the same file")
    starting_runtime_sha = runtime_script_sha256()
    if authentication.authentication_context_sha256 != (
        resume_authentication_context_sha256(starting_runtime_sha)
    ):
        raise ProductionNotReady("resume key is bound to another runtime/authority")
    checkpoint_store: Phase3SQLiteCheckpoint | None = None
    status_destination = destination.with_name(
        destination.name + f".status.{authentication.invocation_nonce}.json"
    )
    status_lexical = os.path.normcase(os.path.abspath(status_destination))
    if status_lexical in {destination_lexical, checkpoint_lexical}:
        raise ProductionNotReady("status path collides with checkpoint/certificate")
    status_resolved = os.path.normcase(str(status_destination.resolve(strict=False)))
    if status_resolved in {destination_resolved, checkpoint_resolved} or (
        status_destination.exists()
        and (
            (destination.exists() and os.path.samefile(status_destination, destination))
            or (
                checkpoint_destination.exists()
                and os.path.samefile(status_destination, checkpoint_destination)
            )
        )
    ):
        raise ProductionNotReady("status path resolves to checkpoint/certificate")
    if status_destination.is_symlink():
        raise ProductionNotReady("invocation status symlink path is forbidden")
    if destination is not None:
        _atomic_json_write(status_destination, {
            "schema": "HODGE-SU3-EXACT-MARKED-CLUSTER-M4-v3-AUTHENTICATED",
            "status": "RUNNING",
            "runtime_script_sha256": starting_runtime_sha,
            "invocation_nonce": authentication.invocation_nonce,
            "target_inputs": [],
        })
    try:
        patch, roots, coverages, candidate_certificate = (
            build_o4_triality_candidate_full_t1_coverage()
        )
        actual_cluster_evaluations = sum(
            len(coverage.embeddings) for coverage in coverages.values()
        )
        if actual_cluster_evaluations != 609:
            raise ProductionNotReady(
                "sealed triality-candidate cluster census changed: "
                f"actual={actual_cluster_evaluations}, required=609"
            )
        configuration_sha = phase3_configuration_sha256(
            patch, roots, coverages, O4_TRIALITY_CANDIDATE_MAX_FACES
        )
        if checkpoint_path is not None:
            checkpoint_store = Phase3SQLiteCheckpoint(
                checkpoint_path,
                configuration_sha256=configuration_sha,
                runtime_sha256=starting_runtime_sha,
                authentication=authentication,
            )
        result = ExactEndpointMarkedVacuumAssembler(
            ExactFaceInsertionBuilder(patch),
            roots,
            coverages,
            disk_checkpoint=checkpoint_store,
        ).evaluate()
        seal = issue_target_blind_m4_seal(result)
        if checkpoint_store is None:
            raise ProductionNotReady("authenticated checkpoint disappeared before sealing")
        resume_manifest = dict(result.authenticated_resume_manifest)
        payload = {
            "schema": "HODGE-SU3-EXACT-MARKED-CLUSTER-M4-v3-AUTHENTICATED",
            "status": "PASS_TARGET_BLIND_M4_SEALED",
            "coefficient": _json_exact(seal.coefficient),
            "construction_sha256": seal.construction_sha256,
            "scientific_result_sha256": seal.construction_sha256,
            "construction_payload": dict(seal.construction_payload),
            "authenticated_execution_attestation": dict(
                seal.authenticated_execution_attestation
            ),
            "gates": list(seal.gates),
            "lower_coefficients": _json_exact(result.lower_coefficients),
            "gamma_by_order": _json_exact(result.gamma_by_order),
            "endpoint_certificate_sha256": result.endpoint_certificate_sha256,
            "runtime_script_sha256": result.runtime_script_sha256,
            "checkpoint": dict(result.checkpoint),
            "persistent_checkpoint": str(Path(checkpoint_path)),
            "candidate_filter_scope": "necessary_not_sufficient",
            "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
            "candidate_coverage_certificate": dict(candidate_certificate),
            "physical_cluster_evaluations": 609,
            "fresh_cluster_evaluations": resume_manifest[
                "fresh_cluster_evaluations"
            ],
            "resumed_cluster_evaluations": resume_manifest[
                "resumed_cluster_evaluations"
            ],
            "authenticated_resume_manifest": resume_manifest,
            "invocation_nonce": authentication.invocation_nonce,
            "target_inputs": [],
        }
        payload["certificate_hmac_sha256"] = (
            checkpoint_store.certificate_hmac_sha256(payload)
        )
        encoded_certificate = _auth_canonical_bytes(payload)
        emit_authenticated_certificate_to_memfd(
            authentication, encoded_certificate
        )
        _atomic_bytes_write(destination, encoded_certificate)
        _atomic_json_write(status_destination, {
            "schema": "HODGE-SU3-EXACT-MARKED-CLUSTER-M4-v3-AUTHENTICATED",
            "status": "PASS_TARGET_BLIND_M4_SEALED",
            "runtime_script_sha256": starting_runtime_sha,
            "invocation_nonce": authentication.invocation_nonce,
            "certificate_sha256": hashlib.sha256(encoded_certificate).hexdigest(),
            "target_inputs": [],
        })
    except BaseException as error:
        if checkpoint_store is not None:
            checkpoint_store.close()
        if destination is not None:
            _atomic_json_write(status_destination, {
                "schema": "HODGE-SU3-EXACT-MARKED-CLUSTER-M4-v3-AUTHENTICATED",
                "status": "FAIL",
                "runtime_script_sha256": starting_runtime_sha,
                "invocation_nonce": authentication.invocation_nonce,
                "error_type": type(error).__name__,
                "error": str(error),
                "target_inputs": [],
            })
        raise
    if checkpoint_store is not None:
        checkpoint_store.close()
    return result, seal


@dataclass(frozen=True)
class TargetBlindM4Seal:
    coefficient: Fraction
    construction_sha256: str
    construction_payload: Mapping[str, Any]
    authenticated_execution_attestation: Mapping[str, Any]
    gates: tuple[str, ...]
    target_inputs: tuple[Any, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "coefficient", as_fraction(self.coefficient))
        if self.target_inputs:
            raise ValueError("a target-blind construction seal cannot contain target inputs")
        digest = str(self.construction_sha256).lower()
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ValueError("construction seal needs a 64-hex SHA256")
        payload = dict(self.construction_payload)
        expected_scientific_keys = {
            "schema", "coefficient", "lower_coefficients", "gamma_by_order",
            "raw_gap_ledger", "mobius_by_channel_sha256",
            "coverage_authorities", "candidate_manifest_sha256",
            "candidate_filter_scope", "physical_cluster_evaluations",
            "endpoint_certificate_sha256", "runtime_script_sha256", "gates",
            "target_inputs",
        }
        if set(payload) != expected_scientific_keys:
            raise ValueError("construction payload exact scientific schema changed")
        if payload.get("target_inputs") != []:
            raise ValueError("construction payload is not target blind")
        if hashlib.sha256(_auth_canonical_bytes(payload)).hexdigest() != digest:
            raise ValueError("construction payload does not reproduce its SHA256")
        if payload.get("coefficient") != _json_exact(self.coefficient):
            raise ValueError("construction payload coefficient changed")
        if tuple(payload.get("gates", ())) != tuple(self.gates):
            raise ValueError("construction payload gates changed")
        attestation = dict(self.authenticated_execution_attestation)
        expected_attestation_keys = {
            "schema", "configuration_sha256", "runtime_script_sha256",
            "authentication_context_sha256", "resume_run_id",
            "invocation_nonce", "candidate_manifest_sha256", "row_count",
            "row_manifest_sha256", "row_manifest_hmac_sha256",
            "fresh_cluster_evaluations", "resumed_cluster_evaluations",
            "current_run_sha256", "current_run_hmac_sha256", "gates",
        }
        if (
            set(attestation) != expected_attestation_keys
            or attestation["schema"] != AUTHENTICATED_EXECUTION_ATTESTATION_SCHEMA
            or attestation["candidate_manifest_sha256"]
            != O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
            or attestation["row_count"] != 609
            or type(attestation["fresh_cluster_evaluations"]) is not int
            or type(attestation["resumed_cluster_evaluations"]) is not int
            or attestation["fresh_cluster_evaluations"] < 0
            or attestation["resumed_cluster_evaluations"] < 0
            or attestation["fresh_cluster_evaluations"]
            + attestation["resumed_cluster_evaluations"] != 609
            or attestation["gates"] != [
                "authenticated-checkpoint-header",
                "authenticated-609-row-manifest",
                "fresh-invocation-nonce",
                "authenticated-current-run-summary",
            ]
        ):
            raise ValueError("authenticated execution attestation invariants failed")
        for key in expected_attestation_keys - {
            "schema", "candidate_manifest_sha256", "row_count",
            "fresh_cluster_evaluations", "resumed_cluster_evaluations", "gates",
        }:
            token = attestation[key]
            if type(token) is not str or len(token) != 64 or any(
                ch not in "0123456789abcdef" for ch in token
            ):
                raise ValueError(f"execution attestation {key} is not SHA256")
        object.__setattr__(self, "construction_sha256", digest)
        object.__setattr__(self, "construction_payload", MappingProxyType(payload))
        object.__setattr__(
            self,
            "authenticated_execution_attestation",
            MappingProxyType(attestation),
        )


def _phase3_numeric_support_sha256(supports: Iterable[Support]) -> str:
    """Digest one exact numeric-face support keyset in size/tuple order."""
    ordered = tuple(sorted(
        {frozenset(map(int, support)) for support in supports},
        key=lambda support: (len(support), tuple(sorted(support))),
    ))
    digest = hashlib.sha256()
    for support in ordered:
        encoded = _auth_canonical_bytes(sorted(support))
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
    return digest.hexdigest()


def _phase3_raw_gap_ledger(result: Phase3AssemblyResult) -> Mapping[str, Any]:
    """Serialize the 609 independent raw gaps used by literal Möbius inversion.

    This ledger is mathematical data, not resume telemetry.  It is therefore
    included in the stable scientific payload and is invariant under a fresh
    versus authenticated-resume execution split.
    """
    rows: list[Mapping[str, Any]] = []
    roots: dict[str, int] = {}
    support_sha256: dict[str, str] = {}
    support_counts: dict[str, int] = {}
    incidence_counts: dict[str, int] = {}
    size_histograms: dict[str, dict[str, int]] = {}
    for input_pol in range(3):
        coverage = result.coverages[input_pol]
        embeddings = tuple(coverage.embeddings)
        root_set = {embedding.canonical_root for embedding in embeddings}
        if len(root_set) != 1:
            raise ProductionNotReady("candidate coverage has no unique marked root")
        root = root_set.pop()
        if root != O4_TRIALITY_CANDIDATE_ROOT_FACE_BY_POL[input_pol]:
            raise ProductionNotReady("candidate numeric marked-root identity changed")
        supports = tuple(sorted(
            (embedding.canonical_support for embedding in embeddings),
            key=lambda support: (len(support), tuple(sorted(support))),
        ))
        if (
            len(supports) != 203
            or len(set(supports)) != 203
            or any(root not in support or len(support) > 6 for support in supports)
            or any(
                embedding.multiplicity != 1
                or any(source != target for source, target in embedding.face_map)
                for embedding in embeddings
            )
        ):
            raise ProductionNotReady("raw gap ledger coverage/keyset changed")
        incidence_count = sum(
            child < parent for parent in supports for child in supports
        )
        digest = _phase3_numeric_support_sha256(supports)
        if (
            incidence_count != 724
            or digest
            != O4_TRIALITY_CANDIDATE_NUMERIC_SUPPORT_SHA256[input_pol]
        ):
            raise ProductionNotReady("raw gap ledger support identity changed")
        histogram = Counter(map(len, supports))
        if dict(sorted(histogram.items())) != {1: 1, 2: 12, 3: 158, 4: 20, 5: 10, 6: 2}:
            raise ProductionNotReady("raw gap ledger support histogram changed")
        roots[str(input_pol)] = root
        support_sha256[str(input_pol)] = digest
        support_counts[str(input_pol)] = len(supports)
        incidence_counts[str(input_pol)] = incidence_count
        size_histograms[str(input_pol)] = {
            str(size): count for size, count in sorted(histogram.items())
        }
        for support in supports:
            gap_by_order = [
                [
                    result.mobius_by_channel[(order, input_pol, output_pol)].raw[
                        support
                    ]
                    for output_pol in range(3)
                ]
                for order in range(1, 5)
            ]
            rows.append(MappingProxyType({
                "input_pol": input_pol,
                "support": sorted(support),
                "gap_by_order": _json_exact(gap_by_order),
            }))
    if len(rows) != 609:
        raise ProductionNotReady("raw gap ledger is not the exact 609-row sweep")
    return MappingProxyType({
        "schema": PHASE3_RAW_GAP_LEDGER_SCHEMA,
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "row_count": 609,
        "roots_by_input_polarization": roots,
        "per_polarization_support_sha256": support_sha256,
        "per_polarization_support_count": support_counts,
        "per_polarization_proper_incidence_count": incidence_counts,
        "per_polarization_size_histogram": size_histograms,
        "embedding_multiplicity": 1,
        "rows": rows,
    })


def _phase3_mobius_payload(result: Phase3AssemblyResult) -> Mapping[str, Any]:
    return {
        str(channel): {
            str(tuple(sorted(support))): _json_exact(value)
            for support, value in reduced.omega.items()
        }
        for channel, reduced in result.mobius_by_channel.items()
    }


def issue_target_blind_m4_seal(result: Phase3AssemblyResult) -> TargetBlindM4Seal:
    """Seal only the complete physical 609-cluster endpoint-resolved result."""
    if not isinstance(result, Phase3AssemblyResult):
        raise ProductionNotReady(
            "legacy scalar/unlabelled Phase2 results can never issue an m4 seal"
        )
    if not result.physical_cluster_evaluations:
        raise ProductionNotReady("synthetic/raw cluster data cannot issue an m4 seal")
    if runtime_script_sha256() != result.runtime_script_sha256:
        raise ProductionNotReady("runtime script bytes changed before sealing")
    if set(result.coverages) != {0, 1, 2}:
        raise ProductionNotReady("all three full-T1 root polarizations are required")
    for coverage in result.coverages.values():
        if coverage.max_faces != O4_TRIALITY_CANDIDATE_MAX_FACES:
            raise ProductionNotReady(
                "each T1 coverage must match the sealed six-face candidate maximum"
            )
        if (
            coverage.authority_sha256
            != O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY
            or len(coverage.embeddings) != 203
        ):
            raise ProductionNotReady("coverage is not the sealed 203-row candidate closure")
        if not (coverage.complete and coverage.physical and coverage.mechanically_verified):
            raise ProductionNotReady(
                "mechanically verified complete physical embeddings are required"
            )
    if result.lower_coefficients != LOWER_ORDER_GAP_REGRESSION:
        raise ProductionNotReady("lower-order exact construction gates did not pass")
    for order, matrix in enumerate(result.gamma_by_order, start=1):
        _exact_gamma_scalar(matrix, f"order-{order}")
    if result.checkpoint.get("last_stage") != "phase3-full-t1-mobius-complete":
        raise ProductionNotReady("Phase3 checkpoint did not reach full-T1 completion")
    mobius_payload = _phase3_mobius_payload(result)
    raw_gap_ledger = _json_exact(_phase3_raw_gap_ledger(result))
    gates = (
        "exact-full-t1-physical-clusters",
        "six-face-direct-seven-face-folded-support-bound",
        "translated-intermediate-endpoint-convolution",
        "literal-rooted-mobius-all-three-polarizations",
        "sealed-203-row-candidate-keyset-per-polarization",
        "stage0-triality-filter-only-no-stage1-amplitudes",
        "lower-orders-one-through-three-exact",
        "target-blind-construction",
    )
    payload = {
        "schema": "HODGE-SU3-TARGET-BLIND-SCIENTIFIC-RESULT-v3",
        "coefficient": _json_exact(result.coefficient),
        "lower_coefficients": _json_exact(result.lower_coefficients),
        "gamma_by_order": _json_exact(result.gamma_by_order),
        "raw_gap_ledger": raw_gap_ledger,
        "mobius_by_channel_sha256": hashlib.sha256(
            _auth_canonical_bytes(mobius_payload)
        ).hexdigest(),
        "coverage_authorities": {
            str(pol): coverage.authority_sha256
            for pol, coverage in result.coverages.items()
        },
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "candidate_filter_scope": "necessary_not_sufficient",
        "physical_cluster_evaluations": 609,
        "endpoint_certificate_sha256": result.endpoint_certificate_sha256,
        "runtime_script_sha256": result.runtime_script_sha256,
        "gates": list(gates),
        "target_inputs": [],
    }
    resume_manifest = dict(result.authenticated_resume_manifest)
    execution_attestation = {
        "schema": AUTHENTICATED_EXECUTION_ATTESTATION_SCHEMA,
        "configuration_sha256": resume_manifest["configuration_sha256"],
        "runtime_script_sha256": result.runtime_script_sha256,
        "authentication_context_sha256": resume_manifest[
            "authentication_context_sha256"
        ],
        "resume_run_id": resume_manifest["resume_run_id"],
        "invocation_nonce": resume_manifest["invocation_nonce"],
        "candidate_manifest_sha256": O4_TRIALITY_CANDIDATE_MANIFEST_IDENTITY,
        "row_count": resume_manifest["row_count"],
        "row_manifest_sha256": resume_manifest["row_manifest_sha256"],
        "row_manifest_hmac_sha256": resume_manifest[
            "row_manifest_hmac_sha256"
        ],
        "fresh_cluster_evaluations": resume_manifest[
            "fresh_cluster_evaluations"
        ],
        "resumed_cluster_evaluations": resume_manifest[
            "resumed_cluster_evaluations"
        ],
        "current_run_sha256": resume_manifest["current_run_sha256"],
        "current_run_hmac_sha256": resume_manifest["current_run_hmac_sha256"],
        "gates": [
            "authenticated-checkpoint-header",
            "authenticated-609-row-manifest",
            "fresh-invocation-nonce",
            "authenticated-current-run-summary",
        ],
    }
    digest = hashlib.sha256(_auth_canonical_bytes(payload)).hexdigest()
    return TargetBlindM4Seal(
        coefficient=result.coefficient,
        construction_sha256=digest,
        construction_payload=MappingProxyType(payload),
        authenticated_execution_attestation=MappingProxyType(execution_attestation),
        gates=gates,
    )


Payload = TypeVar("Payload")


@dataclass(frozen=True)
class P(Generic[Payload]):
    payload: Payload


@dataclass(frozen=True)
class W1(Generic[Payload]):
    payload: Payload


@dataclass(frozen=True)
class R1(Generic[Payload]):
    """First reduced-resolvent output, sealed to the Q1 sector."""
    payload: Payload


@dataclass(frozen=True)
class W2(Generic[Payload]):
    payload: Payload


@dataclass(frozen=True)
class R2(Generic[Payload]):
    """Second reduced-resolvent output, sealed to the Q2 sector."""
    payload: Payload


class CanonicalFourthOrderSchedule(Generic[Payload]):
    """Runtime-sealed realization of P -> W1 -> R1 -> W2 -> R2.

    W has two and only two domain-specific callbacks: one for P and one for Q1.
    There is no Q2 callback. ``apply_w`` recognizes R2 only to raise before
    invoking either W backend, which makes any third-W branch fail closed.
    """

    def __init__(
        self,
        w_on_p: Callable[[Payload], Payload],
        r1_on_w1: Callable[[Payload], Payload],
        w_on_q1: Callable[[Payload], Payload],
        r2_on_w2: Callable[[Payload], Payload],
    ) -> None:
        self._w_on_p = w_on_p
        self._r1_on_w1 = r1_on_w1
        self._w_on_q1 = w_on_q1
        self._r2_on_w2 = r2_on_w2
        self._trace: list[str] = []

    @property
    def trace(self) -> tuple[str, ...]:
        return tuple(self._trace)

    def first_w(self, source: P[Payload]) -> W1[Payload]:
        if type(source) is not P:
            raise IllegalScheduleTransition("first W requires exactly a P stage")
        self._trace.append("P->W1")
        return W1(self._w_on_p(source.payload))

    def first_resolvent(self, stage: W1[Payload]) -> R1[Payload]:
        if type(stage) is not W1:
            raise IllegalScheduleTransition("R1 requires exactly a W1 stage")
        self._trace.append("W1->R1(Q1)")
        return R1(self._r1_on_w1(stage.payload))

    def second_w(self, stage: R1[Payload]) -> W2[Payload]:
        if type(stage) is not R1:
            if type(stage) is R2:
                raise WOnQ2Forbidden("W(Q2) is impossible in the canonical schedule")
            raise IllegalScheduleTransition("second W requires exactly an R1/Q1 stage")
        self._trace.append("R1(Q1)->W2")
        return W2(self._w_on_q1(stage.payload))

    def second_resolvent(self, stage: W2[Payload]) -> R2[Payload]:
        if type(stage) is not W2:
            raise IllegalScheduleTransition("R2 requires exactly a W2 stage")
        self._trace.append("W2->R2(Q2)")
        return R2(self._r2_on_w2(stage.payload))

    def apply_w(
        self, stage: P[Payload] | R1[Payload] | R2[Payload]
    ) -> W1[Payload] | W2[Payload]:
        """Auditable W dispatcher with no Q2 implementation."""
        if type(stage) is P:
            return self.first_w(stage)
        if type(stage) is R1:
            return self.second_w(stage)
        if type(stage) is R2:
            raise WOnQ2Forbidden("W(Q2) is impossible in the canonical schedule")
        raise IllegalScheduleTransition(f"W is undefined on {type(stage).__name__}")

    def run(self, source: P[Payload]) -> R2[Payload]:
        w1 = self.first_w(source)
        r1 = self.first_resolvent(w1)
        w2 = self.second_w(r1)
        return self.second_resolvent(w2)


def require_construction_seal(
    result: Phase3AssemblyResult | None = None,
) -> TargetBlindM4Seal:
    """Fail closed unless a completed endpoint-resolved Phase3 result is supplied."""
    if result is None:
        raise ProductionNotReady(
            "PHASE3_NOT_YET_EVALUATED: the exact Phase3 assembler is ready, but "
            "the sealed 609-row full-T1 candidate sweep has not completed"
        )
    return issue_target_blind_m4_seal(result)


def run_production_m4(
    result: Phase3AssemblyResult | None = None,
) -> Fraction:
    """Return only a coefficient carried by a freshly issued target-blind seal."""
    return require_construction_seal(result).coefficient


def terminal_hamer_diagnostic(
    candidate: TargetBlindM4Seal | Fraction,
    external_reference: Fraction,
    *,
    enabled: bool = False,
) -> Mapping[str, Fraction]:
    """Compare only an already-sealed result with a caller-supplied reference."""
    if not enabled or not isinstance(candidate, TargetBlindM4Seal):
        raise HamerDiagnosticDisabled(
            "terminal Hamer comparison requires an enabled target-blind construction seal"
        )
    coefficient = candidate.coefficient
    external_reference = as_fraction(external_reference)
    return MappingProxyType({
        "candidate": coefficient,
        "external_reference": external_reference,
        "difference": coefficient - external_reference,
    })


def _matrix_from_rows(rows: Sequence[Sequence[Any]]) -> sp.Matrix:
    if sp is None:
        raise ExactEngineError("SymPy matrix requested in a runtime without SymPy")
    return sp.Matrix([[
        sp.Rational(as_fraction(value).numerator, as_fraction(value).denominator)
        for value in row
    ] for row in rows])


def run_self_tests(verbose: bool = True) -> tuple[tuple[str, bool], ...]:
    """Run only cheap exact-local and synthetic Phase2/Phase3 gates."""
    gates: list[tuple[str, bool]] = []

    def check(name: str, condition: bool) -> None:
        passed = bool(condition)
        gates.append((name, passed))
        if verbose:
            print(("[PASS] " if passed else "[FAIL] ") + name)
        if not passed:
            raise AssertionError(name)

    unitary_trace = trace_state(((0, 1), (0, -1)))
    factor, reduced = simplify_unitarity(unitary_trace)
    check("free unitarity Tr(U Udag)=3", factor == 3 and reduced == EMPTY_STATE)

    plaquette = trace_state(((0, 1), (1, 1), (2, -1), (3, -1)))
    check(
        "one-face H0 eigenvalue is exact",
        h0_action(plaquette) == {plaquette: REFERENCE_E0},
    )
    check("one-face Haar norm is exact", haar_inner(plaquette, plaquette) == 1)

    for degree in (1, 2, 3):
        permutations, inverse = balanced_weingarten(degree)
        gram = fraction_matrix([[
            N ** permutation_cycles(
                permutation_compose(permutation_inverse(left), right)
            )
            for right in permutations
        ] for left in permutations])
        check(
            f"balanced ({degree},{degree}) exact projector inverse",
            fraction_matrix_multiply(gram, inverse)
            == fraction_identity(len(permutations)),
        )

    cubic_trace = trace_state(((0, 1), (0, 1), (0, 1)))
    check(
        "determinant (3,0) exact Haar gate",
        haar_inner(EMPTY_STATE, cubic_trace) == 1,
    )

    mixed_gram = fraction_matrix(MIXED_41_GRAM)
    mixed_inverse = fraction_matrix(MIXED_41_PSEUDOINVERSE)
    check(
        "mixed (4,1) invariant-space rank=3",
        fraction_matrix_rank(mixed_gram) == 3,
    )
    check(
        "mixed (4,1) exact projector identity",
        fraction_matrix_multiply(
            fraction_matrix_multiply(mixed_gram, mixed_inverse), mixed_gram
        ) == mixed_gram,
    )

    exact_ready_counts = tuple(family.value for family in HaarFamily)
    exact_ready_work = []
    for n_u, n_ubar in exact_ready_counts:
        total_occurrences = n_u + n_ubar
        contracted = contract_link_partition(
            tuple(range(2 * total_occurrences)),
            tuple(range(n_u)),
            tuple(range(n_u, total_occurrences)),
        )
        exact_ready_work.append(
            bool(contracted)
            and all(isinstance(value, Fraction) for value in contracted.values())
        )
    check("all nine Phase-1 exact Haar routes contract", all(exact_ready_work))

    pure_six_gates = pure_six_exact_gates()
    check("pure-six invariant count is ten", pure_six_gates["partition_count"] == 10)
    check("pure-six exact Gram rank is five", pure_six_gates["gram_rank"] == 5)
    check("pure-six exact tight-frame identity", pure_six_gates["tight_frame"])
    check("pure-six exact Moore-Penrose identities",
          pure_six_gates["mp_GGpG"] and pure_six_gates["mp_pGpGp"])
    check("pure-six coefficient projector is exact",
          pure_six_gates["projector_symmetric"]
          and pure_six_gates["projector_idempotent"]
          and pure_six_gates["projector_trace"] == 5)
    check("pure-six endpoint DSU adapter is complete",
          pure_six_gates["delta_branch_count"] == 456
          and pure_six_gates["dsu_term_count"] == 456)

    poison_calls: list[str] = []
    poison_request = HaarRouteRequest(
        2, 5, "W2", "Q1", "Q2", "q1-state", "q2-state", "link-17",
        "h0-block", "flux-block", "phase1-control",
    )
    try:
        DEFAULT_HAAR_ROUTER.route(
            poison_request,
            lambda _family: poison_calls.append("called"),
        )
    except ForbiddenHaarFamily as error:
        poison_refused = bool(error.provenance)
    else:
        poison_refused = False
    check("(2,5) poison hard-fails with provenance before contractor",
          poison_refused and not poison_calls)

    adjacency = {0: {1}, 1: {0, 2}, 2: {1}}
    connected = lambda support: connected_in_adjacency(support, adjacency)
    minimal = {
        frozenset({0}): Fraction(1, 2),
        frozenset({0, 1}): Fraction(1, 3),
        frozenset({0, 1, 2}): Fraction(-1, 7),
    }
    incidence = rooted_incidence_transform(minimal, 0, connected)
    check("literal rooted incidence recursion recovers the exact ledger",
          dict(incidence.omega) == minimal)
    check("support-union convolution is exact",
          dict(rooted_union_convolution(
              {frozenset({0}): Fraction(2, 3)},
              {frozenset({0, 1}): Fraction(3, 5)},
          )) == {frozenset({0, 1}): Fraction(2, 5)})

    patch = build_open_cubic_patch((
        ((0, 0, 0), 0, 1),
        ((0, 0, 0), 0, 2),
    ))
    concrete_clusters = enumerate_rooted_open_clusters(patch, 0, 2)
    check(
        "open cubic one/two-face rooted clusters are literal and link-connected",
        tuple(cluster.support for cluster in concrete_clusters)
        == (frozenset({0}), frozenset({0, 1})),
    )
    check(
        "one/two-face clusters expose concrete open boundary links",
        all(cluster.exposed_links for cluster in concrete_clusters),
    )

    builder = ExactFaceInsertionBuilder(patch)
    axial = builder.source_axial(0)
    inserted = builder.insert_face(axial, 1, +1)
    check(
        "exact face insertion is Fraction-native on the two-face cluster",
        bool(inserted) and all(isinstance(value, Fraction) for value in inserted.values()),
    )
    q2_probe_calls: list[str] = []
    try:
        apply_w_labelled(
            builder,
            {frozenset({0}): axial},
            {0, 1},
            source_sector=PerturbativeSector.Q2,
        )
    except WOnQ2Forbidden:
        phase2_q2_refused = True
    else:
        phase2_q2_refused = False
        q2_probe_calls.append("contracted")
    check("Phase2 face W(Q2) fails before contraction", phase2_q2_refused and not q2_probe_calls)

    # Do not contract an actual half-history in the local self-test: even the
    # one-face exact Haar endpoint can exceed the ten-second desktop budget.
    # The physical path is exercised in Colab; here we inject exact block/ledger
    # values and test every assembly identity without fitting any coefficient.
    mocked_blocks = ExactGlobalBlockElements(
        Fraction(1), Fraction(2, 3), Fraction(2, 3),
        Fraction(-5, 7), Fraction(11, 13), Fraction(11, 13),
    )
    check(
        "PP/PQ1/Q1Q1/Q1Q2 and adjoints are exact",
        all(
            isinstance(getattr(mocked_blocks, name), Fraction)
            for name in ("PP", "PQ1", "Q1P", "Q1Q1", "Q1Q2", "Q2Q1")
        )
        and mocked_blocks.PQ1 == mocked_blocks.Q1P
        and mocked_blocks.Q1Q2 == mocked_blocks.Q2Q1,
    )
    root_support, pair_support = frozenset({0}), frozenset({0, 1})
    injected_a = {root_support: Fraction(1)}
    injected_e2 = {root_support: Fraction(2)}
    injected_n = {pair_support: Fraction(3)}
    injected_sigma3 = {pair_support: Fraction(4)}
    injected_an = rooted_union_convolution(injected_a, injected_n)
    injected_e3 = ledger_linear_combination((1, injected_sigma3), (-1, injected_an))
    synthetic_lower = ExactLowerOrderLedgers(
        injected_a, injected_e2, injected_sigma3, injected_n, injected_an, injected_e3
    )
    injected_c = {pair_support: Fraction(5)}
    injected_j = {root_support: Fraction(7)}
    injected_d = {pair_support: Fraction(11)}
    injected_e2n = rooted_union_convolution(injected_e2, injected_n)
    injected_ac = rooted_union_convolution(injected_a, injected_c)
    injected_aaj = rooted_union_convolution(
        rooted_union_convolution(injected_a, injected_a), injected_j
    )
    injected_e4 = ledger_linear_combination(
        (1, injected_d), (-1, injected_e2n), (-2, injected_ac), (1, injected_aaj)
    )
    synthetic_fourth = ExactFourthOrderLedgers(
        injected_a, injected_e2, injected_n, injected_c, injected_j, injected_d,
        injected_e2n, injected_ac, injected_aaj, injected_e4,
    )
    check(
        "independent n=1..3 and D/N/J/C ledgers remain exact",
        all(
            isinstance(value, Fraction)
            for ledger in (
                synthetic_lower.A, synthetic_lower.E2, synthetic_lower.E3,
                synthetic_fourth.D, synthetic_fourth.N, synthetic_fourth.J,
                synthetic_fourth.C, synthetic_fourth.E4,
            )
            for value in ledger.values()
        ),
    )

    raw_gap = {
        frozenset({0}): Fraction(1, 2),
        frozenset({0, 1}): Fraction(5, 6),
    }
    synthetic_coverage = EmbeddingCoverageCertificate(
        (
            RootedEmbedding(((0, 0),), 0, 0, 2),
            RootedEmbedding(((0, 0), (1, 1)), 0, 0, 3),
        ),
        max_faces=2,
        complete=True,
        physical=False,
        authority_sha256="synthetic",
    )
    journal = Phase2CheckpointJournal()
    assembled = assemble_rooted_gap_from_raw(
        raw_gap,
        tuple(raw_gap),
        root=0,
        connected=lambda support: connected_in_adjacency(support, patch.adjacency),
        coverage=synthetic_coverage,
        journal=journal,
    )
    check(
        "literal raw-cluster Mobius subtracts the rooted singleton",
        dict(assembled.mobius.omega) == {
            frozenset({0}): Fraction(1, 2),
            frozenset({0, 1}): Fraction(1, 3),
        },
    )
    check("literal embedding multiplicities sum exact omega", assembled.embedded_coefficient == 2)
    check(
        "Phase2 heartbeat/checkpoint chain is deterministic and complete",
        assembled.checkpoint["event_count"] == 3
        and assembled.checkpoint["last_stage"] == "embedding-sum-complete"
        and journal.digest != "0" * 64,
    )
    try:
        issue_target_blind_m4_seal(assembled)
    except ProductionNotReady:
        synthetic_seal_refused = True
    else:
        synthetic_seal_refused = False
    check("synthetic clusters cannot issue a production seal", synthetic_seal_refused)

    phase3_left = EndpointSupportKey(
        frozenset({0, 1, 3, 4}), 0, 1, 0, 1,
        ((3, 4),), ("K2",),
    )
    phase3_right = EndpointSupportKey(
        frozenset({1, 2, 5, 6}), 1, 2, 1, 2,
        ((5, 6),), ("N",),
    )
    phase3_fold = compose_endpoint_ledgers(
        {phase3_left: Fraction(2, 3)},
        {phase3_right: Fraction(3, 5)},
        (0, 1, 2),
    )
    phase3_key = next(iter(phase3_fold.ledger))
    check(
        "Phase3 audits all ordered intermediate endpoints",
        len(phase3_fold.audited_paths) == 27
        and phase3_fold.matched_record_products == 1,
    )
    check(
        "folded K2*N retains initial/intermediate/final P faces and four actions",
        phase3_key.support == frozenset(range(7))
        and phase3_key.intermediate_faces == (1,)
        and phase3_key.history_depth == 4
        and tuple(phase3_fold.ledger.values()) == (Fraction(2, 5),),
    )
    check(
        "direct/folded support bounds are exactly six/seven",
        DIRECT_FOURTH_ORDER_MAX_MARKED_FACES == 6
        and FOURTH_ORDER_MAX_MARKED_FACES == 7,
    )
    candidate_manifest = load_o4_triality_candidate_manifest()
    candidate_patch, candidate_roots, candidate_coverages, candidate_certificate = (
        build_o4_triality_candidate_full_t1_coverage()
    )
    check(
        "Stage0 triality filter is explicitly necessary not sufficient",
        candidate_manifest["necessary_not_sufficient"] is True
        and candidate_manifest["completeness"][
            "physical_amplitudes_or_stage1_filters_used"
        ] is False,
    )
    check(
        "corrected canonical sign census seals 33,702 triality rows",
        candidate_manifest["counts"]["corrected_triality_sign_histories"] == 33702
        and candidate_manifest["counts"]["stage0_invalid_published_sign_histories"] == 68
        and candidate_manifest["counts"]["stage0_missing_recomputed_sign_histories"] == 32,
    )
    check(
        "literal candidate closure seals 203 supports and 724 proper incidences",
        candidate_manifest["concrete_downward_closure_count"] == 203
        and candidate_manifest["concrete_proper_incidence_count"] == 724
        and candidate_manifest["concrete_proper_incidence_sha256"]
        == "6d8729df01236c447b2863973f4de5caa9725d8fc871cfcd95deb2d752bdc4d4",
    )
    check(
        "three fresh T1 input sweeps contain exactly 609 concrete evaluations",
        len(candidate_patch.faces) == 93
        and set(candidate_roots) == {0, 1, 2}
        and all(len(coverage.embeddings) == 203 for coverage in candidate_coverages.values())
        and candidate_certificate["physical_cluster_evaluation_count"] == 609,
    )
    check(
        "candidate max six is distinct from the folded endpoint-label firewall seven",
        all(
            coverage.max_faces == O4_TRIALITY_CANDIDATE_MAX_FACES
            for coverage in candidate_coverages.values()
        )
        and O4_TRIALITY_CANDIDATE_MAX_FACES == 6
        and FOURTH_ORDER_MAX_MARKED_FACES == 7,
    )
    check(
        "reviewed candidate certificate is fixed before physical authorization",
        candidate_certificate["certificate_sha256"]
        == O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256,
    )
    try:
        run_exact_phase3_physical(
            authorized_cluster_evaluations=608,
            authorized_candidate_certificate_sha256=(
                O4_TRIALITY_CANDIDATE_FULL_T1_CERTIFICATE_SHA256
            ),
        )
    except ProductionNotReady:
        wrong_count_refused = True
    else:
        wrong_count_refused = False
    check("wrong candidate count fails before physical construction", wrong_count_refused)
    try:
        run_exact_phase3_physical(
            authorized_cluster_evaluations=609,
            authorized_candidate_certificate_sha256="0" * 64,
        )
    except ProductionNotReady:
        wrong_candidate_sha_refused = True
    else:
        wrong_candidate_sha_refused = False
    check("wrong candidate certificate fails before physical construction", wrong_candidate_sha_refused)
    reflected = phase3_left.transpose()
    require_endpoint_hermitian(
        {phase3_left: Fraction(1), reflected: Fraction(1)}, (0, 1), "mock K2"
    )
    check("endpoint adjoint is an exact computed reflection", True)

    calls: list[str] = []
    schedule = CanonicalFourthOrderSchedule(
        lambda value: calls.append("W(P)") or value + 1,
        lambda value: calls.append("R1") or value + 1,
        lambda value: calls.append("W(Q1)") or value + 1,
        lambda value: calls.append("R2") or value + 1,
    )
    final = schedule.run(P(0))
    check("typed canonical schedule reaches R2/Q2", final == R2(4))
    check(
        "only P->W1->R1->W2->R2 is scheduled",
        schedule.trace == (
            "P->W1", "W1->R1(Q1)", "R1(Q1)->W2", "W2->R2(Q2)"
        ),
    )
    check(
        "W called only on P and Q1",
        calls == ["W(P)", "R1", "W(Q1)", "R2"],
    )
    before = tuple(calls)
    try:
        schedule.apply_w(final)
    except WOnQ2Forbidden:
        q2_refused = True
    else:
        q2_refused = False
    check("W(Q2) fails before backend call", q2_refused and tuple(calls) == before)

    try:
        run_production_m4()
    except ProductionNotReady:
        production_refused = True
    else:
        production_refused = False
    check("unevaluated Phase 3 refuses a production coefficient", production_refused)
    check(
        "manifest is ready but explicitly not yet evaluated",
        CONSTRUCTION_MANIFEST["status"] == PHASE3_STATUS,
    )
    return tuple(gates)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test", action="store_true", help="run cheap exact/structural gates only"
    )
    parser.add_argument(
        "--show-manifest", action="store_true", help="print the fail-closed manifest"
    )
    parser.add_argument(
        "--run-phase3-physical",
        action="store_true",
        help="launch the sealed 609-cluster full-T1 exact construction",
    )
    parser.add_argument(
        "--geometry-preflight",
        action="store_true",
        help="validate the sealed 609-cluster candidate closure with zero physics",
    )
    parser.add_argument(
        "--output",
        default="HODGE_SU3_EXACT_MARKED_CLUSTER_M4_CERTIFICATE.json",
        help="atomic JSON output used only with --run-phase3-physical",
    )
    parser.add_argument(
        "--checkpoint",
        default="HODGE_SU3_EXACT_MARKED_CLUSTER_M4_CHECKPOINT.sqlite",
        help="transactional per-cluster resume database for the physical sweep",
    )
    parser.add_argument(
        "--authorized-cluster-evaluations",
        type=int,
        default=None,
        help="must be the reviewed sealed candidate count: 609",
    )
    parser.add_argument(
        "--authorized-candidate-certificate-sha256",
        default=None,
        help="must be the reviewed full-T1 candidate coverage certificate SHA256",
    )
    options = parser.parse_args(argv)
    if options.show_manifest:
        for key, value in CONSTRUCTION_MANIFEST.items():
            print(f"{key}: {value}")
    if options.geometry_preflight:
        preflight = phase3_geometry_preflight()
        print(json.dumps(_json_exact(preflight), sort_keys=True, indent=2, allow_nan=False))
        print("TRIALITY_CANDIDATE_PREFLIGHT_PASS_609_NO_PHYSICS")
    elif options.run_phase3_physical:
        _result, seal = run_exact_phase3_physical(
            output_path=options.output,
            checkpoint_path=options.checkpoint,
            authorized_cluster_evaluations=options.authorized_cluster_evaluations,
            authorized_candidate_certificate_sha256=(
                options.authorized_candidate_certificate_sha256
            ),
        )
        print("PASS_TARGET_BLIND_M4_SEALED")
        print(f"m4={seal.coefficient}")
        print(f"certificate={options.output}")
    elif options.self_test or not options.show_manifest:
        gates = run_self_tests(verbose=True)
        print(
            f"{sum(passed for _name, passed in gates)}/{len(gates)} "
            "exact Phase-2/Phase-3 gates passed"
        )
        print(PHASE3_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
