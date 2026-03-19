#  Binary Files
# it stores data in the form of bytes (8 bits for each bytye)
# it can deal with text file, image file, audio file, video file etc
# the modes it uses are: wb, rb, ab, xb, w+b, r+b, a+b, x+b

# rb : it is used to read data from a binary file
# wb : it is used to write data to a binary file and it will overwrite the existing data
# ab : it is used to write data to a binary file and it will append the data at the end of the file
# xb : it is used to create a new binary file and write data in it. if the file already exists then it will raise an error 
# w+b : it is used to read and write data in a binary file and it will overwrite the existing data
# r+b : it is used to read and write data in a binary file and it will not overwrite the existing data
# a+b : it is used to read and write data in a binary file and it will append the data at the end of the file
# x+b : it is used to create a new binary file and read and write data in it. if the file already exists then it will raise an error

# copy an image file and create a new image file using binary file handling

source_file = open('source_image.png' , 'rb')
destination_file = open('destination_image.png' , 'wb')
data = source_file.read()
destination_file.write(data)
source_file.close()
destination_file.close()

