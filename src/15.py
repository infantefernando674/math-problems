def get_random_math_problem(a=1, b=2):
    operation = ["+", "-", "*", "/"][random.randint(0, 3)]
    problem = f"{a} {operation} {b}"
    if operation == "+":
        solution = a + b
    elif operation == "-":
        solution = a - b
    elif operation == "*":
        solution = a * b
    else:
        solution = a / b
    return problem, solution
