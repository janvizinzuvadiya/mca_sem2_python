# 5. Allow users to enter multiple strings in the list; 
# arrange the entered string into alphabetical order and display.

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("String Sorting")
    print("Let's sort some strings.\n")

    fruits = ["banana","dragon-fruit","orange","apple","grapes"]

    print(f"Original list : {fruits}")

    fruits.sort()

    print(f"Sorted list   : {fruits}")

    print("\n" + "=" * 50)

    print("\nThank you for using the program! 👋\n")



if __name__ == "__main__":
    main()