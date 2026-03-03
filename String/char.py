#characters

ch = "atmiya"
print(s[0])
print(ch) 

ch = [5]
print(ch)

ch = s[0:3]
print(ch)

# type of char
n = input('enter character')
ch = s[0]
if ch.isalpha():
    print('yes')
    if ch.isupper():
        print('yes uppercase')
    else:
        print('lowercase')
else:
    print('not alpha')  

