# 5) Accept one integer value from the user; display appropriate day of the week.

import time
import os

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Day of Week")
    print("Let's check the day of the week.")
    try:
        num = int(input('👉 Please enter an integer: '))
    except ValueError:
        print("\n❌ Error: Please enter a valid integer number!")
        return

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    print("-" * 50)
    if num == 1:
        print(f"🎉 SUCCESS: {num} is Monday! 🎉")
    elif num == 2:
        print(f"🎉 SUCCESS: {num} is Tuesday! 🎉")
    elif num == 3:
        print(f"🎉 SUCCESS: {num} is Wednesday! 🎉")
    elif num == 4:
        print(f"🎉 SUCCESS: {num} is Thursday! 🎉")
    elif num == 5:
        print(f"🎉 SUCCESS: {num} is Friday! 🎉")
    elif num == 6:
        print(f"🎉 SUCCESS: {num} is Saturday! 🎉")
    elif num == 7:
        print(f"🎉 SUCCESS: {num} is Sunday! 🎉")
    else:
        print(f"❌ RESULT : {num} is not a valid day of the week.")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()