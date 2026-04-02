# 4) Accept one integer value from the user; display the length of the entered number,
#  also display that the entered number is of four digits or not.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Number Length Checker")
    print("Let's check the length of your number.")
    try:
        num = int(input('👉 Please enter an integer: '))
    except ValueError:
        print("\n❌ Error: Please enter a valid integer number!")
        return 

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    print("-" * 50)
    print(f"The length of the number {num} is {len(str(num))}")
    if len(str(num)) == 4:
        print(f"The number {num} is a four-digit number.")
    else:
        print(f"The number {num} is not a four-digit number.")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()
