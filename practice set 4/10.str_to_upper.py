# 10 Accept string from the user; convert the string to upper case.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("String to Upper Case Converter")
    print("Let's convert your string to upper case.\n")

    try:
        str = input("Enter a string: ")
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return

    print("\n⏳ Checking...\n")
    time.sleep(0.5)

    print("-" * 50)
    print(f"Original string: {str}")
    print(f"Upper case string: {str.upper()}")
    print("-" * 50)

    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()