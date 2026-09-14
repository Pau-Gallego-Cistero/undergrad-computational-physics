import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# Unidades naturales
HBAR2_OVER_2M = 0.0380998212 
N = 500 # La malla de continuo a discreto 
L_min = -2 # Ajustado para centrar mejor el pozo
L_max = 4
x = np.linspace(L_min, L_max, N) # Discretizar
dx = x[1] - x[0]
V0 = 20
L = 2

# Definimos el Potencial como matriz
V_array = np.array([V0] * len(x))
V_array[(x > 0) & (x < L)] = 0
V = np.diag(V_array)
# EZEQUIEL: V = np.where((x > 0) & (x < L), 0.0, V0)

# CINÉTICA
# Como estamos usando una malla discreta (puntos separados por dx), no podemos derivar analiticamente. Usamos la "Formula de Diferencias Finitas Centradas".
#                     ψ(i+1) - 2*ψ(i) + ψ(i-1)
#   d^2_ψ / dx^2 ≈ --------------------------------    fuente: https://mathworld.wolfram.com/Derivative.html
#                                 dx^2

comp_traza = -2 * np.ones(N) # En la matriz 500x500
resto_matrix  = np.ones(N-1) # Diagonales secundarias
# Construimos la matriz
D2 = (np.diag(comp_traza, k=0) +
      np.diag(resto_matrix,  k=1) +
      np.diag(resto_matrix,  k=-1))
D2 = D2 / (dx**2)
T = -HBAR2_OVER_2M * D2


# HAMILTONIANOA
H = T + V
VAPS, VEPS = la.eigh(H) # DIAGONALIZACION Autovalores -> energia; autovectores -> Ondas

# Pozo finito
indices_ligados = np.where(VAPS < V0)[0]
E_bound = VAPS[indices_ligados]
psi_bound = VEPS[:, indices_ligados] / np.sqrt(dx) # Normalización

# -- GRAFICO ENERGIAS Y FUNCIONES DE ONDA -- 
plt.figure(figsize=(9, 5.6))
plt.plot(x, V_array, color='black', linewidth=2, label='V(x)')

# Escala visual para las funciones
scale = 0.5 

for i in range(len(E_bound)):
    E = E_bound[i]
    psi = psi_bound[:, i]
    # Desplazamos la funcion de onda a la altura de su energia para visualizar
    psi_scaled = E + scale * psi 
    
    plt.axhline(E, color='gray', linestyle='--', linewidth=0.8) # Linea de nivel
    plt.plot(x, psi_scaled, label=f'n={i}, E={E:.3f} eV')
    print(f'Nivel n={i}, Energía E={E:.4f}') # Printeamos la energia encontrada

plt.title(f'L={L} nm, V0={V0} eV')
plt.xlabel('x (nm)')
plt.ylabel('Energy (eV)')
plt.ylim(-0.04, V0 + 0.1)
plt.legend(fontsize=8, loc='upper right')
plt.grid(True, alpha=0.3)

plt.show()