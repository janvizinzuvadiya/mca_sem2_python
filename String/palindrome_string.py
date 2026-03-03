# check the string is palindrome or not

print('\n--------------------------------------------------------------------------------------\n')

str = input('Enter string: ')
s1 = (str[::-1])
if (str==s1):
    print('String is Palindrome')
else:
    print('String is not Palindrome')

print('\n--------------------------------------------------------------------------------------\n')
