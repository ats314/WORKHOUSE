    % ============================================================
    \section{Logical Status and Theorem Map}
    \label{sec:logical-status-theorem-map}
    % ============================================================

    This document collects three related but logically distinct parts of the project:
    local one-plaquette class-sector spectral asymptotics, finite-dimensional Wick
    certificates for the fixed-rank \(\SU(N)\) coefficients, and a conditional
    projected-capacity route for global Wilson defect geometry.

    The results are not presented as a proof of the four-dimensional Yang--Mills
    mass gap.  The proven statements in this document are local or finite-dimensional
    unless explicitly marked otherwise.  The projected-capacity part is a conditional
    programmatic route: it identifies the deterministic and probabilistic estimates
    that would be needed to pass from local class-sector control to an infinite-volume
    source-stability theorem.

    The organizing principle is therefore not
    \[
    \text{local gap}
    \Longrightarrow
    \text{Yang--Mills mass gap},
    \]
    but rather
    \[
    \text{local class asymptotics}
    \Longrightarrow
    \text{finite algebraic certificates}
    \Longrightarrow
    \text{conditional global mechanism}.
    \]

    \subsection{Three layers}

    The document is divided into three layers.

    \paragraph{Layer I: Local \(\SU(3)\) one-plaquette class spectrum.}
    The first layer proves the rank-two Weyl correction in the \(\SU(3)\)
    one-plaquette class-sector Hamiltonian
    \[
    H_\beta
    =
    \frac12 C_2
    +
    \beta\left(1-\frac13\Re\chi_{(1,0)}(g)\right).
    \]
    The main theorem is the three-term strong-potential expansion
    \[
    \Delta_{\SU(3)}(\beta)
    =
    \sqrt{\frac{2\beta}{3}}
    -\frac5{16}
    -\frac{311\sqrt6}{9216}\,\beta^{-1/2}
    +
    O(\beta^{-1}).
    \]
    The order-\(\beta^{-1/2}\) coefficient is genuinely rank two.  A radial
    calculation gives
    \[
    c_{1}^{\mathrm{rad}}
    =
    -\frac{327\sqrt6}{9216},
    \]
    whereas the full Weyl-invariant calculation gives
    \[
    c_1
    =
    -\frac{311\sqrt6}{9216}.
    \]
    Thus
    \[
    c_1-c_1^{\mathrm{rad}}
    =
    \frac{\sqrt6}{576},
    \]
    and this discrepancy is exactly the contribution of the \(p_3^2\) term in the
    degree-six Wilson-character expansion.

    The finite leakage matrix attached to the same first-order data is recorded as a
    finite-channel diagnostic only.  It is not asserted to be a full-channel polymer
    constant.  The radial Laguerre tail obstruction explains why the finite matrix
    cannot be promoted without an additional transfer norm, compact-group shell
    estimate, or smoothing mechanism.

    \paragraph{Layer II: Fixed-rank \(\SU(N)\) local class gaps.}
    The second layer gives fixed-rank \(\SU(N)\) local class-sector coefficients in
    the Weyl--Gaussian model.  Throughout this layer, \(N\) is fixed first and
    \(\beta\to\infty\).  No uniform large-\(N\) assertion is made unless explicitly
    stated.

    The charge-conjugation-even local class gap is
    \[
    \Delta_{\SU(N)}^{+}(\beta)
    =
    \sqrt{\frac{2\beta}{N}}
    -\frac{2N^2-3}{16N}
    -\frac{\sqrt2(6N^4-24N^2+41)}{1024N^{3/2}}\,
    \beta^{-1/2}
    +
    O_N(\beta^{-1}).
    \]
    The corresponding charge-conjugation-odd local class gap is
    \[
    \Delta_{\SU(N)}^{-}(\beta)
    =
    \sqrt{\frac{9\beta}{2N}}
    -\frac{3(N^2-3)}{16N}
    -\frac{\sqrt2(14N^4-97N^2+290)}{1536N^{3/2}}\,
    \beta^{-1/2}
    +
    O_N(\beta^{-1}).
    \]
    The odd-sector coefficient
    \[
    -\frac{3(N^2-3)}{16N}
    \]
    is the corrected value.  In particular, the expression
    \[
    -\frac{3(2N^2+1)}{16N}
    \]
    does not belong to the final theorem stack.

    Both fixed-rank formulas are supported by finite Wick certificates in the
    traceless Hermitian Gaussian model with covariance
    \[
    \E[X_{ab}X_{cd}]
    =
    \frac12
    \left(
    \delta_{ad}\delta_{bc}
    -\frac1N\delta_{ab}\delta_{cd}
    \right).
    \]
    The even-sector \(H_1\)-resolvent certificate gives
    \[
    q_{\mathrm{res}}^{(N),+}
    =
    -\frac{34N^4-120N^2+171}{3072N^2},
    \]
    while the odd-sector certificate gives
    \[
    q_-^{(N)}
    =
    -\frac{14N^4-97N^2+290}{1536N^2}.
    \]

    \paragraph{Layer III: Conditional projected-capacity route.}
    The third layer concerns global Wilson defect geometry.  It is not a consequence
    of the local one-plaquette theorems alone.

    The incorrect target is a global fixed-window top-norm firewall of the form
    \[
    \|P_{\Lambda,L}\mathbf 1_{D_L}P_{\Lambda,L}\|
    \le c < 1
    \qquad
    \text{uniformly in }L
    \]
    at fixed positive defect density.  Such a statement is false in large volume:
    rare large defective islands occur somewhere in the box and can force the global
    top norm close to one.

    The viable replacement is rooted.  One studies the bad island connected to a
    fixed root plaquette \(p_0\), weighted by its projected capacity.  The desired
    summability object has the schematic form
    \[
    \sum_{\Gamma\ni p_0}
    \exp\{a|\Gamma|+s\Theta_\Lambda(\Gamma)\}
    \,
    \mathbb P_\beta(\Gamma\subset D_\delta)
    <\infty,
    \]
    where \(\Gamma\) ranges over connected plaquette animals containing \(p_0\).

    The projected-capacity route therefore has the conditional structure
    \[
    \text{inhomogeneous Wilson free-energy stability}
    \Longrightarrow
    \text{hard-defect Peierls bound}
    \Longrightarrow
    \text{rooted projected-capacity summability}
    \Longrightarrow
    \text{source stability}.
    \]
    The open analytic input is the Wilson free-energy stability estimate strong
    enough to support this chain.  Numerical projected-capacity audits are evidence
    and calibration data for this route; they are not substitutes for the missing
    stochastic theorem.

    \subsection{Theorem-status convention}

    Every result below is labeled according to one of the following statuses.

    \begin{center}
    \renewcommand{\arraystretch}{1.35}
    \begin{tabular}{p{0.24\linewidth}p{0.66\linewidth}}
    \toprule
    Status label & Meaning \\
    \midrule
    \textbf{Theorem} &
    A proved statement within the local or finite-dimensional model specified in
    the hypotheses. \\

    \textbf{Finite certificate} &
    An exact finite Wick, Gram, projection, or symbolic computation whose inputs and
    outputs are explicitly stated. \\

    \textbf{Numerical audit} &
    A computational check of a finite truncation, finite lattice, or finite spectral
    window.  It is evidence, not a proof of an infinite-volume theorem. \\

    \textbf{Conditional theorem} &
    A theorem whose conclusion follows once a clearly named analytic hypothesis is
    supplied. \\

    \textbf{Open input} &
    A missing analytic estimate required for the global projected-capacity route. \\
    \bottomrule
    \end{tabular}
    \end{center}

    This convention is part of the mathematical content of the document.  It is used
    to prevent local spectral coefficients, finite-dimensional diagnostics, and
    conditional global mechanisms from being collapsed into a single unsupported
    claim.

    \subsection{What is not claimed}

    This document does not claim that the local one-plaquette class gap is a physical
    glueball mass.  It does not claim a completed infinite-volume Osterwalder--
    Schrader construction.  It does not claim a continuum Yang--Mills mass gap.
    It does not claim that the finite leakage matrix is a full-channel polymer
    constant.  It does not claim that projected-capacity numerics prove the Wilson
    free-energy stability estimate.

    The claim is narrower and sharper: the local class-sector coefficients are
    computed exactly through the displayed orders, the finite Wick certificates
    verify the fixed-rank \(\SU(N)\) formulas, and the projected-capacity mechanism
    has a precise conditional target.
