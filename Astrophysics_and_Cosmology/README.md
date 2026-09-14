# 🔭 Astrophysics & Cosmological Simulations

Numerical simulation of gravitational instability and linear structure growth in an expanding universe.

---

## Cosmological Perturbation Growth (MCE)

This simulation models the evolution of matter density fluctuations $\delta(x, t)$ in a flat, matter-dominated FLRW universe ($a(t) = t^{2/3}$), governed by the second-order differential equation:

$$\ddot{\delta} + 2H(t)\dot{\delta} = 4\pi G \bar{\rho}(t) \delta$$

where:
* $H(t) = \frac{2}{3t}$ is the Hubble parameter representing cosmic expansion damping (Hubble friction).
* $\bar{\rho}(t) = \rho_0 / a(t)^3$ is the mean background matter density.
* Perturbations are integrated iteratively using an explicit Euler numerical scheme.

### Physical Output
The script perturbs the initial spatial positions of particles and evolves them through cosmic time, tracking the clustering of matter into gravitational potential wells over three snapshots ($t = 0.1, 5, 10$).

---


```bash
python cosmological_perturbations_growth.py
