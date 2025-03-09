
import random

def get_random_math_problem(difficulty=1):
    """Returns a randomly generated math problem of the specified difficulty level.
    
    Args:
        difficulty (int): The level of difficulty for the math problem, with higher values indicating more difficult problems. Defaults to 1.
    
    Returns:
        tuple: A tuple containing the problem and its solution.
    """
    # Generate a random mathematical operation and the two numbers involved
    operation = random.choice(["+", "-", "*", "/"])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Generate a solution for the problem
    if operation == "+":
        solution = num1 + num2
    elif operation == "-":
        solution = num1 - num2
    elif operation == "*":
        solution = num1 * num2
    else:
        solution = int(num1 / num2)
    
    # Return the problem and its solution as a tuple
    return (f"What is {num1} {operation} {num2}?", solution)