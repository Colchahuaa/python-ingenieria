# main.py

from parameters import *
from analysis import solve_reactor_temperature

def main():

    # Diccionario de parámetros
    params = {
        "F": F,
        "Cp": Cp,
        "Tin": Tin,
        "delta_H_rxn": delta_H_rxn,
        "r": r,
        "U": U,
        "A": A,
        "T_cool": T_cool
    }

    # Estimación inicial
    T_guess = 80.0  # °C

    # Resolver balance de energía
    T_reactor = solve_reactor_temperature(T_guess, params)

    # Resultados
    Q_generated = -delta_H_rxn * r
    Q_removed = U * A * (T_reactor - T_cool)

    print("===================================")
    print(" BALANCE DE ENERGÍA – CSTR ")
    print("===================================")
    print(f"Temperatura del reactor : {T_reactor:.2f} °C")
    print(f"Calor generado           : {Q_generated:.2f} kJ/h")
    print(f"Calor removido           : {Q_removed:.2f} kJ/h")
    print("===================================")

if __name__ == "__main__":
    main()
