import numpy as np
from scipy.optimize import minimize

def f(x):
    return x ** 2 - 4 * x + 3

result = minimize(f, 1)
print(result.x)
