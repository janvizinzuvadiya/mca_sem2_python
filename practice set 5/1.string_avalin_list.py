# 1. Create a list containing several strings. Take input from the user (search string); 
# display whether entered string is available in the list or not.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("String available in list")
    print("Let's check if your fruit is available in the Menu.\n")

    list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    try:
        frt = input('👉 Please enter an a Fruit Name : ')
    except ValueError:
        print("\n❌ Error: Please enter a valid String!")
        return

    print("\n⏳ Checking...\n")
    time.sleep(0.5)

    print("-" * 50)

    if frt in list:
        print(f"🎉 SUCCESS: {frt} IS available in the Menu! 🎉")
    else:
        print(f"❌ RESULT : {frt} is NOT available in the Menu.")

    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()
