def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    sqrt_val = math.sqrt(x)
    return sqrt_val

try:
    print(square_root(-4))
except ValueError as e:
    print(e)  # Output: Cannot compute square root of a negative number
