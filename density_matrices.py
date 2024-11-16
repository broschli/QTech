# -*- coding: utf-8 -*-
import numpy as np

# Import data
data1re = np.genfromtxt("./data/p2_Data1re.txt", delimiter="\t")
data1im = np.genfromtxt("./data/p2_Data1im.txt", delimiter="\t")
data2re = np.genfromtxt("./data/p2_Data2re.txt", delimiter="\t")
data2im = np.genfromtxt("./data/p2_Data2im.txt", delimiter="\t")

# Generate density matrices from data
rho1 = data1re + 1j * data1im
rho2 = data2re + 1j * data2im

# Check if tr(rho) = 1
assert abs(np.trace(rho1) -1) < 1e-15
assert abs(np.trace(rho2) - 1) < 1e-15

# Purity tr(rho^2) for both density matrices (@ is matrix multiplication)
purity_1 = np.trace(rho1 @ rho1)
purity_2 = np.trace(rho2 @ rho2)

# Generate psi vector from part a)
psi = np.zeros(16, dtype=complex)
psi[6] = 1 
psi[9] = 1
psi *= 2**-0.5

# Fidelity <psi|rho|psi> for both density matrices
fidelity_1 = psi @ (rho1 @ psi)
fidelity_2 = psi @ (rho2 @ psi)

# Print results
print(f"Data 1:\n\tPurity: \t{purity_1:1.4f}\n\tFidelity: \t{fidelity_1:1.4f}",
      "\n\n", 
      f"Data 2:\n\tPurity: \t{purity_2:1.4f}\n\tFidelity: \t{fidelity_2:1.4f}")
