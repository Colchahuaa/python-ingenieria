
# ========================================================
# OPERACIONES UNITARIAS
# Intercambiador de Calor de Doble Tubo (Contracorriente)
# Nivel: Medio
# ========================================================

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Datos del proceso
# --------------------------------------------------------

# Fluido caliente
m_dot_h = 1.2        # kg/s
T_h_in = 90          # °C
Cp_h = 4180          # J/kg·K

# Fluido frío
T_c_in = 25          # °C
Cp_c = 4180          # J/kg·K

# Intercambiador
U = 850              # W/m²·K
A = 8                # m²

# --------------------------------------------------------
# 2. Función LMTD
# --------------------------------------------------------

def lmtd(T_h_in, T_h_out, T_c_in, T_c_out):
    delta_T1 = T_h_in - T_c_out
    delta_T2 = T_h_out - T_c_in
    return (delta_T1 - delta_T2) / np.log(delta_T1 / delta_T2)

# --------------------------------------------------------
# 3. Análisis paramétrico
# --------------------------------------------------------

m_dot_c_range = np.linspace(0.5, 2.0, 30)

Q_list = []
T_h_out_list = []
T_c_out_list = []

for m_dot_c in m_dot_c_range:

    C_h = m_dot_h * Cp_h
    C_c = m_dot_c * Cp_c
    C_min = min(C_h, C_c)

    effectiveness = 0.65
    Q = effectiveness * C_min * (T_h_in - T_c_in)

    T_h_out = T_h_in - Q / C_h
    T_c_out = T_c_in + Q / C_c

    Q_list.append(Q)
    T_h_out_list.append(T_h_out)
    T_c_out_list.append(T_c_out)

# --------------------------------------------------------
# 4. Resultados gráficos
# --------------------------------------------------------

plt.figure()
plt.plot(m_dot_c_range, T_c_out_list)
plt.xlabel("Caudal másico fluido frío [kg/s]")
plt.ylabel("Temperatura de salida fluido frío [°C]")
plt.title("Temperatura de salida vs caudal")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(m_dot_c_range, Q_list)
plt.xlabel("Caudal másico fluido frío [kg/s]")
plt.ylabel("Calor transferido [W]")
plt.title("Carga térmica vs caudal")
plt.grid(True)
plt.show()
