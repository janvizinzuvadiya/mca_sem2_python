# 12) Print 1 2 4 8 16 32 64 128 256 512 1024

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Double the numbers")
    print("Let's display the  last numbers exact double")

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    print("-"*50)
    print("\n")

    num = 1

    for i in range(1,12):
        print(num, end=" ")
        num*=2

    print("\n")
    print("-"*50)
    print("\n")

    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()