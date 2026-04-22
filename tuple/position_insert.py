# allow user to insert the value at desired position in tuple

a = (1, 2, 3, 4, 5)
print(a)
# print(id(a))

l=int(input("Enter the value to be inserted: "))
print(type(l))

new_num = (l,)
pos= int(input("Enter the position where you want to insert the value: "))
temp = a[0:pos-1]
print(temp)

temp = temp + new_num
print(temp)

a= temp + a[pos-1:]
print(a)
# print(id(a))