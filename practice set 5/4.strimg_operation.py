# 4. Accept the string from the user; allow user to choose from the following options and perform the task as per user's choice.
#  
# i). Convert to the upper case, 
# ii). Convert to the lower case, 
# iii). Convert to the swap case, 
# iv). Convert to the title case

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("String Operations")
    print("Let's perform some operations on your string.\n")

    try:
        string = input("👉 Please enter a string : ")
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return

    print("\n⏳ Processing...\n")
    time.sleep(0.5)

    print("-" * 50)

    print("\n👉 Please choose an option:")
    print("1. Upper Case")
    print("2. Lower Case")
    print("3. Swap Case")
    print("4. Title Case")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice : ")

        if choice == "1":
            print(f"Upper Case      : {string.upper()}")
        elif choice == "2":
            print(f"Lower Case      : {string.lower()}")
        elif choice == "3":
            print(f"Swap Case       : {string.swapcase()}")
        elif choice == "4":
            print(f"Title Case      : {string.title()}")
        elif choice == "5":
            print("\nThank you for using the program! 👋\n")
            return
        else:
            print("\n❌ Error: Invalid choice!")
            return 

    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()