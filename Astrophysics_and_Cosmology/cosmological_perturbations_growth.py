

import numpy as np
import matplotlib.pyplot as plt


N = 20
G = 6.674e-11
L_min = 0
L_max = 1
t0 = 0.1
t_f = 10
ts = np.linspace(t0, t_f, N)
rho_0 = 1.5e10  # cte en rho = cte * a^-3, grande para compensar G
x0 = np.linspace(L_min, L_max, N, endpoint=False)
epsilon = 0.1 # cuánto se desplazan las partículas
delta = epsilon * np.sin(2 * np.pi * x0)  # Perturbación inicial pequeña
delta_dot = 0.0

def ecu_densidad(delta, delta_dot, t):
    a = (t)**(2/3) # Factor de escala
    H = (2/3) * (1/t) # Hubble
    rho = rho_0 / (a**3) # Densidad media
    
    d2_delta = 4 * np.pi * G * rho * delta - 2 * H * delta_dot
    return d2_delta

dt = 0.01

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# Creamos una figura con 1 fila y 3 columnas
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)


momentos = [t0, 5, 10] 

for i, t in enumerate(momentos):
    
    while t0 < t:
        ddelta = ecu_densidad(delta, delta_dot, t0)
        delta_dot += ddelta * dt
        delta += delta_dot * dt
        t0 += dt
    
    posiciones = (x0 + delta) % L_max 
    
    axs[i].hist(posiciones, bins=10, range=(0,1), 
                color='royalblue', edgecolor='black', rwidth=0.85)
    
    # Títulos individuales en cada subplot
    axs[i].set_title(f'Tiempo t = {t}', fontsize=14)
    axs[i].set_xlabel('Posición', fontsize=12)
    axs[i].grid(axis='y', alpha=0.3)

axs[0].set_ylabel('Número de partículas', fontsize=12)
    
plt.tight_layout() # Ajusta automáticamente los márgenes para que no se pisen las letras
plt.show()


'''
def calcular_posicion(t):
    x_t = x0 + t * epsilon * np.sin(2 * np.pi * x0) + delta(t)

    # El % partícula pasa de 1, vuelva a aparecer por el 0
    x_t = x_t % L_max 
    
    return x_t

x_t = []
'''
