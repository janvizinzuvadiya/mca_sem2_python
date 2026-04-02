# 2) Accept one integer value from the user; check whether entered number is divisible by 5 or not.
import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Divisibility by 5 Checker")
    print("Let's check if your number is perfectly divisible by 5.\n")
    
    try:
        num = int(input('👉 Please enter an integer : '))
    except ValueError:
        print("\n❌ Error: Please enter a valid integer number!")
        return

    print("\n⏳ Checking...\n")
    time.sleep(0.5)
    
    print("-" * 50)
    if num % 5 == 0:
        print(f"🎉 SUCCESS: {num} IS divisible by 5! 🎉")
    else:
        print(f"❌ RESULT : {num} is NOT divisible by 5.")
        print(f"             (Leaves a remainder of {num % 5})")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()