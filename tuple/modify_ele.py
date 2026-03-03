#  modify elements in existing tuple
a = (1, 2, 3, 4, 5)
print(a)

l = [int(input ("Enter the value to be inserted: "))]
new_tuple = tuple(l)
print(new_tuple)
pos = int(input("Enter the position where you want to insert the value: "))
temp = a[0:pos-1]
print(temp)
temp = temp + new_tuple
print(temp)
a = temp + a[pos:]
print(a)
