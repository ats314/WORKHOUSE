# q-deformed 6j symbols: classical limit and explicit small-$\theta$ error control

## 0. What this layer contributes

This layer is technically independent of the curvature/BE pipeline. It provides a rigorous bound controlling how q-deformed recoupling coefficients approach the classical ones.

Write $q=e^{i\theta}$ with $|\theta|\ll 1$. For spins up to $J_{\max}$, the project derives a polynomial error bound of the form

$$
\big|\{6j\}_q - \{6j\}\big| \le C\,\theta^2\,J_{\max}^{5/2}.
$$

This is the kind of estimate you need if you want to use q-deformation as a regulator and then take $\theta\to 0$ with controlled errors.

---

## 1. Outline of the derivation

The derivation proceeds by:

1. Defining q-integers, q-factorials, and q-triangle coefficients.
2. Writing the q-6j symbol in Racah-sum form (q-Racah formula).
3. Expanding each q-factorial / q-triangle piece in $\theta$.
4. Bounding the Racah sum by controlling its number of terms and the growth of the prefactors.

Two key inputs:

- q-factorials admit expansions with leading corrections $O(\theta^2\,n^3)$.
- classical 6j symbols decay at least like a negative power of $J_{\max}$ (Ponzano–Regge asymptotics for nondegenerate configurations), giving room to improve exponents.

The project notes first obtain a crude exponent $7/2$ and then tighten to $5/2$ by using the expected scaling of the full symbol.

---

## 2. Final bound (as stated in the project appendix)

The appendix states (paraphrased):

- There exists a constant $C$ such that for sufficiently small $|\theta|$ and bounded maximal spin $J_{\max}$,

$$
\big|\{6j\}_q - \{6j\}\big| \le C\,\theta^2\,J_{\max}^{5/2}.
$$

This is the “safe” quantitative statement you can quote.

---

## 3. Numerical scan harness (computational confirmation)

The Colab exports include a JAX/NumPy scan that:

- computes $\{6j\}$ and $\{6j\}_q$ for a symmetric family $\{j\,j\,j;\,j\,j\,j\}$,
- loops over $J_{\max}$ and $\theta$,
- records the maximum absolute error,
- checks scaling vs $\theta^2 J_{\max}^{2.5}$.

A representative scaling diagnostic is the ratio

$$
\text{ratio}(J_{\max},\theta) := \frac{\max\_j |\{6j\}_q - \{6j\}|}{\theta^2 J_{\max}^{2.5}},
$$

which should remain bounded if the exponent $5/2$ is correct.

---

## 4. Where to find the full details

- Full derivation: `YM_Salvage_Stack_Appendix_E_q6j_Classical_Limit_and_Error.txt`
- Full scan code: `COLAB PDF EXPORT.pdf` and `12-2-25 code runs 3.pdf`

This markdown is the “paper-ready” narrative version.
