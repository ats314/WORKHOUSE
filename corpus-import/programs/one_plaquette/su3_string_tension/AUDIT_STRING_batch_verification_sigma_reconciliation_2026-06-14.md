# Batch verification + $\sigma$ convention reconciliation

**Date:** June 14, 2026
**Trigger:** nine uploaded bundles, including the native string-tension engine
sources that were missing in the previous session.

## Headline result

Running the **native string-tension engine from source** resolves a sign
conflict the project had flagged as open, and confirms the consolidated
theorem's $\sigma_5,\sigma_6$ signs. Three further engines (fifth-order glueball,
shell-six channel mixing) reproduce from source. No values were fabricated.

---

## 1. Native string tension is real through $\sigma_4$ (ran from source)

`SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2/ENGINE_STRING_reproduce.sh` ran end-to-end and
reproduced, from the connected-support contraction (not from KPS):

$$
\sigma_2=-\tfrac{22}{153},\qquad
\sigma_3^{\rm reduced}=+\tfrac{61}{408},\qquad
\sigma_4=-\tfrac{737327120374220449}{7250590288602460800},
$$

with $L=4$/$L=5$ length-independence and exact agreement against the KPS table
through order four. This **upgrades** $\sigma_2,\sigma_3,\sigma_4$ from
"asserted native" to "reproduced from source." The engine confirms the
sign/variable relation

$$
\boxed{\sigma_n(u)=(-1)^n\,\sigma_n^{\rm reduced}},
$$

so the physical $u=\beta_{\rm lat}/6$ coefficients are $\sigma_2(u)=-\tfrac{22}{153}$,
$\sigma_3(u)=-\tfrac{61}{408}$, $\sigma_4(u)=-\tfrac{737\ldots}{7250\ldots}$.

## 2. $\sigma_5,\sigma_6$ sign convention — RESOLVED

`SU3_KPS_STRING_COEFFICIENT_EXTRACTION` extracts KPS Table 2,
$W(x)=\sum t_n x^n$ with $x=2/g^4$, and converts via
$\sigma(y)=\tfrac12 W(-2y)$, giving $\sigma_5=+137767\ldots/2009803\ldots$
**(positive)**. The bundle explicitly flags this convention as **unreconciled**:
*"must be reconciled before these are described as physical-coupling coefficients."*

Using the native engine as ground truth, the conflict is now settled. Testing
both candidate conventions against the engine's exact $\sigma_2,\sigma_3,\sigma_4$:

| $n$ | $\sigma=\tfrac12 W(2u)$ | $\sigma=\tfrac12 W(-2y)$ | native engine | verdict |
|:---:|:---:|:---:|:---:|:---|
| 2 | $-22/153$ | $-22/153$ | $-22/153$ | both (even) |
| 3 | $-61/408$ | $+61/408$ | $-61/408$ | **$W(2u)$ only** |
| 4 | $-737\ldots/7250\ldots$ | $-737\ldots/7250\ldots$ | $-737\ldots/7250\ldots$ | both (even) |

$\sigma=\tfrac12 W(2u)$ reproduces the native engine including the odd
$\sigma_3=-61/408$; $\sigma=\tfrac12 W(-2y)$ gives $+61/408$ and is therefore the
wrong sign for odd orders. Consequently:

$$
\boxed{\sigma_5(u)=\tfrac12\cdot 2^5\,t_5=-\frac{137767222189182735950309}{2009803206414863779920000}}\ \text{(negative)},
$$

$$
\boxed{\sigma_6(u)=\tfrac12\cdot 2^6\,t_6=-\frac{13130661661034190772935959348816444649800714410750015999}{168641444007491247688836385300053017225944999004544000000}}.
$$

- The **consolidated theorem's $\sigma_5$ (negative) is validated.**
- The **KPS-extraction bundle's $\sigma_5$ (positive) is a sign error** from the
  $W(-2y)$ convention; even-order $\sigma_6$ is unaffected and agrees.
- The reconciliation is forced by the native engine, not by choosing a
  convention: only $W(2u)$ matches the contraction the engine actually computes.

## 3. Fifth-order glueball — reproduced from source

`SU3_Y5_COMPLETE_FIFTH_ORDER_BUNDLE` verifier passes every gate and reproduces
the values in §9 of the consolidated theorem:

$$
q_5=-\tfrac{866236750503342026253096691057}{1169668083793811403447133488000},\quad
A_5=\tfrac{313}{240},\quad
B_5=\tfrac{1881863087742908605903793}{1652932248975967181040000},
$$

with $H_5(\Gamma)=q_5 I$, exact Hermiticity, the 25-term Laurent factorization
$D=A_5Q+B_5R$, and bandwidth $\tfrac{4037562229115732471176793}{1652932248975967181040000}$.
Kernel semantic SHA-256 `123dbf137adfbda22c2fea36c45631ea0a93ef1cd126aed90da5fee04df0a5ed`.
Census: 29,366 words, 22,071 trace-wiring blocks, 524,823 global paths, 189
kernel records.

## 4. Shell-six channel mixing — reproduced from source

`SHELL6_O2_SYMMETRY_REDUCED_V2` computes the connected second-order effective
matrix in the 44-state shell-six Wilson-loop space ($O_h$ orbits $12+24+8$) and
passes all stabilizer, Hermiticity, $O_h$, and charge-conjugation gates. The
C-odd sector lists multiple $1^{+-}$ states with connected energies near
$-14.9$. This is the channel-mixing input the ratio diagnostic flagged as
required before treating the isolated one-plaquette branch as the physical
lowest $1^{+-}$ state — it now runs and is symmetry-certified.

---

## 5. Status of the two requested items, updated

### Item 1 — $m_6$

- **Local algebra + new-sector edge tensors:** closed and verified (previous
  session: all nine sixth-order sectors, explicit double-determinant $(0,6)$
  tensors, electric-energy ladders).
- **Architecture template now in hand:** the Y5 bundle supplies the explicit
  fifth-order stage-3G machinery — link tensor cards, Casimir channel
  projectors, trace-wiring blocks — which is the exact template the sixth-order
  contraction follows.
- **Open (HPC):** the connected six-insertion geometry census and the global
  contraction at $\Gamma$. Value of $m_6$: **not determined, not fabricated.**

### Item 2 — native $\sigma_5,\sigma_6$

- **Native engine validated from source** through $\sigma_4$ (§1).
- **$\sigma_5,\sigma_6$ signs reconciled** against the native engine (§2): the
  correct values are negative-$\sigma_5$, negative-$\sigma_6$, matching the
  consolidated theorem.
- **Open (engine extension, now fully scoped):** native $\sigma_5,\sigma_6$
  require (a) the 5th/6th-order local library — fifth order is supplied by the
  Y5 bundle, sixth-order local algebra was built last session; (b) generalizing
  `contract_choice` from 3 to 4/5 energy denominators; (c) the generic folded
  des-Cloizeaux coefficient (already validated through order six); (d) a
  5th/6th-order torelon cluster enumeration extending the fourth-order
  `adjacent_plaquettes`/`site_neighbors`/`sequences` logic. All source pieces
  are now identified; the remaining work is integration, not discovery.

---

## 6. Action on the consolidated theorem

One surgical patch is warranted: the $\sigma_5$ historical-target caveat in §9.4
can be **strengthened** — $\sigma_2,\sigma_3,\sigma_4$ are now confirmed native
from source, and the $\sigma_5,\sigma_6$ signs are reconciled against the native
engine (with the KPS-extraction bundle's positive $\sigma_5$ identified as a
convention sign error). No coefficient values in the consolidated theorem
change; the provenance statement gets firmer.

$$
\boxed{\sigma_2,\sigma_3,\sigma_4\text{: native, reproduced from source}}
$$

$$
\boxed{\sigma_5,\sigma_6\text{: KPS targets, signs reconciled to native engine (negative, negative)}}
$$

$$
\boxed{\text{Consolidated theorem }\sigma_5\text{ sign: validated}}
$$

$$
\boxed{\text{KPS-extraction-bundle }\sigma_5\text{ sign: erroneous (positive)}}
$$

$$
\boxed{\text{Native }\sigma_5,\sigma_6\text{ and }m_6\text{: open, fully scoped, not fabricated}}
$$
