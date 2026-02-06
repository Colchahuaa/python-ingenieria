
from src.limpieza_datos import limpiar_datos
from src.calculos_termicos import calcular_kpis
from src.analisis_estadistico import resumen_operacional
from src.visualizacion import graficar_kpis

df = limpiar_datos("data/datos_proceso.csv")
df = calcular_kpis(df)

resumen = resumen_operacional(df)

print("Resumen Operacional:")
for k, v in resumen.items():
    print(f"{k}: {v:.2f}")

graficar_kpis(df)

