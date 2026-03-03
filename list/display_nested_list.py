# Display Values from nested list

print('\n--------------------------------------------------------------------------------------\n')

l = [10,20,30,[100,200]]

print(l)

print('Using each element:')
print(l[0])
print(l[1])
print(l[2])
print(l[3][0])
print(l[3][1])

print('\n---------------------------------------------\n')

print('Using Loop:')
print(l)
print(l[0])
print(l[1])
print(l[2])
for i in l[3]:
    print(i)




print('\n--------------------------------------------------------------------------------------\n')
