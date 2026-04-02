# 9) Display square and cube of numbers 1-10.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Square and Cube of Numbers 1-10")
    print("Let's display the square and cube of numbers 1-10.\n")

    print("\n⏳ Checking...\n")
    time.sleep(0.5)

    print("-" * 50)
    print("Number  |  Square |  Cube")
    print("-" * 50)
    for i in range(1,11):
        print(f"{i:^7} | {i*i:^7} | {i*i*i:^8}")
    print("-" * 50)

    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()

