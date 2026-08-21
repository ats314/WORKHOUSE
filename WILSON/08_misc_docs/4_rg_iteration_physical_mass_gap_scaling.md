# RG Iteration and Physical Mass Gap Scaling (Correct \(L^2\) Bookkeeping)

This module is the **scale-keeping** part: it transports the fixed-cutoff gap mechanism
along a dyadic RG trajectory and shows that the **physical** gap stays bounded below as \(a\to 0\).

The key point is the **\(L^2\) scaling factor**: when you iterate Poincaré constants across a dyadic block map,
a factor \(4\) (not \(2\)) appears.

---

## 1. Dyadic scales and objects

Let \(\{a_n\}_{n=0}^N\) be dyadic lattice spacings with
\[
a_{n+1}=2a_n,\qquad a_N=a_{\mathrm{phys}}\ \ (\text{fixed}).
\]

At each scale \(a_n\), let \(\mu_n\) be the Wilson \(\mathrm{SU}(2)\) Gibbs measure on a lattice with spacing \(a_n\),
and let \(C_P^{(n)}\) denote the **fine-scale global Poincaré constant** normalized at scale \(a_n\), i.e.
\[
\mathrm{Var}_{\mu_n}(f)
\le
C_P^{(n)}\int |\nabla f|^2\,d\mu_n,
\]
where the gradient is taken with respect to the product bi-invariant metric at spacing \(a_n\).

Let \(H_{a_n}\) denote the Osterwalder–Schrader reconstructed Hamiltonian at cutoff \(a_n\),
and \(\mathrm{gap}(H_{a_n})\) its spectral gap above the vacuum.

---

## 2. The one-step RG Poincaré recursion (assumption)

Assume there is a block map \(\pi_n\) from the fine configuration space at scale \(a_n\)
to the coarse configuration space at scale \(a_{n+1}\), and constants
\(C_{\mathrm{RG}}\le 1\) and \(C_{\mathrm{block}}<\infty\) (independent of \(n\)) such that:

### (RG) One-step inequality (fine-scale form)
\[
\boxed{
C_P^{(n)}
\ \le\
4\,C_{\mathrm{RG}}\,C_P^{(n+1)}
\;+\;
C_{\mathrm{block}} .
}
\tag{RG}
\]

**Where does the factor \(4\) come from?**  
A dyadic block map halves linear scale, so a coarse observable \(F\) satisfies
\(|\nabla (F\circ\pi_n)| \lesssim 2^{-1}|\nabla F|\circ\pi_n\).
Squaring gives a \(2^{-2}=1/4\) factor in the Dirichlet form, hence a \(4\) in the Poincaré constant.

### Coarse anchor
Assume at the coarsest scale \(n=N\),
\[
C_P^{(N)}\le C_{\mathrm{init}}(a_{\mathrm{phys}}),
\tag{A}
\]
depending only on the fixed physical volume.

---

## 3. Solve the recursion (no heuristics)

Iterate (RG) from \(n\) to \(N\):
\[
C_P^{(n)}
\le
(4C_{\mathrm{RG}})^{N-n} C_P^{(N)}
\;+\;
C_{\mathrm{block}} \sum_{k=0}^{N-n-1}(4C_{\mathrm{RG}})^k.
\tag{3.1}
\]

Since \(C_{\mathrm{RG}}\le 1\),
\[
C_P^{(n)}
\le
4^{N-n} C_P^{(N)}
\;+\;
C_{\mathrm{block}}\frac{4^{N-n}-1}{3}
\le
K\,4^{N-n},
\tag{3.2}
\]
where
\[
K:=C_{\mathrm{init}}(a_{\mathrm{phys}})+\frac13\,C_{\mathrm{block}}.
\]

Now use the dyadic relation \(a_N=2^{N-n}a_n\), so
\[
4^{N-n}=\left(2^{N-n}\right)^2=\left(\frac{a_N}{a_n}\right)^2=\left(\frac{a_{\mathrm{phys}}}{a_n}\right)^2.
\tag{3.3}
\]

Therefore
\[
\boxed{
C_P^{(n)} \ \le\ K\,\frac{a_{\mathrm{phys}}^2}{a_n^2}.
}
\tag{3.4}
\]

This is the correct scale-explicit bound: \(C_P^{(n)}\) grows like \(a_n^{-2}\) as \(a_n\to 0\).

---

## 4. Lattice gap scaling and physical gap permanence

The fixed-cutoff analysis yields a relationship between the *dimensionless* lattice decay rate \(\eta(a)\)
and the Poincaré constant:
\[
\eta(a_n)\ \asymp\ \frac{1}{\sqrt{C_P^{(n)}}}.
\tag{4.1}
\]
(Here \(\asymp\) means “bounded above and below by fixed multiples,” coming from the localization/Helffer–Sj\"ostrand/Combes–Thomas chain.)

Insert (3.4) into (4.1):
\[
\eta(a_n)\ \gtrsim\ \frac{a_n}{a_{\mathrm{phys}}\sqrt{K}}.
\tag{4.2}
\]

Finally, OS reconstruction relates the physical Hamiltonian gap to the dimensionless rate by
\[
\mathrm{gap}(H_{a_n})=\frac{\eta(a_n)}{a_n}.
\tag{4.3}
\]

Combining (4.2) and (4.3) gives the uniform lower bound
\[
\boxed{
\mathrm{gap}(H_{a_n})
\ \ge\
m_0
:=
\frac{1}{a_{\mathrm{phys}}\sqrt{K}}
\ >\ 0,
\qquad\text{for all }n.
}
\tag{4.4}
\]

So the **UV cancels in physical units**: as \(a_n\to 0\) at fixed \(a_{\mathrm{phys}}\),
the physical gap remains strictly positive.

---

## 5. Remarks (what this does and does not prove)

- This module is purely an **iteration/normalization** result: it does not generate the one-step inequality (RG);
  it tells you exactly what (RG) buys you once obtained.
- No super-contraction is needed: \(C_{\mathrm{RG}}\le 1\) suffices.
- The output is “continuum-stable in physical units,” but it is not a full continuum limit construction;
  OS existence in the limit is an external (hard) step.

