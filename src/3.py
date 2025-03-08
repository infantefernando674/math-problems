import random

def get_random_math_problem(difficulty=1):
    """
    Generates a random math problem with the given difficulty level.
    The difficulty can be an integer from 1 to 5, where 1 is the easiest and 5 is the hardest.
    """
    # List of operators and their precedence levels
    operators = [("+", 1), ("-", 2), ("*", 3), ("/", 4)]
    # Generate a random problem with the given difficulty level
    problem = ""
    for i in range(difficulty):
        operator = random.choice(operators)
        problem += " {} ".format(operator[0])
    return problem