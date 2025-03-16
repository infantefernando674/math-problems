import random

def get_random_math_problem(lower_bound=1, upper_bound=10):
    first_number = random.randint(lower_bound, upper_bound)
    second_number = random.randint(lower_bound, upper_bound)
    operator = random.choice(['+', '-', '*', '/'])
    problem = f'{first_number} {operator} {second_number} = ?'
    return problem