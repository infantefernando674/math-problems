import numpy as np

def calculate_area(shape, padding):
    """
    Calculate the area of a shape given its dimensions and padding.
    :param shape: A tuple (length, width) representing the dimensions of the shape.
    :param padding: An integer representing the amount to add or subtract from each side of the shape.
    :return: The calculated area.
    """
    length, width = shape
    original_area = length * width

    # Calculate the new dimensions after adding padding
    new_length = length + 2 * padding
    new_width = width + 2 * padding

    # Update the areas with the new dimensions
    updated_area = new_length * new_width

    return updated_area - original_area

shape = (5, 3)
padding = 1
print(calculate_area(shape, padding))
