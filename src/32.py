import numpy as np

def calculate_sum(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Parameters:
    - numbers: A list of integers or floats
    
    Returns:
    - The sum of the numbers.
    """
    return np.sum(numbers)

# Example usage and check function
example_numbers = [1, 2, 3, 4]
print("Sum:", calculate_sum(example_numbers))
