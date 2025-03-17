def solve_math_problem(number1: int, number2: int) -> str:
    """
    Solves a math problem by taking two numbers as inputs and returning the solution as a string.
    """
    problem = f"{number1} + {number2} = ?"
    answer = str(number1 + number2)
    return problem, answer
