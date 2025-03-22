import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define equation
equation = x**3 - 3*x**2*y + 4*y**2 - 10*x + 6

# Solve the equation
solution = sp.solve(equation, (x, y))

# Print the solution
print(solution)
