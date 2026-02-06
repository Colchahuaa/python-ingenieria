def resumen_operacional(df):
    resumen = {
        "Q_promedio (W)": df["Q_real"].mean(),
        "Eficiencia promedio": df["eficiencia_termica"].mean(),
        "Desviacion Q": df["Q_real"].std(),
        "Operacion estable (%)": 
            (abs(df["Q_real"] - df["Q_real"].mean()) < df["Q_real"].std()).mean()*100
    }
    return resumen
