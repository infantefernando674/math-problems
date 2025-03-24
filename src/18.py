def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def main():
    print("Triangle check program")
    try:
        # Input side lengths from user or from file (use 'a,b,c' format)
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))

        if is_triangle(side1, side2, side3):
            print(f"The given sides can form a triangle.")
        else:
            print(f"The given sides do not form a triangle.")

    except ValueError:
        print("Please enter numeric values for the side lengths.")

if __name__ == "__main__":
    main()
