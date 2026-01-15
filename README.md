
## 📁 Estructura del proyecto
balance-mezcla/
│
├── README.md
│
├── src/ 
│   └── balances.py
│
├── notebooks/
│   └── balance_mezcla.ipynb
│
└── docs/
    └── modelo.md


# Balance de masa en un sistema de mezcla

Este proyecto modela una operación unitaria de mezcla de dos corrientes con diferente concentración de soluto utilizando balances de masa y Python.

El objetivo es calcular el caudal total, el flujo de soluto y la fracción másica final de la corriente de salida.

Este tipo de problema es común en procesos de formulación, preparación de soluciones, dilución de productos y control de calidad en plantas químicas.

---

## 🧪 Enunciado del problema 1

Dos corrientes de agua con soluto se mezclan en un estanque:

| Corriente | Caudal (kg/h) | Fracción másica |
|--------|----------------|-------------------|
|   A    |     500        |     0.10          |
|   B    |     300        |     0.25          |

Se pide calcular:

a.- Caudal total de salida  
b.- Flujo total de soluto  
c.- Fracción másica final  

---

## 🧮 Modelo matemático

Balance total de masa:

F_out = F₁ + F₂  

Balance de soluto:

m_soluto = F₁·x₁ + F₂·x₂  

Fracción másica de salida:

x_out = m_soluto / F_out  

Donde:
- F es el caudal másico (kg/h)
- x es la fracción másica de soluto

---

# 🧠 Interpretación ingenieril

El sistema produce una corriente final con una concentración de soluto del 15.6%.  
Este tipo de cálculo es clave en procesos de formulación, preparación de soluciones químicas y control de calidad.

---

## 🛠️ Tecnologías
- Python
- Programación estructurada
- Ingeniería de procesos

---




