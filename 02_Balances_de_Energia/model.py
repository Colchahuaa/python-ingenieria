# model.py

def energy_balance(T, params):
    """
    Balance de energía para un CSTR en estado estacionario.
    Retorna el residuo del balance.
    """

    F = params["F"]
    Cp = params["Cp"]
    Tin = params["Tin"]

    delta_H_rxn = params["delta_H_rxn"]
    r = params["r"]

    U = params["U"]
    A = params["A"]
    T_cool = params["T_cool"]

    # Término por flujo
    flow_term = F * Cp * (Tin - T)

    # Calor generado por reacción
    reaction_term = -delta_H_rxn * r

    # Calor removido
    cooling_term = U * A * (T - T_cool)

    # Balance de energía
    return flow_term + reaction_term - cooling_term
