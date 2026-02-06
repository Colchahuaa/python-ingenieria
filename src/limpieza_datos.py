
import pandas as pd

def limpiar_datos(path):
    df = pd.read_csv(path)
    df = df[(df["T_hot_in"] > df["T_hot_out"])]
    df = df[(df["T_cold_out"] > df["T_cold_in"])]
    df = df[df["m_hot"] > 0]
    df = df[df["m_cold"] > 0]
    return df
