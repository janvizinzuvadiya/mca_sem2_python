# 3. Accept some data from the user and append it into the file sample.txt 
# (created in question 1), also the data in the file.

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Appending data into file sample.txt")

    try:
        print('Enter data you want to append into the file:')
        str = input()
        f =  open('sample.txt','a')
        f.write(str)
        f.close()

        print('\nData appended successfully')
        print('-' * 50)

        print('\nData in the file :\n')
        f = open('sample.txt','r')
        str = f.read()
        print(str)
        print('-'*50)
        f.close()

        print('=' * 50)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()