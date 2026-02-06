
import matplotlib.pyplot as plt

def graficar_kpis(df):

    plt.figure()
    plt.plot(df["Q_real"])
    plt.title("Carga térmica en el tiempo")
    plt.xlabel("Tiempo")
    plt.ylabel("Q [W]")
    plt.show()

    plt.figure()
    plt.hist(df["eficiencia_termica"], bins=30)
    plt.title("Distribución de eficiencia térmica")
    plt.show()
