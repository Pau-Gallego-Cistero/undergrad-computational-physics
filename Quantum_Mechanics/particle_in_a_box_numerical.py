#PARTICULA EN UNA CAJA
import numpy as np
import matplotlib.pyplot as plt
import math as mt

# -------------------------
# Parámetros físicos
# -------------------------
# hbar = 1.0  <- (Nota: El cursor tapa la 'h', probablemente sea 'hbar')
hbar = 1.0 
m = 1.0
L = 1.0   # longitud del pozo

# -------------------------
# Espacio de trabajo
# -------------------------
N = 100
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# ---------------------------------------------------
# Matriz del operador cinético (segunda derivada)
# ---------------------------------------------------
T = np.zeros((N, N))
for i in range(N):
    T[i, i] = -2.0
    if i > 0:
        T[i, i-1] = 1.0
    if i <  N-1:
        T[i, i+1] = 1.0
T = (-hbar**2 / (2*m*dx**2)) * T
print(T)

# ---------------------------------------------------
# Potencial (pozo infinito)
# ---------------------------------------------------
V = np.zeros(N)         #Dentro del pozo, V=0
V[0] = V[-1] = 1e10     #Bordes: infinito aprox.
V_matrix = np.diag(V)

# -------------------------
# Hamiltoniano total
# -------------------------
H = T + V_matrix

# -------------------------
# Resolviendo el problema de Schrödinger
# -------------------------
E, psi = np.linalg.eigh(H)
# Normalización
psi = psi / np.sqrt(dx)
#
#Calculamos la densidad de probabilidad
#-------------------------
psi2 = np.square(psi)
#-------------------------
# Energías analíticas para comparación
#-------------------------
n_levels = 3
n = np.arange(1, n_levels+1)
E_analiticas = (np.pi**2 * hbar**2 * n**2) / (2*m*L**2)

#-------------------------
# Gráficas
#-------------------------
plt.figure(figsize=(10,5))

# (1) Espectro de energías
plt.subplot(1,2,1)
plt.plot(range(1, n_levels+1), E[:n_levels], 'o', label='Numérico')
plt.plot(range(1, n_levels+1), E_analiticas, 'x', label='Analítico')
plt.plot(range(1, n_levels+1), E_analiticas, 'x', label='Analítico')
plt.xlabel("n")
plt.ylabel("Energía")
plt.title("Energias de la partícula en el pozo")
plt.legend()

# (2) Funciones de onda
plt.subplot(1,2,2)
for i in range(n_levels):
    plt.plot(x, psi[:,i] + E[i], label=f'n={i+1}')
    plt.plot(x, psi2[:,i] + E[i], label=f'n={i+1}')

plt.xlabel("x")
plt.ylabel(r"$\psi_n(x)$ (desplazada)")
plt.title("Funciones de onda")
plt.legend()

plt.tight_layout()
plt.show()