
def calcular_kpis(df):
    Cp = 4180
    df["Q_real"] = df["m_hot"] * Cp * (df["T_hot_in"] - df["T_hot_out"])
    df["eficiencia_termica"] = (
        (df["T_cold_out"] - df["T_cold_in"]) /
        (df["T_hot_in"] - df["T_cold_in"])
    )
    df["desempeno_relativo"] = df["Q_real"] / df["Q_real"].max()
    return df
