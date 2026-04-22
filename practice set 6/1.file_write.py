# 1. Create a file with file name sample.txt, 
# accept some data from the user and store it in the file.

def print_header(heading):
    print("=" * 50)
    print(heading)
    print("=" * 50)

def main():
    print_header("Writing data into sample.txt")

    print('enter the data you want to store in the file')
    str = input()
    try:
        f = open('sample.txt', 'w')
        f.write(str)
        f.close()
    except Exception as e:
        print(e)

    print("\nData written successfully")
    print('=' * 50)


if __name__ ==  "__main__":
    main()