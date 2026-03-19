# Syntax:
# with open(file_name, mode) as file_object:
#     # perform file operations

# the with statement automatically takes care of closing the file after the block of code is executed, even if an error occurs. This ensures that resources are properly released and helps prevent potential issues related to open files.

# create a file and store the data by accepting from user using with statement
# with open('file.txt' , 'w') as file_name:
#     data = input("Enter the data to be stored in the file: ")
#     file_name.write(data)

# seek() : it is used to change the position of the file pointer
# syntax: file_object.seek(offset, whence)
# offset : it is the number of bytes to move the file pointer
# whence : it is the reference point from which the offset is calculated. It can take the

# syntax : file_object.seek(offset, 'from_where')
# offset means the number of bytes to move the file pointer, and from_where specifies the reference point for the offset.
# The from_where parameter can take the following values:

# following values:
# - 0: It means the beginning of the file (default value).
# - 1: It means the current position of the file pointer.
# - 2: It means the end of the file.

# tell() : it is used to get the current position of the file pointer
# syntax: file_object.tell()
# It returns the current position of the file pointer in bytes from the beginning of the file.

# purpose: of seek() and tell() is to manipulate the file pointer in a file. seek() allows you to move the file pointer to a specific position in the file, 
# while tell() allows you to get the current position of the file pointer. This can be useful for various operations such as reading or writing data at specific locations in the file, or for navigating through the file in a non-linear way.


# create a binary file add data into it 
# ask user the position of the data to display
# display as per the required position

# reco_len = 10
# with open('hardware.bin' , 'wb') as f:
#     n = int(input("Enter the number of records you want to store in the file: "))
#     for i in range(n):
#         name = input("Enter the name of the hardware: ")
#         len = len(name)
#         name = name + (reco_len - len) * ' '
#         name = name.encode()  # encode() : converts nrml data to bytes
#         f.write(name)

# reco_len = 10
# with open('hardware.bin','rb') as f:
#     n = int(input('enter record no od the data you want to see:'))
#     f.seek(reco_len*(n-1)) # removes the file pointer to the end of the n-1th record
#     s = f.read(reco_len) # get the nth record with 10 characters
#     print(s.decode()) # decodes the data to display data from bin file

