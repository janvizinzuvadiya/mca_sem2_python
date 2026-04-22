# 4. Accept the file name from the user, check the availability of the file:
#  i). If the file exists display the data on the screen, 
# ii). If the file is not available, display the appropriate message.
import os,sys

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Checking file existance")

    try:
        print('Enter the file name : ')
        fname = input()
        if (os.path.isfile(fname)):
            print('file is available')

            f = open(fname,'r')
            str = f.read()
            f.close()

            print('-' * 50)
            print('data in the file->')
            print(str)
            print('-' * 50)

        else:
            print('file is not available')

        print('=' * 50)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()