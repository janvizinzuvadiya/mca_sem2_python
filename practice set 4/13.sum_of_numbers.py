# 13) Accept numbers from the user; display the sum of the entered numbers.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Sum of Numbers")
    print("Let's find the sum of the numbers you enter.")  
    try:
        print('How many numbers you want to enter?')
        n = int(input("👉 Please enter : "))
        
    except ValueError:
        print("\n❌ Error: Please enter a valid Number!")
        return

    sum = 0
    for i in range(n):
        print('Enter Actual Number')
        num = int(input(f"👉 Please Enter Number {i+1} : "))
        sum += num

    print(f"The sum of {n} numbers is {sum}")

    print("\n" + "=" * 50)
    print("Thank you for using the Sum of Numbers calculator!")
    print("=" * 50)
    time.sleep(1)
    return

if __name__ == "__main__":
    main()

    