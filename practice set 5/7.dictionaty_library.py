# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, 
# b. Display the name of Author,
# c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert 'year' as the new key
# and display the dictionary again.

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Dictionary Library")
    print('Here is the library dictionary : \n')

    library = {
        'Bookid' : 1,
        'Title' : 'Python Programming',
        'Author' : 'John Doe',
        'Price' : 500,
        'Publisher' : 'ABC Publications'
    }

    print(library)

    print('\n' + "=" * 50)

    print(f"\nAuthor name : {library['Author']}")

    print(f"Bookid : {library['Bookid']}")

    print(f"Length of the dictionary : {len(library)}")

    library['Price'] = 600

    print(f"Updated price : {library['Price']}")

    library['year'] = 2022

    print(f"Updated dictionary : {library}")

    print('\nThank you for using the program! 👋\n')

if __name__ == "__main__":
    main()