# Making the dwarf kill-switch pass without “special pleading”

## 0. What the failure mode is (in one line)

The anti-kernel multiplier
\[
M_{\rm anti}(k)=1+\frac{\mu^2}{k^2}
\]
has an **IR pole** at \(k\to 0\). In any finite-data implementation, this pole is only controlled by whatever “effective \(k_{\min}\)” your numerical procedure actually enforces.

That means dwarfs (low-acceleration, small sizes, often low S/N at large radii) are a *diagnostic amplifier* for whether the IR regularization is physical or just a hack.

## 1. Diagnose the blow-up as an IR regularization problem

In your SPARC Hankel code, you already introduce:
- a hard \(k_{\min}\) (or equivalently a floor in the \(k\)-grid), and
- a taper/window \(W(k)\) to suppress ringing/edge artefacts.

That’s good, but it needs to be *theory-driven*.

A “no special pleading” kill-switch is not “turn \(\mu\) off on dwarfs”; it is:

> derive the IR cutoff scale from **finite geometry** and/or **leakage physics** that becomes dominant exactly in low-\(g\) systems.

## 2. Three physically-motivated kill-switch mechanisms

### (A) Finite-disk IR cutoff (geometry, not tuning)

A galaxy of finite radius \(R_{\max}\) cannot support modes with \(k \ll 1/R_{\max}\).

So replace the formal pole by:
\[
\frac{1}{k^2}\quad\longrightarrow\quad \frac{1}{k^2+k_{\rm IR}^2},
\qquad
k_{\rm IR}\sim \frac{c}{R_{\max}},
\]
with \(c=\mathcal{O}(1)\) fixed (not per-galaxy tuned).

Interpretation:
- large galaxies have smaller \(k_{\rm IR}\), so more IR enhancement,
- dwarfs have larger \(k_{\rm IR}\), naturally suppressing the blow-up.

This is *exactly* the kind of “environment dependence” that is really just “finite support”.

### (B) Finite thickness / vertical leakage (a real physical regulator)

A razor-thin disk is the *worst case* for IR pathologies.

For a disk of scale height \(h\), vertical structure introduces an effective smoothing at \(k\lesssim k_z\sim 1/h\).

A very common regulator is:
\[
\frac{1}{k^2}\quad\longrightarrow\quad \frac{1}{k^2+k_z^2},
\qquad
k_z\sim \frac{1}{h}.
\]

In practice you can combine with the finite-radius IR scale:
\[
\frac{1}{k^2}\to \frac{1}{k^2+k_{\rm IR}^2+k_z^2}.
\]

This is attractive because dwarfs are *puffier* (larger \(h/R\)) than big spirals, so it pushes exactly in the right direction.

### (C) External field / environment (EFE-style) regulator

If the modified response depends on a background field (cosmic environment, group potential), you expect a regulator based on an external acceleration scale \(g_{\rm ext}\).

A clean way to encode that *spectrally* is to promote
\[
\mu \;\to\; \mu_{\rm eff}(g_{\rm ext})
\]
or to shift the pole:
\[
\frac{\mu^2}{k^2}\;\to\;\frac{\mu^2}{k^2+k_{\rm ext}^2},
\qquad
k_{\rm ext}\sim \frac{g_{\rm ext}}{v^2_{\rm char}}
\]
where \(v_{\rm char}\) is a characteristic velocity (set once, not per galaxy).

This is the least “closed” of the three options because it requires environment data, but it is theoretically motivated and falsifiable.

## 3. A minimal implementation that is hard to argue with

If you want the simplest patch that is also physically legible, do this:

1. Define \(R_{\max}\) as the last measured radius in the rotation curve (already in the dataset).
2. Set \(k_{\rm IR}=\pi/R_{\max}\).
3. Modify the anti-kernel to
\[
M_{\rm anti}(k)=1+\frac{\mu^2}{k^2+k_{\rm IR}^2}.
\]

This removes the literal \(k=0\) divergence and uses **no new fitted parameters**.

If you then still need a kill-switch, *that itself* becomes strong evidence for additional physics (thickness, leakage, extra field).

## 4. What “passing on dwarfs” should mean quantitatively

Define a dwarf pass/fail test:

- pick a dwarf subset (e.g. low \(V_{\max}\) or low \(g_{\max}\)),
- require the median \(\chi^2/{\rm dof}\) not to diverge,
- and require no systematic trend in residuals at large \(r\).

If a theory needs a discrete on/off switch to satisfy that, it’s not a theory yet; it’s a fit machine.

## 5. Next work item (code-level)

Implement the regulated anti-kernel
\[
M(k)=1+\frac{\mu^2}{k^2+k_{\rm IR}^2}
\]
in the Hankel pipeline and re-run the global \(\mu\) scan.

Then compare:
- global best \(\mu\),
- total \(\chi^2\),
- dwarf subset performance,
- distribution of fitted \(\Upsilon\) (if you removed \(A\) as suggested in UPG_03).

This is the cleanest way to make the dwarf behavior diagnostic rather than ad hoc.
