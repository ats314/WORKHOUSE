    % ============================================================
    \section{The \texorpdfstring{\(\SU(3)\)}{SU(3)} Three-Term Local Gap}
    \label{sec:su3-three-term-local-gap}
    % ============================================================

    This section computes the local \(\SU(3)\) one-plaquette class-sector gap
    through order \(\beta^{-1/2}\).  The computation is finite: only the
    Weyl-invariant polynomial sector through degree six is needed.

    \subsection{Weyl-invariant shell basis through degree six}

    The local invariant ring is
    \[
    \mathbb R[x,y]^{S_3}
    =
    \mathbb R[p_2,p_3],
    \qquad
    \deg p_2=2,
    \qquad
    \deg p_3=3.
    \]
    Through degree six, a convenient raw invariant list is
    \begin{equation}
    \mathcal B_{\le6}
    =
    \{1,\ p_2,\ p_3,\ p_2^2,\ p_2p_3,\ p_2^3,\ p_3^2\}.
    \label{eq:su3-raw-basis-degree-six}
    \end{equation}
    The local inner product is the Weyl--Gaussian one
    \[
    \langle f,g\rangle_W
    =
    \int_{\mathbb R^2}
    f(x,y)g(x,y)
    \left(\frac12p_2^3-3p_3^2\right)
    e^{-p_2}
    \,dx\,dy.
    \]
    After Gram--Schmidt, the invariant sector decomposes into shell degrees
    \[
    0,\ 2,\ 3,\ 4,\ 5,\ 6,\ 6.
    \]
    We denote the normalized shell representatives by
    \[
    \psi_0,\psi_1,\psi_2,\psi_3,\psi_4,\psi_5,\psi_6,
    \]
    where \(\psi_0\) is the ground state and \(\psi_1\) is the first
    charge-conjugation-even class excitation.  The states \(\psi_0,\psi_1,\psi_3,\psi_5\)
    belong to the radial Laguerre tower, while \(\psi_2,\psi_4,\psi_6\) are
    non-radial channels involving \(p_3\).

    The gap of interest is
    \[
    \Delta_{\SU(3)}(\beta)
    =
    E_1(\beta)-E_0(\beta),
    \]
    where \(E_0(\beta)\) and \(E_1(\beta)\) are the two lowest eigenvalues in the
    real class sector.

    \subsection{Rayleigh--Schrödinger expansion}

    The scaled Hamiltonian has the form
    \[
    H_\beta
    =
    \beta^{1/2}H_0
    +
    H_1
    +
    \beta^{-1/2}H_2
    +
    O(\beta^{-1}),
    \]
    where
    \[
    H_1
    =
    -\frac{p_2^2}{96},
    \qquad
    H_2
    =
    \sqrt6
    \left(
    \frac{p_2^3}{11520}
    +
    \frac{p_3^2}{8640}
    \right).
    \]
    For a nondegenerate low eigenstate \(\psi_a\), the local perturbation expansion is
    \[
    E_a(\beta)
    =
    \beta^{1/2}E_a^{(0)}
    +
    E_a^{(1)}
    +
    \beta^{-1/2}E_a^{(2)}
    +
    O(\beta^{-1}),
    \]
    with
    \begin{equation}
    E_a^{(1)}
    =
    \langle \psi_a,H_1\psi_a\rangle_W
    \label{eq:su3-first-order-energy}
    \end{equation}
    and
    \begin{equation}
    E_a^{(2)}
    =
    \langle \psi_a,H_2\psi_a\rangle_W
    +
    \sum_{b\ne a}
    \frac{
    |\langle \psi_b,H_1\psi_a\rangle_W|^2
    }{
    E_a^{(0)}-E_b^{(0)}
    }.
    \label{eq:su3-second-order-energy}
    \end{equation}
    Since \(H_1\) has degree four, and the two source states lie in shells \(0\)
    and \(2\), the second-order \(H_1\)-resolvent contribution to the gap is
    captured by the finite degree-six shell space.

    \subsection{Order \texorpdfstring{\(\beta^{1/2}\)}{beta\^1/2}}

    The unperturbed shell energies are
    \[
    E_s^{(0)}
    =
    \frac{\sqrt6}{6}s+\mathrm{const}.
    \]
    The first nontrivial class excitation has shell \(s=2\).  Hence
    \[
    E_1^{(0)}-E_0^{(0)}
    =
    \frac{\sqrt6}{3}
    =
    \sqrt{\frac23}.
    \]
    Therefore the leading term of the compact one-plaquette class gap is
    \begin{equation}
    \Delta_{\SU(3)}(\beta)
    =
    \sqrt{\frac{2\beta}{3}}
    +
    O(1).
    \label{eq:su3-leading-local-gap}
    \end{equation}

    \subsection{Order \texorpdfstring{\(\beta^0\)}{beta\^0}}

    At order \(\beta^0\), only the diagonal \(H_1\) matrix elements contribute:
    \[
    c_0
    =
    \langle \psi_1,H_1\psi_1\rangle_W
    -
    \langle \psi_0,H_1\psi_0\rangle_W.
    \]
    Since \(H_1=-p_2^2/96\) is radial, the computation reduces to the radial
    Laguerre sector.  In the \(\SU(3)\) Weyl--Gaussian measure, the radial variable
    \(u=p_2\) has Gamma shape \(A=4\), and the first two radial states may be taken as
    \[
    e_0=1,
    \qquad
    e_1=\frac{u-4}{2}.
    \]
    The required moment difference is
    \[
    \langle e_1,u^2e_1\rangle
    -
    \langle e_0,u^2e_0\rangle
    =
    30.
    \]
    Therefore
    \begin{equation}
    c_0
    =
    -\frac1{96}\cdot 30
    =
    -\frac5{16}.
    \label{eq:su3-c0}
    \end{equation}

    \subsection{Order \texorpdfstring{\(\beta^{-1/2}\)}{beta\^-1/2}: direct \texorpdfstring{\(H_2\)}{H2} term}

    The direct order-\(\beta^{-1/2}\) contribution is
    \[
    c_{1,H_2}
    =
    \langle \psi_1,H_2\psi_1\rangle_W
    -
    \langle \psi_0,H_2\psi_0\rangle_W.
    \]
    Using
    \[
    H_2
    =
    \sqrt6
    \left(
    \frac{p_2^3}{11520}
    +
    \frac{p_3^2}{8640}
    \right),
    \]
    this splits into a radial part and a rank-two angular part:
    \[
    c_{1,H_2}
    =
    c_{1,H_2}^{\mathrm{rad}}
    +
    c_{1,H_2}^{p_3^2}.
    \]
    The radial contribution is
    \[
    c_{1,H_2}^{\mathrm{rad}}
    =
    \frac{\sqrt6}{32}
    =
    \frac{288\sqrt6}{9216},
    \]
    while the non-radial degree-six contribution is
    \[
    c_{1,H_2}^{p_3^2}
    =
    \frac{\sqrt6}{576}
    =
    \frac{16\sqrt6}{9216}.
    \]
    Thus
    \begin{equation}
    c_{1,H_2}
    =
    \frac{19\sqrt6}{576}
    =
    \frac{304\sqrt6}{9216}.
    \label{eq:su3-direct-H2}
    \end{equation}

    The term \(c_{1,H_2}^{p_3^2}\) is the rank-two Weyl correction.  It is absent
    from any purely radial computation.

    \subsection{Order \texorpdfstring{\(\beta^{-1/2}\)}{beta\^-1/2}: second-order \texorpdfstring{\(H_1\)}{H1} resolvent term}

    The second contribution at order \(\beta^{-1/2}\) is the reduced-resolvent
    term generated by \(H_1\):
    \[
    c_{1,\mathrm{res}}
    =
    \sum_{b\ne1}
    \frac{
    |\langle \psi_b,H_1\psi_1\rangle_W|^2
    }{
    E_1^{(0)}-E_b^{(0)}
    }
    -
    \sum_{b\ne0}
    \frac{
    |\langle \psi_b,H_1\psi_0\rangle_W|^2
    }{
    E_0^{(0)}-E_b^{(0)}
    }.
    \]
    Since \(H_1=-p_2^2/96\), this term is radial.  The active radial shells are
    \(0,2,4,6\), and the finite Rayleigh--Schrödinger contraction gives
    \begin{equation}
    c_{1,\mathrm{res}}
    =
    -\frac{205\sqrt6}{3072}
    =
    -\frac{615\sqrt6}{9216}.
    \label{eq:su3-resolvent}
    \end{equation}
    This is the complete second-order \(H_1\)-resolvent contribution to the
    \(\SU(3)\) local class gap through degree six.

    \subsection{Assembly}

    Combining \eqref{eq:su3-direct-H2} and \eqref{eq:su3-resolvent},
    \[
    c_1
    =
    c_{1,H_2}
    +
    c_{1,\mathrm{res}}
    =
    \frac{304\sqrt6}{9216}
    -
    \frac{615\sqrt6}{9216}
    =
    -\frac{311\sqrt6}{9216}.
    \]
    Therefore:

    \begin{theorem}[\(\SU(3)\) local one-plaquette class gap]
    The local charge-conjugation-even class-sector gap of the compact
    one-plaquette \(\SU(3)\) Wilson Hamiltonian satisfies
    \begin{equation}
    \boxed{
    \Delta_{\SU(3)}(\beta)
    =
    \sqrt{\frac{2\beta}{3}}
    -
    \frac5{16}
    -
    \frac{311\sqrt6}{9216}\,\beta^{-1/2}
    +
    O(\beta^{-1}).
    }
    \label{eq:su3-main-gap-theorem}
    \end{equation}
    \end{theorem}

    \begin{proof}
    The leading term is \eqref{eq:su3-leading-local-gap}.  The order-\(\beta^0\)
    term is \eqref{eq:su3-c0}.  The order-\(\beta^{-1/2}\) term is the sum of the
    direct \(H_2\) contribution \eqref{eq:su3-direct-H2} and the second-order
    \(H_1\)-resolvent contribution \eqref{eq:su3-resolvent}.  This gives the
    displayed expansion.
    \end{proof}

    \subsection{Radial comparison}

    If the angular \(p_3^2\) term in \(H_2\) is dropped, then
    \[
    c_{1,H_2}^{\mathrm{rad}}
    =
    \frac{\sqrt6}{32}
    =
    \frac{288\sqrt6}{9216}.
    \]
    Keeping the same radial \(H_1\)-resolvent term gives
    \[
    c_1^{\mathrm{rad}}
    =
    \frac{288\sqrt6}{9216}
    -
    \frac{615\sqrt6}{9216}
    =
    -\frac{327\sqrt6}{9216}.
    \]
    The full Weyl-invariant result differs by
    \begin{equation}
    c_1-c_1^{\mathrm{rad}}
    =
    -\frac{311\sqrt6}{9216}
    +
    \frac{327\sqrt6}{9216}
    =
    \frac{\sqrt6}{576}.
    \label{eq:su3-rank-two-correction}
    \end{equation}
    Thus the third coefficient is not determined by the radial Laguerre sector.
    The degree-six invariant \(p_3^2\) shifts the local gap by the exact amount
    \(\sqrt6/576\).
