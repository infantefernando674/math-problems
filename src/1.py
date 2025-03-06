import random

def get_random_math_problem():
    operands = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    problem = f"{operands[random.randint(0, len(operands) - 1)]} {operators[random.randint(0, len(operators) - 1)]} {operands[random.randint(0, len(operands) - 1)]}"
    return problem