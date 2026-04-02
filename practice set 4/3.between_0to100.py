# 3) Accept one integer value from the user; check whether entered number is between 0-100 ог not.
import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Number Range Checker")
    print("Let's check if your number is between 0 and 100.")
    try:
        num = int(input('👉 Please enter an integer: '))
    except ValueError:
        print("\n❌ Error: Please enter a valid integer number!")
        return

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)
    
    print("-" * 50)
    if 0 <= num <= 100:
        print(f"🎉 SUCCESS: {num} IS between 0 and 100! 🎉")
    else:
        print(f"❌ RESULT : {num} is NOT between 0 and 100.")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()

    