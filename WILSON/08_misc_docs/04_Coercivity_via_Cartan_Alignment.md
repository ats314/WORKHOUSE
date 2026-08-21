# Coercivity on the rough set via Cartan alignment: a quantitative program (with numerical hunting)

This note extracts the project’s most “new-physics-adjacent” idea:

> In $SU(2)$ lattice gauge theory, **rough curvature cannot have small force** unless the configuration is *essentially abelian* (Cartan-aligned).

The project treats this as the missing ingredient for coercivity on $K^c$ in the fixed-cutoff mass gap argument.

---

## 1. The analytic need: coercivity on $K^c$

Let $S$ be the Wilson action at inverse coupling $\beta$.
The localization strategy introduces a “good set” $K(\varepsilon)$ (small plaquette defects) and needs a **uniform lower bound** on a pairing functional on the complement $K(\varepsilon)^c$.

One representative form (project notation) is:
\[
\mathcal P_\Lambda
\;=\;
\frac12\langle \nabla S,\;\nabla V\rangle,
\qquad
V \;=\;\sum_{p} z_p,
\]
where $z_p$ measures the plaquette defect.
The desired inequality is
\[
\mathcal P_\Lambda \;\ge\; c_\varepsilon\, D
\qquad \text{on } K(\varepsilon)^c,
\quad
D=\sum_p z_p,
\]
with $c_\varepsilon>0$ independent of volume.

This is the “coercivity-on-$K^c$” input.

---

## 2. The local cancellation heuristic

For $SU(2)$, each link $b$ participates in $2(d-1)=6$ plaquettes in $d=4$.
The force at $b$ is a (transported) sum of Lie algebra contributions from these plaquettes.

The heuristic is:

- if the plaquette holonomies around $b$ point in generic directions in $\mathfrak{su}(2)\cong\mathbb R^3$,
  their transported contributions cannot cancel to near zero;

- cancellation is only possible when these contributions are approximately colinear after parallel transport,
  meaning the configuration lies close to a common **$U(1)$ subgroup** (a Cartan subgroup) locally.

### Overdetermination (key “counting” idea)

In $d=4$, the link $b$ lies in **three independent coordinate planes** $(b,\nu)$ with $\nu\neq \mu(b)$.
Each plane imposes an alignment constraint if the two plaquettes in that plane are to cancel at $b$.
That gives roughly **6 scalar constraints**, but the local Lie algebra direction is only **3 degrees of freedom**.
Hence simultaneous cancellations across three planes are generically impossible unless the configuration collapses into a common Cartan direction.

This is the geometric heart of the conjectured lemma.

---

## 3. A quantitative conjecture (clean target statement)

Fix $\varepsilon>0$ and define a rough set $K(\varepsilon)^c$ by requiring the average plaquette defect
\[
B_{\mathrm{avg}} \;=\; \frac{1}{6|\Lambda|}\sum_{p} (1-\tfrac12\mathrm{Tr}\,U_p)
\]
to satisfy $B_{\mathrm{avg}}\ge \varepsilon$.

Define an “alignment score” $A(U)$ measuring how far the link variables are from lying in a common $U(1)$ subgroup.

**Conjecture (Rough $\Rightarrow$ force bounded below away from Cartan).**  
There exist constants $c(\varepsilon,\beta)>0$ and $A_{\min}>0$ such that
\[
B_{\mathrm{avg}}(U)\ge \varepsilon \ \text{and}\ A(U)\ge A_{\min}
\quad\Longrightarrow\quad
\|\nabla S(U)\| \;\ge\; c(\varepsilon,\beta)\,|\Lambda|^{1/2}.
\]

A stronger form would replace the global norm by a localized linkwise coercivity bound.

---

## 4. Numerical evidence via counterexample hunting

The project uses GPU “counterexample hunts” designed to find configurations satisfying

- $B_{\mathrm{avg}}\ge \varepsilon$ (rough),
- alignment score $A(U)\ge A_{\min}$ (not Cartan-ish),
- and small force norm $\|\nabla S\|$ (near stationary).

The observed best hits (in large parallel scans) keep force **very large** even when roughness and nonalignment are enforced,
suggesting coercivity may hold quantitatively.

This is not a proof, but it is exactly the right kind of computation: it tries to *falsify* the lemma.

---

## 5. What would turn this into a theorem

1. **Local transport bookkeeping**:
   express each plaquette’s contribution to the link force in a common tangent space with explicit adjoint transports.

2. **Geometric noncancellation bound**:
   prove that unless the transported plaquette Lie algebra elements are nearly colinear,
   the sum of six vectors in $\mathbb R^3$ has norm bounded below by a function of their magnitudes.

3. **Compactness + stratification**:
   show the set of “near cancellation” configurations is contained in a tubular neighborhood of the Cartan-aligned subset,
   with a uniform quantitative bound.

4. **Integrate with the localization scheme**:
   translate a local force lower bound into the pairing functional lower bound $\mathcal P_\Lambda \ge c_\varepsilon D$.

---

## 6. Why this could be a new theory direction

If true, the lemma is a *rigidity principle*:
nonabelian roughness produces unavoidable restoring force unless the system abelianizes locally.

That is an interesting bridge between:

- nonabelian geometry (Cartan subgroups and adjoint transport),
- coercivity needed for functional inequalities,
- and a physics intuition: “nonabelian disorder resists stationarity unless it collapses to an abelian sector.”
