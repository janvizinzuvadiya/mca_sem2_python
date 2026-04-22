# 2. Display the data stored in the sample.txt file (created in question 1).

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('='* 50)

def main():
    print_header("Displaying data from sample.txt")

    try:
        f = open('sample.txt','r')
        str = f.read()
        print('-' * 50)
        print('data from the file :\n')
        print(str)
        f.close()
        print('\n')
        print('-' * 50)
    except Exception as e:
        print(e)
    
    print('=' * 50)
    
if __name__ == "__main__":
    main()