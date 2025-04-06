import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = 5  # Example: 5 is given in your project's requirements.
area = calculate_area(radius)
print("The area of the circle with radius", radius, "is:", area)
