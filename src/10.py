import random

def get_random_math_problem():
    operands = [1, 2, 3, 4, 5]
    operator = ["+", "-", "*", "/"]
    problem = f"{random.choice(operands)} {random.choice(operator)} {random.choice(operands)}"
    return problem
