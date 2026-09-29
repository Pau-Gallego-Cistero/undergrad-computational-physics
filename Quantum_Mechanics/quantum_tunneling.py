#-----------
#ENTREGA DE PYTHON: Efecto tunel
#-----------

import numpy as np
import matplotlib.pyplot as plt

hbar = 1.054571817 * 10**-34
m = 9.109383702 * 10**-31 # kg, masa del electrón
e = 1.602176634 * 10**-19 # A⋅s, carga del electrón
E = 1.602176634 * 10**-19 # J, energía del electrón
c = 2.998e8 # velocidad de la luz en m/s
L_nm = np.linspace(0, 2.0) # En nanómetros para el eje X
L = L_nm * 1e-9
N = 2000 # número de puntos para Runge-Kutta
x = np.linspace(0, L, N)
dx = x[1] - x[0]
V0 = [1.2 * e, 2.0 * e, 3.0 * e, 5.0 * e]
V0_labels = [1.2, 2.0, 3.0, 5.0] # Para las etiquetas de la leyenda en eV -> corrección de IA
T = []
V = []

i = 0
while i < len(V0):
    V_actual = V0[i]

    for j in range(len(L)):
        L_actual = L[j]
        k1 = np.sqrt(2 * m * np.abs(E - V_actual)) / hbar
        k2 = np.sqrt(2 * m * (V_actual - E)) / hbar
        transmision = 1 / (1 + (V_actual**2 * np.sinh(k2 * L_actual)**2) / (4 * E * (V_actual - E)))
        V.append(V_actual)
        T.append(transmision)

    i += 1

#-------------------------
# Gráficas
#-------------------------
T_matriz = np.reshape(T, (len(V0), len(L))) # Separamos en 4 bloques de 500 para poder dibujar contra el eje X (que tiene 500).

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# Dibujamos las 4 curvas en cada gráfico
for idx in range(len(V0)):
    ax1.plot(L_nm, T_matriz[idx], label=f'V0={V0_labels[idx]} eV')
    ax2.plot(L_nm, T_matriz[idx], label=f'V0={V0_labels[idx]} eV')

# Grafica 1: Escala lineal
ax1.set_title('Efecto Túnel - Escala Lineal')
ax1.set_xlabel('L (nm)')
ax1.set_ylabel('Transmisión T')
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(True, alpha=0.3)

# Grafica 2: Escala Logarítmica (como pide el ejercicio)
ax2.set_title('Efecto Túnel - Escala Logarítmica')
ax2.set_xlabel('L (nm)')
ax2.set_ylabel('Transmisión T (Log)')
ax2.set_yscale('log') 
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("La transmitancia decae exponencialmente porque quanto mayor es L mas despreciables se vuelven los efectos quanticos,")
print("y la probabilidad de que el electrón atraviese la barrera es menor.")
print("Esto se debe a que la función de onda del electrón se atenúa dentro de la barrera")

#--------------------------------------------
# Efecto de la altura y mapa bidimensional
#--------------------------------------------
L_list_nm = [0.10, 0.30, 0.50, 1.00] 
L_list = np.array(L_list_nm) * 1e-9
V0_array_eV = np.linspace(1.01, 5.0, 500)
V0_array = V0_array_eV * e
L_map_nm = np.linspace(0.02, 2.0) 
L_map = L_map_nm * 1e-9
logT = np.zeros((len(V0_array), len(L_map)))
k2_V = np.sqrt(2 * m * (V0_array - E)) / hbar # no depende de L

plt.figure(figsize=(6, 4.5))
for i in range(len(L_list)):
    L_actual = L_list[i]
    T_L = 1 / (1 + (V0_array**2 * np.sinh(k2_V * L_actual)**2) / (4 * E * (V0_array - E)))
    plt.plot(V0_array_eV, T_L, label=f'L = {L_list_nm[i]:.2f} nm')

plt.yscale('log')
plt.title('Transmisión vs altura $V_0$')
plt.xlabel('$V_0$ (eV)')
plt.ylabel('T')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

for i in range(len(V0_array)):
    V_actual = V0_array[i]
    k2 = np.sqrt(2 * m * (V_actual - E)) / hbar
    T_fila = 1 / (1 + (V_actual**2 * np.sinh(k2 * L_map)**2) / (4 * E * (V_actual - E)))
    logT[i, :] = np.log10(T_fila)

plt.figure(figsize=(7, 5))
plt.pcolormesh(L_map_nm, V0_array_eV, logT, shading='auto', cmap='viridis')
plt.colorbar(label=r'$\log_{10} T$')

cs = plt.contour(L_map_nm, V0_array_eV, logT, levels=[-3, -2, -1], # Dibuja lineas encima de mapa de colores
                 colors='white', linestyles='--')

plt.title(r'Mapa de $\log_{10} T$ en el plano $(L, V_0)$')
plt.xlabel('L (nm)')
plt.ylabel('$V_0$ (eV)')
plt.show()

print("----Efecto de la altura y mapa bidimensional------")
print("Si L aumenta la transmitancia disminuye, y si V0 aumenta la transmitancia también disminuye,")
print("porque en la fórmula de T hay dos factores que dependen de V0, V0^2/(4E(V0-E)) y kappa*L del sinh.")
print("Los pares (L, V0) que producen la misma transmisión son los que están sobre una misma curva de nivel del mapa;")
print("cuanto menor es T, más a la derecha queda la curva, ya que se necesita mayor L para el mismo V0.")


#--------------------------------------------
# USO DE LA IA
#--------------------------------------------
print("---Declaración de uso de la IA---")
print("Prompt: respeta mi while y for, si ves algun error dimelo y luego modifica el ploteo dado como quieras para que cumpla,")
print("esto es un problema de efecto tunnel y se deben mantener k1. <<codigo insertado>>.")