import numpy as np
from scipy.optimize import minimize
from sympy import symbols, Eq

def f(x):
    return x[0]**2 + 3*x[1]*x[0] - 4

def constraints():
    return [Eq(x[0], 1), Eq(x[1], 2)]

# Minimize the function subject to given constraints
solution = minimize(f, (1, 2), constraints=constraints())

print("Solution:", solution)
