# 2. Accept the string from the user; 
# display the message whether the entered string is palindrome or not.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Palindrome Checker")
    print("Let's check if your string is a palindrome.\n")
    
    try:
        string = input('👉 Please enter a string : ')
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return

    print("\n⏳ Checking...\n")
    time.sleep(0.5)
    
    print("-" * 50)
   
    if string[::1] == string[::-1]:
        print(f"🎉 SUCCESS: '{string}' IS a palindrome! 🎉")
    else:
        print(f"❌ RESULT : '{string}' is NOT a palindrome.")
        print(f"             (Reverse is '{string[::-1]}')")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()