# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: 
    # i). No. of characters,
    # ii). No. of words and
    # iii). No. of lines
# b. If the file does not exist, than display the appropriate message.

import os

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Checking file existance and other operations")
    try:
        print('Enter the file name : ')
        fname = input()

        if(os.path.isfile(fname)):
            f = open(fname, 'r')
            
            char_count = 0
            word_count = 0
            line_count = 0  

            for line in f:
                line_count += 1
                words = line.split()
                word_count += len(words)
                char_count += len(line)

            print('-' * 50) 

            print("Number of lines : ", line_count)
            print("Number of words : ", word_count)
            print("Number of characters : ", char_count)

            f.close()
            print('-' * 50)
            
        else:
            print("file is not available")
            print('-' * 50)
            

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()