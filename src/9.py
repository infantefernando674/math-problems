import random

def get_random_math_problem():
    numbers = [random.randint(1, 10) for _ in range(2)]
    operation = ["+", "-", "*", "/"][random.randint(0, 3)]
    answer = eval(str(numbers[0]) + operation + str(numbers[1]))
    return f"What is {numbers[0]} {operation} {numbers[1]}: {answer}"
