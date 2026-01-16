# analysis.py

import numpy as np
from scipy.optimize import fsolve
from model import energy_balance

def solve_reactor_temperature(initial_guess, params):
    """
    Resuelve la temperatura de operación del reactor.
    """

    solution = fsolve(
        energy_balance,
        initial_guess,
        args=(params,)
    )

    return solution[0]
