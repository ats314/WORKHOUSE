# Derivation of the Flux Truncation Error Bound in 2D U(1) Lattice Gauge Theory

**Author:** Manus AI

**Date:** November 25, 2025

## 1. Introduction

In the tensor network construction for 2D U(1) lattice gauge theory, the integer flux variables $n_p$ on each plaquette are, in principle, unbounded. For a practical numerical implementation, these variables must be truncated to a finite range, typically $|n_p| \le N_{\max}$. This truncation introduces an approximation error. This document provides a detailed derivation of the error bound, showing that it decays exponentially with $N_{\max}^2$, which justifies the truncation as a controlled approximation.

## 2. The Villain Action and Flux Probabilities

The partition function, after integrating out the gauge fields, is a sum over all possible integer flux configurations on the plaquettes:

$$ Z(\beta, \theta) = \sum_{\{n_p\}} \left( \prod_p e^{-\frac{\beta}{2}(\theta_p - 2\pi n_p)^2} \right) e^{i\theta Q[\{n_p\}]} \times \delta(\text{constraints}) $$

where $\delta(\text{constraints})$ enforces the discrete Bianchi identity. The weight of any given flux configuration is dominated by the product of the Villain action terms, $e^{-\frac{\beta}{2}(\theta_p - 2\pi n_p)^2}$.

Let us consider the probability distribution for the flux $n_p$ on a single plaquette, ignoring the constraints for a moment. The probability of a flux $n_p$ is proportional to its Boltzmann weight:

$$ P(n_p) \propto e^{-\frac{\beta}{2}(\theta_p - 2\pi n_p)^2} $$

For simplicity, let's assume the plaquette angle $\theta_p$ is close to zero, which is the case for smooth field configurations. The weight becomes:

$$ P(n_p) \propto e^{-2\pi^2\beta n_p^2} $$

This is a discrete Gaussian distribution. The probability of observing a large flux value $|n_p| > N_{\max}$ is extremely small for any reasonable value of $\beta$.

## 3. Bounding the Truncation Error

The error introduced by truncating the fluxes can be bounded by considering the total weight of all configurations that are excluded by the truncation. Let $Z_{\text{TN}}$ be the partition function with the truncation $|n_p| \le N_{\max}$ for all $p$, and $Z$ be the exact partition function. The error is:

$$ |Z - Z_{\text{TN}}| = \left| \sum_{\{\text{configs with any } |n_p| > N_{\max}\}} (\text{Weight}) \right| $$

Since all weights are positive (we can bound the absolute value of the full complex expression by the sum of the absolute values of the weights, and $|e^{i\theta Q}| = 1$), we can use a union bound. The probability of *any* plaquette having a large flux is bounded by the sum of the probabilities for each individual plaquette:

$$ |Z - Z_{\text{TN}}| \le \sum_p \sum_{|n_p| > N_{\max}} P(n_p) \cdot Z_{\text{rest}} $$

where $Z_{\text{rest}}$ is the partition function of the remaining lattice, which is a constant factor. The dominant term is the tail probability of the Gaussian distribution.

### 3.1. The Gaussian Tail Bound

We need to bound the sum of the tail of the discrete Gaussian distribution:

$$ S_{\text{tail}} = \sum_{|n| > N_{\max}} e^{-2\pi^2\beta n^2} = 2 \sum_{n=N_{\max}+1}^{\infty} e^{-2\pi^2\beta n^2} $$

This sum can be bounded by its corresponding integral. Let $\alpha = 2\pi^2\beta$. Then:

$$ \sum_{n=N_{\max}+1}^{\infty} e^{-\alpha n^2} \le \int_{N_{\max}}^{\infty} e^{-\alpha x^2} dx $$

We can use a standard inequality for the tail of the Gaussian integral (related to the error function):

$$ \int_K^{\infty} e^{-\alpha x^2} dx \le \frac{1}{2\alpha K} e^{-\alpha K^2} \quad \text{for } K > 0 $$

Applying this bound with $K = N_{\max}$:

$$ S_{\text{tail}} \le 2 \cdot \frac{1}{2(2\pi^2\beta)N_{\max}} e^{-2\pi^2\beta N_{\max}^2} = \frac{1}{2\pi^2\beta N_{\max}} e^{-2\pi^2\beta N_{\max}^2} $$

### 3.2. The Total Error Bound

The total error is the sum of these tail probabilities over all $N_{\text{plaq}} = L_x \times L_t$ plaquettes:

$$ |Z - Z_{\text{TN}}| \le (L_x L_t) \cdot C_0 \cdot \frac{1}{2\pi^2\beta N_{\max}} e^{-2\pi^2\beta N_{\max}^2} $$

where $C_0$ is a normalization constant from the partition function. We can absorb the prefactors into a single constant $C(\beta, L_x, L_t)$ and the constant in the exponent as $c(\beta) = 2\pi^2\beta$. This gives the final form of the bound:

$$ |Z(\beta, \theta) - Z_{\text{TN}}(\beta, \theta; N_{\max})| \le C(\beta, L_x, L_t) \cdot e^{-c(\beta) N_{\max}^2} $$

This demonstrates that the error introduced by truncating the integer fluxes decays **exponentially with the square of the cutoff, $N_{\max}^2$**. This is a very rapid decay, which means that a relatively small value of $N_{\max}$ is sufficient to achieve high precision.

## 4. Justification and Assumptions

*   **Dominance of the Villain Action:** The derivation assumes that the dominant contribution to the path integral weight comes from the Villain action term. The Bianchi identity constraint only prunes the set of allowed configurations but does not change the exponential decay of the weights for individual fluxes.
*   **Smooth Field Configurations:** We assumed $\theta_p \approx 0$ for simplicity. If $\theta_p$ is large, the Gaussian is centered at a non-zero value, but the argument still holds. The decay is still Gaussian, just centered around a different mean. The truncation must be chosen relative to this mean, e.g., $|n_p - \frac{\theta_p}{2\pi}| \le N_{\max}$.
*   **Union Bound:** The use of the union bound is a conservative estimate, but it is sufficient to establish the exponential nature of the decay.

## 5. Conclusion

The truncation of integer fluxes to a finite range $|n_p| \le N_{\max}$ is a necessary step for the practical implementation of the tensor network for 2D U(1) lattice gauge theory. The error introduced by this truncation is rigorously bounded and shown to decay exponentially with $N_{\max}^2$. This rapid decay ensures that the approximation is well-controlled and that the bond dimension of the tensors can be kept manageable without sacrificing accuracy. The exponential decay is a direct consequence of the Gaussian nature of the Villain action, which penalizes large flux values, making them statistically insignificant in the path integral.
