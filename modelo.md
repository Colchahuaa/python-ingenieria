# 🧪⚙️ Modelo Matemático – Sistema de Mezcla

---

## 🔹 1. Definición rigurosa del sistema

Se analiza una **operación unitaria de mezcla** con:

📥 Corrientes de entrada  
- F1, F2 → flujos másicos [kg/s o kg/h]

📤 Corriente de salida  
- Fout

Cada corriente contiene un **soluto** con fracción másica:

- **x1** en F1  
- **x2** en F2  
- **xout** en la salida  

🧠 La unidad corresponde a un **mezclador ideal en régimen estacionario**.

---

## 🔹 2. Hipótesis de modelación

Estas hipótesis garantizan un modelo físicamente consistente y matemáticamente resoluble:

|             Supuesto         |     Significado físico          |
|-------------------------------------------------------------  
| ⏱️ Estado estacionario       | No hay acumulación de masa      |
| 🧬 Sin reacción              | El soluto no se crea ni se destruye |
| 🚫 Sin pérdidas              | No hay fugas ni evaporación     |
| 🔄 Mezcla perfecta           | La salida es homogénea          |
| 📏 Densidad constante        | Los flujos másicos son aditivos |

➡️ En resumen:  
**Todo lo que entra, sale… y sale perfectamente mezclado.**

---

## 🔹 3. Balance total de masa

Ecuación general:
Entrada - Salida = Acumulación

Como el sistema está en estado estacionario:
F1 + F2 - Fout = 0

Por lo tanto:
Fout = F1 + F2


🧠 Esto representa la **ley de conservación de la masa**:  
el equipo no crea ni destruye materia.

---

## 🔹 4. Balance del soluto

Flujo másico de soluto en cada corriente:
- Entrada 1: `F1 * x1`  
- Entrada 2: `F2 * x2`  
- Salida: `Fout * xout`

Balance de soluto:
F1x1 + F2x2 = Fout*xout


Sustituyendo 
`Fout = F1 + F2`:

Despejando:
xout = (F1x1 + F2x2) / (F1 + F2)


🧩 Esta ecuación es el **corazón del mezclador**:  
una **media ponderada por flujo másico**.

---

## 🔹 5. Interpretación física

La concentración de salida es un **promedio ponderado**.

💡 La corriente que aporta mayor flujo másico tiene mayor influencia en la composición final.

Si entra poco flujo concentrado y mucho flujo diluido…  
👉 el diluido manda.  







