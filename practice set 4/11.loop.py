#  11) Display the following output using loop:
# i. 1 to 10 
# ii. 10 to 1
# iii. 1 3 5 7 9 
# iv. 2 4 6 8 10


import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Displaying numbers using loop")
    print("Let's display the numbers using loop.")

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    print(f"{"i. 1 to 10":_^50}")
    print("\n")
    for i in range(1,11):
        print(i, end=" ")
    print("\n")

    print(f"{"ii. 10 to 1":_^50}")
    print("\n")
    for i in range(10,0,-1):
        print(i, end=" ")
    print("\n")

    print(f"{"iii. 1 3 5 7 9":_^50}")
    print("\n")
    for i in range(1,10,2):
        print(i, end=" ")
    print("\n")

    print(f"{"iv. 2 4 6 8 10":_^50}")
    print("\n")
    for i in range(2,11,2):
        print(i, end=" ")
    print("\n")

    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()