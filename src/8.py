import random

def get_random_math_problem(n=2):
    numbers = [random.randint(1, 10) for _ in range(n)]
    operators = ["+", "-", "*", "/"]
    operation = random.choice(operators)
    problem = f"{numbers[0]} {operation} {numbers[1]}"
    if n == 3:
        problem += f" {operation} {numbers[2]}"
    return problem
