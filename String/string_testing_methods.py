# isalnum(): true - alphabet , number || false
# isalpha(): true - alphabet || false
# isidgit(): true - numbers || false
# islower(): true - lowercase || false
# isupper(): true - uppercase || false

contact_num = input('enter the mobile number->')
print(contact_num.isdigit())
if(contact_num.isdigit())!=True:
    print('enter vlid number')


s = []
n = int(input('how many sting you want to input'))
for i in range (n):
    print('enter string')
    s.append(input())

print(s)
s1 = s.sort()
print(s1)

for i in s1:
    print(i , end=',')
