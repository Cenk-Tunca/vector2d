from math import atan2, degrees, hypot
import math
import random
from vector2d import Vector2d

def print_conversion(vector, form):
    if form == "polar":
        r = hypot(vector.x, vector.y)
        theta = degrees(atan2(vector.y, vector.x))
        print(f"Rectangular form: ({vector.x}, {vector.y})\n"
              f"Polar form: ({r:.2f}, {theta:.2f} degrees)")
    elif form == "rectangular":
        r, theta = vector.to_polar()
        print(f"Rectangular form: ({vector.x}, {vector.y})\n"
              f"Polar form: ({r:.2f}, {degrees(theta):.2f} degrees)")
    else:
        print("Invalid form specified. Please choose either 'polar' or 'rectangular'.")

def generate_vector() -> Vector2d:
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    return Vector2d(x, y)

def print_conversion_solution(vector: Vector2d, form: str) -> None:
    if form == "polar":
        r = hypot(vector.x, vector.y)
        theta = degrees(atan2(vector.y, vector.x))
        print(f"Convert ({vector.x}, {vector.y}) to polar form:\n"
              f"r = {r:.2f}, theta = {theta:.2f} degrees")
    elif form == "rectangular":
        r, theta = vector.to_polar()
        print(f"Convert ({vector.x}, {vector.y}) to rectangular form:\n"
              f"x = {r:.2f} cos({degrees(theta):.2f}), y = {r:.2f} sin({degrees(theta):.2f})")
    else:
        print("Invalid form specified. Please choose either 'polar' or 'rectangular'.")

if __name__ == '__main__':
    while True:
        # Ask the user which type of conversion they want to practice
        form = input("Which type of conversion would you like to practice (rectangular or polar)? ")
        
        # Generate a random vector
        vector = generate_vector()
        
        # Display a conversion question of the appropriate type
        if form == "polar":
            print(f"Convert ({vector.x}, {vector.y}) to polar form:")
        elif form == "rectangular":
            print(f"Convert ({vector.x}, {vector.y}) to rectangular form:")
        else:
            print("Invalid form specified. Please choose either 'polar' or 'rectangular'.")
            continue
        
        # Wait for user input
        input("Press Enter to see the answer...")
        
        # Display the correct answer
        print_conversion_solution(vector, form)
        
        # Ask the user if they want to continue or quit
        choice = input("Would you like to receive another question (y/n)? ")
        if choice.lower() == "n":
            break

def print_polar_conversion(vector):
    r = math.sqrt(vector.x ** 2 + vector.y ** 2)
    theta = math.atan2(vector.y, vector.x)
    print(f"({vector.x}, {vector.y}) in polar form is ({r}, {theta})")


def print_rectangular_conversion(vector):
    x = vector.x * math.cos(vector.y)
    y = vector.x * math.sin(vector.y)
    print(f"({vector.x}, {vector.y}) in rectangular form is ({x}, {y})")


def print_polar_solution(vector):
    print_polar_conversion(vector)


def print_rectangular_solution(vector):
    print_rectangular_conversion(vector)

def vector_addition():
    print("Vector Addition")
    print("Enter the components of the first vector:")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    print("Enter the components of the second vector:")
    x2 = int(input("x: "))
    y2 = int(input("y: "))
    vector1 = Vector2d(x1, y1)
    vector2 = Vector2d(x2, y2)
    result = vector1 + vector2
    print(f"The result of the vector addition is: {result}")

def mixed_practice():
    while True:
        choice = random.choice(["rectangular", "polar"])
        vector = generate_vector()

        if choice == "rectangular":
            print_rectangular_conversion(vector)
            print_rectangular_solution(vector)
        else:
            print_polar_conversion(vector)
            print_polar_solution(vector)

        another = input("Another question? (Y/N): ")
        if another.upper() == "N":
            break

def Main_Menu():
    while True:
        print("Main Menu")
        print("1. Conversions")
        print("2. Vector Addition")
        print("Q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            conversion_menu()
        elif choice == "2":
            vector_addition()
        elif choice.upper() == "Q":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


def conversion_menu():
    while True:
        print("\nConversion Menu")
        print("1. Rectangular to Polar")
        print("2. Polar to Rectangular")
        print("3. Mixed Practice")
        print("R. Return to Main Menu")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            print_rectangular_conversion(generate_vector())
            print_rectangular_solution(generate_vector())
        elif choice == "2":
            print_polar_conversion(generate_vector())
            print_polar_solution(generate_vector())
        elif choice == "3":
            mixed_practice()
        elif choice.upper() == "R":
            break
        else:
            print("Invalid choice. Please try again.\n")
