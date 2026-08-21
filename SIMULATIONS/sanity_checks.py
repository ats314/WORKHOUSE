#!/usr/bin/env python3
# Sanity checks for two algebraic facts used in the project:
# 1) Local Gram matrix M = 3 I_6 + s s^T has det 2187 and eigenvalues {9,3,...,3}.
# 2) Fourier symbol of D1^* D1 is λ(k) I - q q^*, giving eigenvalues 0 and λ(k).

import numpy as np

def local_gram_matrix():
    # s encodes whether the plaquette includes the fixed link edge with + or - orientation.
    s = np.array([1, -1, 1, -1, 1, -1], dtype=float)
    M = 3.0*np.eye(6) + np.outer(s, s)
    eig = np.linalg.eigvals(M)
    det = np.linalg.det(M)
    return M, eig, det

def D1_symbol(k):
    'Return D1(k) as a (d choose 2) x d matrix for d=len(k).'
    d = len(k)
    q = np.array([np.exp(1j*kk)-1.0 for kk in k], dtype=complex)
    pairs = [(mu,nu) for mu in range(d) for nu in range(mu+1,d)]
    D = np.zeros((len(pairs), d), dtype=complex)
    for r,(mu,nu) in enumerate(pairs):
        D[r,mu] = q[nu]
        D[r,nu] = -q[mu]
    return D, q

def maxwell_symbol_eigs(k):
    D,q = D1_symbol(k)
    A = D.conj().T @ D  # D1^* D1
    eig = np.linalg.eigvals(A)
    lam = float(np.sum(np.abs(q)**2))
    return eig, lam

def main():
    print('=== Local Gram matrix check ===')
    M, eig, det = local_gram_matrix()
    eig_sorted = np.sort(np.real_if_close(eig))
    print('Eigenvalues:', eig_sorted)
    print('Determinant:', det)
    print()

    print('=== Fourier symbol check for random k (d=4) ===')
    for i in range(3):
        k = np.random.uniform(-np.pi, np.pi, 4)
        eig, lam = maxwell_symbol_eigs(k)
        eig_sorted = np.sort(np.real_if_close(eig))
        print(f'Sample {i+1}:')
        print('  k =', k)
        print('  eig(D1^*D1) =', eig_sorted)
        print('  lambda(k)   =', lam)
        print()

if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True)
    main()
