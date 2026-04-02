# 1) Accept two integer values from the user; display the number which is smaller and the number which is bigger.
import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Number Comparator")
    print("Please enter two integer values below to compare them.\n")
    
    try:
        a = int(input('👉 Enter the First Number  : '))
        b = int(input('👉 Enter the Second Number : '))
    except ValueError:
        print("\n❌ Error: Please enter valid integer numbers!")
        return

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)
    
    print("-" * 50)
    if a == b:
        print(f"✨ Both numbers are identically equal to {a}! ✨")
    elif a > b:
        print(f"✅ Bigger Number  : {a} (First Value)")
        print(f"➖ Smaller Number : {b} (Second Value)")
    else:
        print(f"✅ Bigger Number  : {b} (Second Value)")
        print(f"➖ Smaller Number : {a} (First Value)")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()