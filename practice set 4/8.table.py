# 8) Accept one integer value from the user; display the table of it.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Table of a Number")
    print("Let's display the table of the number you enter.\n")
    
    try:
        num = int(input('👉 Please enter an integer : '))
    except ValueError:
        print("\n❌ Error: Please enter a valid integer number!")
        return

    print("\n⏳ Checking...\n")
    time.sleep(0.5)

    print("-" * 50)
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
    print("-" * 50)
    
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()