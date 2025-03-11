import random

def get_random_math_problem(max_value=100):
    operands = [i for i in range(2, max_value + 1)]
    operation = random.choice(["+", "-", "*", "/"])
    problem = f"{random.choice(operands)}{operation}{random.choice(operands)}"
    return eval(problem)