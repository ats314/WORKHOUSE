# SU(3) fourth-order real-space SOS package

## Exact result

`ENGINE_Y4_exact_real_space_sos_certificate.py` proves in rational Laurent arithmetic that the full 189-record fourth-order kernel satisfies

\[
C^\dagger(H_4-qI)C
=\frac{5}{48}\sum_iL_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}(\nabla_i\nabla_j)^\dagger(\nabla_i\nabla_j).
\]

## GPU validation

`ENGINE_Y4_sos_a100_validation.py` is a single-block Colab script. It requires CUDA by default, embeds the exact kernel as a fallback, compares the full 189-record plaquette action against the 25-point scalar stencil, checks the FFT symbol and generalized eigenvalue, and benchmarks the local stencil.

## Run

Exact CPU certificate:

```bash
python ENGINE_Y4_exact_real_space_sos_certificate.py --kernel DATA_Y4_full_real_space_h4_kernel.json.gz
```

Colab A100:

```python
%run /content/ENGINE_Y4_sos_a100_validation.py
```
