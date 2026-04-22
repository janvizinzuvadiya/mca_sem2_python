# 6. Create a tuple and display it. Enter 25 at the third position and display it again.

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Tuple Modification")
    print("Let's modify a tuple.\n")

    my_tuple = (10,20,30,40,50)

    print(f"Original tuple : {my_tuple}")

    my_tuple[2] = 25

    print(f"Modified tuple : {my_tuple}")

    print("\n" + "=" * 50)

    print("\nThank you for using the program! 👋\n")



if __name__ == "__main__":
    main()