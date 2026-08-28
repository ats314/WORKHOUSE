# WORKHOUSE uniform carrier-residue (H3) audit

Date: 2026-08-22  
Scope: unpublished PMBSF/LCI/Bałaban/source-radius material, `carrier4.txt` Part VII, and the exact RG–OS/transfer-entry route.  
Repository status: read-only; this report is external to the WORKHOUSE clone.

## 1. Target

After separated-time normalization, the carrier-residue target is a cutoff-independent lower bound

`lambda_min Z_a >= z_*>0`,

where `Z_a` is the matrix weight of a shrinking carrier mass island in the normalized zero-momentum source measure. Equivalently, in the compact transfer variable `x=exp(-AE)`, it is

`eta_a(J_a) >= z_* I`

for intervals `J_a` shrinking to `x_*=exp(-AM)` with `0<x_*<1`, equivalently `0<M<infinity`.

The fixed-spacing CMP(4) theorem proves this type of bound for the literal three-orientation Wilson source in the small-`u` lattice quasiparticle band. The present question is whether the unpublished continuum/RG/source material transports that bound along a Wilson continuum scaling trajectory.

## 2. Decisive non-implication in `carrier4.txt`

Line 316 of `carrier4.txt` identifies the desired PMBSF anchored activity estimate

`sum_(Gamma joining p,r) |w_s(Gamma)| exp[a(Gamma)] <= C exp[-m d(p,r)]`

with a carrier correlator decay rate and then treats it as progress toward a carrier atom/residue.

Even if the displayed PMBSF estimate were proved for the signed carrier source, this inference would not establish H3. An absolute activity bound can imply an upper estimate

`|C(t)| <= C_0 exp(-Mt)`.

It cannot produce a lower bound on the bottom atom.

### Counterexample

Let

`dmu(E)=1_[M,M+1](E) dE`.

Then

`C(t)=exp(-Mt)(1-exp(-t))/t` and `C(0)=1`.

This correlator is completely monotone and therefore has a positive spectral/transfer representation. It obeys exponential upper decay with bottom exponent `M`, yet

`mu({M})=0`.

Thus reflection positivity, a positive transfer representation, an analytic Gaussian source, exponential clustering, and even the correct support-edge exponent are all compatible with zero carrier atom. The example does not itself construct a Wilson/Bałaban polymer expansion; rather, it proves that any polymer theorem used only through an exponential **upper** bound is insufficient.

The missing ingredient must be an actual Riesz/pole lower bound, or an exact leading exponential whose coefficient is uniformly nonzero and whose remainder is uniformly strictly faster after source normalization. A generic nonzero leading marked polymer is not enough unless those spectral and remainder properties are proved. No audited PMBSF file proves such an inequality for the SU(3) charge-odd carrier.

## 3. PMBSF inventory and exact status

### 3.1 Valid deterministic positive-source steps

The following pieces are mathematically useful within their stated nonnegative-source scope:

- positive Taylor-coefficient extraction from a source partition function;
- TOS+J to positive tilt-radius bounds;
- deterministic projected plaquette/capacity identities and PTO summability components;
- local one-link heat-bath and cap-geometry reductions;
- finite-channel SU(3) class-Hamiltonian calculations.

Here “source radius” is a radius in the positive tilt parameter, or an exponential moment of a rooted rare-defect capacity. It is **not** the physical spatial radius of a flowed/smeared carrier source.

### 3.2 Current open inputs

`PMBSF_SU2_conditional_firewall_paper_v3_4_merged_20260526.md` replaces the old broad source-weighted expansion by a narrower rare-defect route, but its displayed LCI-to-TOS+J passage is not closed as written. The current file proves cap-indicator tilt control and then applies it to the actual smooth `X`-source tilt; normalized tilted ratios are not ordered by pointwise domination of their tilt functions. The revised Section 8 correctly replaces that step by an unproved smooth-source LCI hypothesis (8.15).

The current rare-defect stack therefore still needs:

1. local cap-intersection typicality;
2. Bałaban far-source stability of the LCI parameters;

plus a boundary-band auxiliary.

`PMBSF_SU2_Paper_Section_14_Remaining_Analytic_Tasks.md` records a historical broader branch and still labels the following targets open:

- smooth-source LCI, including (14.12);
- far-source stability, (14.26);
- the optional/superseded marked activities/KP/anchored decay package, (14.35)–(14.37);
- the hard-source boundary gate.

The carrier's analyticity avoids the hard-indicator smoothing problem, but it does not supply the missing signed noncancellation estimate, SU(3) source derivative, physical source-radius scaling, OS transfer entry, or KL atom lower bound.

### 3.3 Concrete normalized-tilt error in both the old reduction and current v3.4 presentation

`LCI_TOSJ_Reduction_for_LemmaQ_20260526.md`, lines 778–791, uses pointwise domination

`X_r <= 1_(C_r)`

inside positive tilts to infer a normalized conditional expectation bound. Pointwise domination of the tilt factors does not order their normalized ratios.

For a direct counterexample, let `P(A)=q`, let the target and actual incident source both be `X=1_A`, and let the cap envelope be `Y=1_(A union B)` with `P(B)=1/2`. Then `X<=Y`. With `s=1/q`, the actual `X`-tilted target probability approaches `1/2`, while the broader cap tilt can keep the target probability of order `q`. A bound proved under the envelope tilt therefore does not imply the desired bound under the actual normalized tilt.

The same logical substitution appears in the current v3.4 presentation when it moves from cap-indicator tilts to the actual smooth source. This does not refute every possible LCI theorem. It refutes the displayed normalization step and confirms that the relevant source-tilted estimate must be proved directly, as the revised Section 8 now requires.

### 3.4 Gauge-group mismatch

The canonical PMBSF paper is SU(2). For SU(2), `Tr U` is real and charge conjugation is gauge-trivial, so

`Im Tr U=0`.

The SU(2) nonnegative defect machinery therefore cannot directly carry the WORKHOUSE SU(3), `C=-` Wilson source.

## 4. Exact local SU(3) source anchor

The unpublished SU(3) shell calculation contains a genuine source-entry seed. In its Weyl–Gaussian normalization,

`psi_0=sqrt(6)/(3 sqrt(pi))`,

`psi_2=sqrt(5)/(15 sqrt(pi)) y(3x^2-y^2)`,

and

`p_3=sqrt(6)/6 y(3x^2-y^2)`.

Therefore

`p_3=[sqrt(30 pi)/2] psi_2`,

`p_3 psi_0=sqrt(5) psi_2`,

and

`<psi_0,p_3^2 psi_0>=5`.

After normalization, the unperturbed oscillator `p_3` source has unit weight onto the corresponding odd local state. The literal Wilson source has `Im Tr exp(i theta)=-p_3/6+O(theta^5)`, and no audited result controls that remainder uniformly through global geometry and RG blocking. Thus this is an exact finite-dimensional source anchor, not yet a literal-Wilson residue theorem. It does not by itself control the thermodynamic source frame, RG blocking errors, or the continuum KL residue.

## 5. Strongest valid H3 route

The exact path-product block map and the RG–OS isometry provide the correct mechanism. For one fixed-origin coarse source `W_c` and its exact fine pullback, the entire normalized source spectral measure is preserved at every physical block time. This does not automatically preserve the cross terms required by a translation-completed fine `p=0` source; those are a separate momentum-entry obligation below.

To obtain that coarse island from the fixed-spacing CMP(4) reference, use the transfer-entry theorem. Fiberwise, let `(T_*(k),J_{W,*}(k))` be the reference positive transfer and **unprojected** literal-Wilson synthesis map, let `P_*(k)` be its carrier projection, and assume the uniformly bounded raw source norm `sup_k||J_{W,*}(k)||<=M_*` supplied by the clustered unprojected Gram kernel. The projected frame bound is

`J_{W,*}(k)^* P_*(k) J_{W,*}(k) >= z_* I_3`.

After constructing a specified gauge-, charge-, cubic-, translation-, and alias-covariant common Hilbert/fiber identification, it is sufficient to prove uniformly in cutoff and volume

`||T_hat_c-T_*|| <= epsilon_T < d_*/4`  `(TE)`

and

`||J_hat_(W,c)-J_(W,*)|| <= epsilon_W`  `(SE)`.

Riesz perturbation theory gives

`||P_hat_c-P_*|| <= eta_P`

and the unnormalized coarse frame bound

`J_{W,c}(k)^*P_c(k)J_{W,c}(k) >= z_ent I_3`,

where

`z_ent = z_* - 2M_*epsilon_W - epsilon_W^2 - M_*^2 eta_P`.

If `z_ent>0`, then `||J_{W,c}(k)||<=M_*+epsilon_W`. For time-zero Gram whitening the normalized island fraction obeys

`lambda_min[(J_{W,c}^*J_{W,c})^(-1/2) J_{W,c}^*P_cJ_{W,c} (J_{W,c}^*J_{W,c})^(-1/2)]`

`>= z_ent/(M_*+epsilon_W)^2 > 0`.

For the positive separated-time normalization used in the matrix KL theorem, at the completed `p=0` fiber define

`G_c(tau_0)=J_{W,c}^*exp(-2tau_0H_c)J_{W,c}`

and

`Z_c(tau_0)=G_c(tau_0)^(-1/2)J_{W,c}^*P_c exp(-2tau_0H_c)P_cJ_{W,c}G_c(tau_0)^(-1/2)`.

Suppose the carrier island lies below a uniform physical energy `E_+`. Its filtered numerator is at least

`exp(-2tau_0 E_+) z_ent I`,

while the complete filtered Gram is at most `(M_*+epsilon_W)^2 I`. It is invertible because it contains the positive carrier contribution. Hence the exact normalized whole-island bound is

`lambda_min Z_c(tau_0) >= exp(-2tau_0 E_+) z_ent/(M_*+epsilon_W)^2>0`.

After the uniform thermodynamic and alias-completed fiber passage, exact OS pullback preserves this lower bound for the fine extended Wilson-loop source of fixed physical blocked size. It becomes H3—an exact bottom-atom bound at `p=0`—if momentum completion leaves exactly one irreducible rank-three cubic `T1` copy: cubic covariance and Schur's lemma then make the transfer scalar on that fiber. If alias completion produces several `T1` copies, one must additionally isolate a source-weighted sub-island whose physical-energy diameter tends to zero. No orthogonal-fiber contraction estimate is needed merely for this carrier-visible atom. Such a complement estimate is needed later for full-sector isolation and standard Haag–Ruelle stability.

## 6. Exact first missing inequalities

Before `(TE)` and `(SE)` are meaningful, no audited unpublished file constructs the required common symmetry-covariant, alias-complete `p=0` representation for the exact blocked four-dimensional SU(3) Wilson systems. Conditional on that construction, no file proves the two entry estimates uniformly along the continuum trajectory.

The missing statements are not generic declarations that “the continuum is hard.” They are the explicit operator inequalities

`sup_(n,L,p in K) ||(T_hat_c,n,L(p)-T_*,L(p))(z-T_*,L(p))^(-1)|| < 1`

on an isolating contour (the contour-relative form of TE), and

`sup_(n,L,p in K) ||J_hat_(W,c),n,L(p)-J_(W,*),L(p)|| <= epsilon_W`

with the displayed positive `z_ent` margin.

The momentum-entry gate is quantitative, not merely formal. A fixed-origin block map is covariant only under block-step translations. To speak about the fine `p=0` fiber, one must include all `b_n^3` residue-class block origins, prove their closed span reduces the fine transfer and all one-step translations, construct the alias-fiber disintegration, and establish a uniform cross-Gram/frame lower bound. Equivalently, one may build an alias-complete direct-integral intertwiner carrying those same properties.

No corpus file supplies that fiber matching or proves that the completed rest fiber remains a single `T1` copy (or provides the shrinking-island substitute).

## 7. What PMBSF can still contribute

PMBSF/Bałaban machinery remains relevant as a possible way to control the error terms in TE and SE:

- unmarked polymer locality can control coarse transfer corrections;
- a new signed SU(3) marked expansion can control source derivatives;
- finite-dimensional LCI/local class calculations can provide block anchors;
- rooted bounds can identify the worst polymer classes and boundary conditions.

But an absolute upper activity bound must be supplemented by a source-entry/Riesz lower comparison, or by a pure leading exponential with a uniformly nonzero coefficient and uniformly faster remainder. It cannot be promoted directly to H3.

## 8. Status

- **Defined and normalized:** the continuum carrier atom target.
- **Proved at fixed small `u`:** positive literal-Wilson full-island frame.
- **Proved abstractly:** exact OS pullback preserves its normalized measure; TE+SE preserve a uniformly visible island under controlled coarse/reference mismatch; a single irreducible `T1` rest fiber or shrinking-island condition turns that into the atom hypothesis.
- **Proved locally:** a nonzero SU(3) `p_3` source anchor.
- **First unresolved model step:** construct the common alias-complete, spectrally resolved `p=0` representation for the exact blocked SU(3) Wilson system; then prove uniform TE+SE and the continuum moment/source interfaces.
- **Not supplied by PMBSF:** a lower carrier atom/residue bound.
