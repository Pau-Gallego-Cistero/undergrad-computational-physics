# Quantum Mechanics: 1D Bound State Solvers

A collection of numerical and analytical solutions to the 1D time-independent Schrödinger equation for canonical quantum potentials:

$$\hat{H}\psi = \left( -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x) \right)\psi = E\psi$$

---

## Physics & Numerical Methods
* **Spatial Discretization:** The continuous coordinate $x$ is mapped to a discrete grid of $N$ points with spacing $\Delta x$.
* **Finite Difference Kinetic Operator:** The second spatial derivative is approximated via a 3-point central difference scheme:
  $$\frac{d^2\psi}{dx^2} \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta x^2}$$
* **Matrix Diagonalization:** The Hamiltonian matrix $\hat{H} = \hat{T} + \hat{V}$ is diagonalized using `scipy.linalg.eigh` to extract eigenvalues (energies $E_n$) and eigenvectors (stationary states $\psi_n(x)$).

---

## 📂 Included Scripts

| Script | Potential $V(x)$ | Method |
| :--- | :--- | :--- |
| **`infinite_potential_well.py`** | Particle in an infinite box ($V=0$ inside, $\infty$ outside) | Analytical vs. Finite Difference comparison |
| **`quantum_dots_finite_well.py`** | Finite square well (Quantum Dot model, $V_0 = 20\text{ eV}$) | Matrix diagonalization & bound state filtering |
| **`quantum_harmonic_oscillator.py`** | Parabolic potential $V(x) = \frac{1}{2}m\omega^2 x^2$ | Numerical diagonalization vs. theoretical $E_n = \hbar\omega(n + 1/2)$ |

---

## 👥 Collaborators
* **Quantum Harmonic Oscillator:** Developed with Marco Novellini and Nacho Fons.
