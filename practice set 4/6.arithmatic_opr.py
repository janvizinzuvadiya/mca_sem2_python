# 6) Take choice from the user, and perform the arithmetic operation as per the choice. Choices: 1)
# Addition, 2) Subtraction, 3) Multiplication 4) Division

import time
import os

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Arithmetic Operations")
    print("Let's perform arithmetic operations.")

    print(f"{'Operations:':_^50}")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input('👉 Please enter your choice: '))

        num1 = int(input('👉 Please enter the first number: '))
        num2 = int(input('👉 Please enter the second number: '))
    except ValueError:
        print("\n❌ Error: Please enter valid integer numbers!")
        return

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    if(choice == 1):
        print(f"{'Addition':-^50}")
        print("-" * 50)
        print(f" {num1} + {num2} = {num1 + num2}")
    elif(choice == 2):
        print(f"{'Subtraction':-^50}")
        print("-" * 50)
        print(f" {num1} - {num2} = {num1 - num2}")
    elif(choice == 3):
        print(f"{'Multiplication':-^50}")
        print("-" * 50)
        print(f" {num1} * {num2} = {num1 * num2}")
    elif(choice == 4):
        print(f"{'Division':-^50}")
        print("-" * 50)
        print(f" {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice")

    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()
