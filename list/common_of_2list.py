# find common elemetns from teo lists

print('\n--------------------------------------------------------------------------------------\n')

city1 = ['a','b','c','d']
city2 = ['a','c','r','f']

s1 = set(city1)
s2 = set(city2)

s3 = s1.intersection(s2)
common = list(s3)
print('Common Values are :',end='')
print(common)



print('\n--------------------------------------------------------------------------------------\n')
