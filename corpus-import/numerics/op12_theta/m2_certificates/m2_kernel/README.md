# m2_kernel — translation-lookup tensor cache (regenerable)

`tensor_L{4,6,8}_b{β}.npz` (key `T`): G_P orbit columns used by the M2 lookup. Cache only — deleting forces a clean regeneration by `ENGINE_OP1_m2_pair_certificates.py` / `ENGINE_OP1_m2_l8_shells.py`. Wart (recorded June 12): the engines resolve this path **relative to CWD**, so running from `numerics/op12_theta/` (the documented CWD) writes a second copy there; one such stray was verified array-identical and removed June 12. This directory is the canonical cache.
