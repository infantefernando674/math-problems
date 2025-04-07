import random

def random_number_generator():
    return random.randint(1, 100)

def main():
    print("Random number between 1 and 100:")
    result = random_number_generator()
    print(result)
