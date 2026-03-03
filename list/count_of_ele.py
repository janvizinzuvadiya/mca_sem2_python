# count of a variable

print('\n--------------------------------------------------------------------------------------\n')

a = []
n = int(input('Total No of Element:'))
for i in range(n):
    print('Enter Value:',end='')
    a.append(int(input()))

print('Elemets are:' , a)
find = int(input('Give Element to check count of it:'))
count = 0
for i in a:
    if(find==i):
        count+=1
print('Element',find ,'occures',count ,'Times in the List')

print('\n--------------------------------------------------------------------------------------\n')
