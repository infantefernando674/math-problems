import random
import math
def generate_math_problem(difficulty):
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # Determine the operator based on the difficulty level
    if difficulty == "easy":
        operator = "+-*/"
    elif difficulty == "medium":
        operator = "+-*/^"
    else:
        operator = "+-*/^%&"
    # Generate a random problem using the numbers and operator
    problem = f"{num1} {operator[random.randint(0, len(operator) - 1)]} {num2} = ?"
    return problem