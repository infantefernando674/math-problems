import random

def get_random_math_problem():
    numbers = [random.randint(0, 100) for i in range(2)]
    operation = random.choice(['+', '-', '*', '/'])
    answer = eval(str(numbers[0]) + operation + str(numbers[1]))
    return f'What is {numbers[0]} {operation} {numbers[1]}'