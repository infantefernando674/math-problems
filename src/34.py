import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        area = length * width
    elif shape == "circle":
        radius = dimensions[0]
        area = math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape")
    return area

shape = input("Enter the shape: rectangle or circle: ")
dimensions = list(map(int, input(f"Enter dimensions for {shape}:\n").split()))
area = calculate_area(shape, dimensions)
print(area)
