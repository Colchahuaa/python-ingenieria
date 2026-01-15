# Proyecto: Balance de masa en un sistema de mezcla
# Ingeniería de Procesos – Implementación en Python
# Modelo basado en balances de masa en estado estacionario

F1 = 500
x1 = 0.10

F2 = 300
x2 = 0.25

F_out = F1 + F2
m_soluto = F1*x1 + F2*x2
x_out = m_soluto / F_out

print("Caudal total:", F_out, "kg/h")
print("Flujo de soluto:", m_soluto, "kg/h")
print("Fracción másica final:", round(x_out,4))
