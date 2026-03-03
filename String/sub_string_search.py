#accept sub-string from users check if the sub-string is available in the string or not

print('\n--------------------------------------------------------------------------------------\n')


s = 'hello world! the world of Computer Science'
sub = input('Enter string to Search:  ')
if sub in s:
    print('String is Present')
else:
    print('String is not Present')

print('\n--------------------------------------------------------------------------------------\n')
