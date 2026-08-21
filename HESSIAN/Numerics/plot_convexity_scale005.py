#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

betas = np.array([0.40,0.77,1.14,1.51,1.89,2.26,2.63,3.00])

# scale=0.05 tables from the scan
L4 = np.array([0.107639,0.090999,0.074027,0.058620,0.042761,0.024951,0.006105,-0.008208])
L6 = np.array([0.108966,0.093839,0.079105,0.063542,0.048837,0.033850,0.018730,0.003391])
L8 = np.array([0.109207,0.094372,0.078979,0.065228,0.049413,0.036033,0.020245,0.005785])

plt.figure()
plt.plot(betas, L4, marker='o', label='L=4')
plt.plot(betas, L6, marker='o', label='L=6')
plt.plot(betas, L8, marker='o', label='L=8')
plt.axhline(0.0)
plt.xlabel('β')
plt.ylabel('min Hessian eigenvalue λ_min')
plt.title('Convexity scan at scale=0.05 (SU(3), Padé22)')
plt.legend()
plt.show()
