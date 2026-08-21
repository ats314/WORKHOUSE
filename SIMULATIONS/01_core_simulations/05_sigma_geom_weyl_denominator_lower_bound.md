---
title: "A concrete \u03c3\_geom: Weyl-denominator convexity on the conjugacy-class orbit space"
date: "2025-12-28"
project: "SIMULATIONS"
---

> **Purpose.** This note gives a *fully explicit* and *fully positive* lower bound for a geometric source term
> \(\sigma_{\rm geom}\) on a clean orbit space: the space of conjugacy classes \(SU(N)/\!\operatorname{Ad}SU(N)\).
> 
> The computation is intended as a template for the lattice gauge-orbit space, where analogous
> Weyl/FP determinants appear once one reduces to gauge-invariant variables.

## 1. The toy orbit space and its intrinsic Jacobian

Let \(G=SU(N)\) with Haar measure \(dg\).
Consider the **orbit space** of conjugation (adjoint) action,
\[
  G/\!\operatorname{Ad}G \;\cong\; T/W,
\]
where \(T\) is a maximal torus and \(W\) the Weyl group.

For **class functions** \(f(g)=f(hgh^{-1})\), Weyl's integration formula gives
\[
  \int_G f(g)\,dg
  = \frac{1}{|W|}\int_T f(t)\,|\Delta(t)|^2\,dt,
\]
where \(dt\) is normalized Haar measure on \(T\) and \(\Delta\) is the Weyl denominator.

Writing \(t=\mathrm{diag}(e^{i\theta_1},\dots,e^{i\theta_N})\) with \(\sum_i\theta_i\equiv 0\pmod{2\pi}\), one has
\[
  |\Delta(e^{i\theta})|^2
  = \prod_{1\le i<j\le N}\big|e^{i\theta_i}-e^{i\theta_j}\big|^2
  = \prod_{i<j} 4\sin^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big).
\]

So the **orbit-space measure density** on \(T/W\) contains the factor
\[
  w(\theta) := \prod_{i<j} 4\sin^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big).
\]
Define the associated **geometric potential**
\[
  S_{\rm geom}(\theta) := -\log w(\theta)
  = -\sum_{i<j}\log\Big(4\sin^2\!\frac{\theta_i-\theta_j}{2}\Big).
\]
The **reducible locus** (non-regular elements) corresponds to eigenvalue collisions \(\theta_i=\theta_j\), i.e.
\(\sin((\theta_i-\theta_j)/2)=0\), where \(S_{\rm geom}\to +\infty\).

## 2. Hessian of \(S_{\rm geom}\) is a weighted graph Laplacian

Set
\[
  w_{ij}(\theta) := \csc^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big)\quad (i\ne j).
\]
Note \(w_{ij}(\theta)\ge 1\) everywhere it is finite, since \(\sin^2\le 1\).

A direct derivative computation gives the Hessian entries (for \(i\ne j\)):
\[
  \frac{\partial^2 S_{\rm geom}}{\partial\theta_i\partial\theta_j}
  = -\frac12\,w_{ij}(\theta),
  \qquad
  \frac{\partial^2 S_{\rm geom}}{\partial\theta_i^2}
  = \frac12\sum_{k\ne i} w_{ik}(\theta).
\]
So
\[
  \nabla^2 S_{\rm geom}(\theta)\;=\;\frac12\,L_{w(\theta)},
\]
where \(L_{w(\theta)}\) is the **weighted Laplacian of the complete graph** on \(\{1,\dots,N\}\) with edge weights \(w_{ij}(\theta)\).

Equivalently, for any vector \(x\in\mathbb R^N\),
\[
  x^\top\,\nabla^2 S_{\rm geom}(\theta)\,x
  = \frac14\sum_{i<j} w_{ij}(\theta)\,(x_i-x_j)^2.
\]

## 3. Uniform positive lower bound on the SU(N) constraint hyperplane

For \(SU(N)\), the eigenangles satisfy \(\sum_i\theta_i=0\) (mod \(2\pi\)).
Thus tangent vectors satisfy \(\sum_i x_i=0\).

Using \(w_{ij}(\theta)\ge 1\), we get
\[
  x^\top\,\nabla^2 S_{\rm geom}(\theta)\,x
  \ge \frac14\sum_{i<j} (x_i-x_j)^2.
\]
Now use the identity
\[
  \sum_{i<j}(x_i-x_j)^2
  = N\sum_{i=1}^N x_i^2 - \Big(\sum_{i=1}^N x_i\Big)^2.
\]
On the hyperplane \(\sum_i x_i=0\), this becomes
\[
  \sum_{i<j}(x_i-x_j)^2 = N\sum_i x_i^2.
\]
Therefore, for all \(x\) with \(\sum_i x_i=0\),
\[
  x^\top\,\nabla^2 S_{\rm geom}(\theta)\,x
  \ge \frac{N}{4}\,\|x\|^2.
\]

### Conclusion (explicit \u03c3\_geom)

On the regular part of the conjugacy-class orbit space \(SU(N)/\!\operatorname{Ad}SU(N)\), the geometric potential satisfies the *uniform convexity bound*
\[
  \nabla^2 S_{\rm geom}\big|_{\sum x_i=0}\;\ge\;\frac{N}{4}\,I.
\]
So one may take the **strictly positive source**
\[
  \boxed{\;\sigma_{\rm geom} \;:=\; \frac{N}{4}\;>0\;}
\]
(in the Euclidean metric on eigenangles).

For \(SU(2)\) this yields \(\sigma_{\rm geom}=\tfrac12\), consistent with
\(S_{\rm geom}(\theta)=-\log(4\sin^2(\theta/2))\) and \(S_{\rm geom}''(\theta)=\tfrac12\csc^2(\theta/2)\ge\tfrac12\).

## 4. Why this matters for the lattice orbit space

The key features are robust:

1. **Irreducibles \u2194 regular elements.** The boundary of the Weyl chamber (eigenvalue collisions) is precisely where stabilizers enlarge.

2. **The Jacobian is geometric.** The Weyl denominator comes from quotienting by the adjoint action, i.e. from orbit-space geometry, not from the Wilson action.

3. **Hessian is a Laplacian.** The convexity is ultimately the convexity of a complete-graph Laplacian with weights \(\ge 1\). This is a very strong, nonperturbative convexity mechanism.

The lattice gauge-orbit space is more complicated than a direct conjugacy-class quotient, but any reduction to gauge-invariant holonomy eigenangles (plaquettes/blocks) generically produces analogous Weyl/FP determinants.
Those determinants are the natural candidates for a continuum-surviving \(\sigma_{\rm geom}\): they are built from group topology and orbit-volume collapse near reducibles.

