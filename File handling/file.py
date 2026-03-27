# file handling
# 1. Text file :it store data in the form of characters 
                # 'abc'->abc 123->123
# 2. Binary file:it stores data in the form of bytes
                # every bytes will have 8 bits and 
                # every bit will have value 0 or 1
                # Text , image , audio , video are all binary files

# file handling in python# file handling in python

# file opening modes
# w : allows to write data in a file and it will overwrite the existing data
# a : allows to write data in a file and it will append the data at the end of the file
# r : allows to read data from a file
# x : allows to create a new file and write data in it. if the file already exists then it will raise an error
    # it open the file in exclusive mode creation of file will fail if the file already exists 
# + : it allows to read and write data in a file with w,r,a modes
    
# close() : it is used to close a file
# syntax: file_handler.close()
# it is important to close a file after performing operations on it to free up system resources and avoid potential data loss or corruption.

# 1. open() : it is used to open a file and it returns a file object
# syntax: file_handler = open ('file_name' , 'mode')

# 2. read() : it is used to read the contents of a file
# 3. write() : it is used to write data to a file
# 4. close() : it is used to close a file

# # create file and store the data by accepting from user

# file_name = open('file.txt' , 'w')
# data = input("Enter the data to be stored in the file: ")
# file_name.write(data)
# file_name.close()
    
# # read the data from the file and display it on the console
# f = open('file.txt' , 'r')
# data = f.read()
# print("Data from the file: ", data)
# f.close()

# # accept nultiple lines of data from user and store it in a file;
# file_name = open('file.txt' , 'w')
# n = int(input("Enter the number of lines you want to store in the file: "))
# s =''
# while s!='$':
#     data = input("Enter the data to be stored in the file (enter $ to stop): ")
#     if data == '$':
#         break
#     file_name.write(data + '\n')
# file_name.close()

# uasing for loop
# for i in range(n):
#     data = input("Enter the data to be stored in the file: ")
#     file_name.write(data + '\n')

# # uaing while loop
# i = 0
# while i < n:
#     data = input("Enter the data to be stored in the file: ")
#     file_name.write(data + '\n')
#     i += 1    
# file_name.close()

# while loop
 