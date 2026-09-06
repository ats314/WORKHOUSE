# Independent review of the literal-vacuum projection and intrinsic score

5 September 2026. Outputs-only mathematical audit; current canonical proof,
run, native code and graph bytes are not changed by these experiments.

Accepted source snapshots:

- `../LITERAL_VACUUM_COARSE_PROJECTION.md`, SHA256
  `3e64cf53600a4e07805f4e3e9c5911cc49a1a7f807b810ba7d4760a5f8bb9b55`.
- `../GROUND_MARGINAL_SCHUR_SCORE.md`, SHA256
  `8070371a611bfad5036824ff0c910fa4a57fc21a467d566cd889513397beff25`.

## 1. Actual literal-vacuum result

The literal projection proof is accepted at its stated actual fixed-strip,
fixed-rank scope. Its retained vector is the true full ground times a coarse
class function. The smooth positive marginal supplies the weighted isometry
and preserves the Sobolev domain at each fixed u; no uniform lower bound on
the marginal is required for the asymptotic approximation.

The bounded coarse cutoff is essential. For fixed R, its operator norm is
uniform in u, so harmonic L2 convergence of the full vacuum may be multiplied
by it. Only afterwards may R grow. This proves leakage of the entire simple
first excited physical state into Q tends to zero without passing an
unbounded polynomial through an L2 limit. Exact vacuum inclusion removes the
other low-space leakage. The complete physical spectral decomposition then
gives the refined floor b-(b-a)delta^2. It is a lower bound, not a claimed
compression asymptotic equality.

The fixed-u Schur argument is also valid. Haar differentiation of fiber
orthogonality and one coarse integration by parts eliminate the derivative
of the retained input. Smooth fixed-u coefficients and positive marginal
give the required L2-to-complement-form bound; ellipticity and the proved
positive floor identify the complementary form norm with H1. Bounded form
subtraction, the triangular domain and the vacuum kernel are consequently
the actual ones. The lift kills the true vacuum exactly.

For independent copies with independent Gauss constraints, Q applied to
different single excitations gives orthogonal vectors of norm delta. This
is why the complete low-window leakage stays delta independently of copy
count. The countable vacuum tensor product has a dense finite-excitation
form core; applying its limiting Q stays within a finite product form domain.
The infinite-rank frame uses positivity of B B*, which proves surjectivity.
This accepts the independent-product conclusion without adding shared Gauss,
ambient interactions or identifying the equal-time range with all histories.

## 2. Intrinsic score identity and the coefficient

Write nu=mu(U)rho_U(K), and use the actual completed-square horizontal field
D_a=partial_a+b_a.grad_K. Differentiating E_U g=0 and performing fiber Haar
integration by parts gives

    E_U D_a g = -E_U(g s_a),
    s_a=partial_a log rho_U + div_K(rho_U b_a)/rho_U.

Its mean is zero. Both parts of div(rho b), including div b, are necessary.
Since A depends only on U, the retained-fine cross form is exactly

    h[f,g]=-(1/2) integral (grad f)* A E_U(g s) dmu.

The original full ground-state equation removes the potential and full
vacuum energy together. A conditional rotor ground or Gibbs density cannot
be substituted in this formula.

For I=E(s s*), the Fisher hypothesis A^(1/2) I A^(1/2)<=2 eta w I implies

    |A^(1/2)E(gs)|^2 <= 2 eta w E|g|^2.

This follows by taking the supremum over unit covectors in the conditional
Cauchy-Schwarz inequality. Summing individual coordinate bounds would
introduce an unnecessary dimension factor; the operator-norm proof does not.
The 1/2 in the cross form, followed by the fact that a[f] is one half of the
coarse gradient integral, yields precisely

    |h[f,g]|^2 <= eta a[f] integral w E|g|^2 <= eta a[f] h[g].

Riesz on the complementary form space therefore gives the stated Schur
loss eta on the retained form domain. This alone gives no bounded lift on
retained L2. The source correctly separates that stronger domain statement.

## 3. Full gap, sharpness and conditional weighted target

For a mean-zero total vector, its conditional mean is marginal mean-zero.
Writing x=sqrt(a[f]), y=sqrt(h[g]) gives the two exact scalar inequalities

    h[f+g]>=x^2+y^2-2sqrt(eta)xy,
    ||f+g||^2<=x^2/alpha+y^2/f0.

The smaller generalized eigenvalue is

    (alpha+f0-sqrt((alpha-f0)^2+4 eta alpha f0))/2.

It is positive for eta<1 and is attained by an abstract two-state form. No
operator-domain multiplication or L2-bounded lift is required for this direct
gap argument. The constant Fisher version substitutes eta=beta/(2f0), giving
the displayed coefficient 2 alpha beta under the square root.

The final Wilson pair of inequalities is correctly conditional. If it were
proved with uniform positive constants, one could choose

    2 eta = max(C0/c0,C1/c1)/sqrt(u)

as a sufficient bound. This is the ratio of the actual score covariance to
the vacuum-subtracted full complementary energy weight, not a claim about a
global conditional rotor gap. No such uniform Wilson Fisher or weighted
full-complement estimate is proved by the present audit or controls.

## 4. Independent exact controls

`check_ground_marginal_score.py` passed four control families. Its final
saved payload is `ground_marginal_score_controls_final.json` (SHA256
`06e28aa4b6ffbe01de468c2985cc9725c9692af79a83c4ae3ee5948d0a9d7289`).
The source SHA256 is
`18d965bec7edbb123b35c10354f0cb3839f40246528ead27acc3941f2ad6f770`.
The earlier unsuffixed JSON is a draft snapshot before the source's purely
structural sorting change; use the final payload for source-matched replay.

- A noncommuting two-dimensional metric/Fisher pair has
  A=[[2,1],[1,2]], I=diag(1,2), Fisher eigenvalues 3+-sqrt(3), and cap 6.
  The positive congruence slack 6A^-1-I=[[3,-2],[-2,2]] verifies that cap
  without diagonalizing both factors. A four-point centered score and an
  explicit g give cross^2=49 versus the correct upper bound 63.
- A compact two-torus example has conditional density 1+cos(y)/2, connection
  b=(2+cos(x))sin(y), A=S=1 and full metric determinant one. Its true positive
  ground may be chosen proportional to the square root of this density by
  setting V=(div(C grad Omega))/(2 Omega). The ground transform is then
  nonnegative and has the stated ground. For g=cos(y)-1/4 and f=sin(x), the
  direct kinetic and score cross forms both equal -1/8. The score correlation
  is (2+cos(x))/2; retaining only div b gives 7(2+cos(x))/16, and retaining
  only b.grad log rho gives (2+cos(x))/16. Each omission is rejected exactly.
- The energy matrix [[4,-3],[-3,9]] attains the gap
  (13-sqrt(61))/2 at alpha=4, f0=9, eta=1/4. An exact eigenvector verifies
  equality. Changing the Fisher factor to the smaller unjustified value
  produces a negative determinant for H-Delta_wrong I. The normalized Schur
  energy 27/10 separately obeys the earlier f mu/(f+mu) sandwich.
- A nonconstant positive weight and score ratio give the exact inverse-sqrt(u)
  majorant, including equality of the constant branch at v=0.

These finite and compact-example calculations test the mechanism and its
failure boundaries. They do not machine-certify the general elliptic or
spectral arguments, nor provide the open Wilson uniform hypotheses.

Reproduce with the repository's declared SymPy dependency and a fresh path:

    python check_ground_marginal_score.py --output fresh-score.json

The script rejects optimized Python and refuses to overwrite evidence.
