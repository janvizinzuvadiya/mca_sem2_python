str = input('Enter String->')

print('------------------------------------------------------------')

print('\n \tThe Type of The Variable is :\t', type(str))

print('\n \tThe String is :\t\t\t',str)

print('\n \t3rd Character :\t\t\t',str[2])

print('\n \t4rth to 6th Character :\t\t',str[4:7])

str = str[:2] + 'A' + str[3:]
print('\n \tReplaced Character :\t\t',str)

print('\n------------------------------------------------------------')