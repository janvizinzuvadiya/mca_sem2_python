# 3. Accept the string from the user; display the string in the reverse order.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Reverse String")
    print("Let's reverse your string.\n")

    try:
        string = input("👉 Please enter a string : ")
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return

    print("\n⏳ Reversing...\n")
    time.sleep(0.5)

    print("-" * 50)
    print(f"Original String : {string}")
    print(f"Reversed String : {string[::-1]}")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")




if __name__ == "__main__":
    main()