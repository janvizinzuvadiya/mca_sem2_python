import numpy as np

#array

arr= np.array([4,2,5,2,4,6])
print(arr)
print(type(arr))

#modify
arr[3]=55
print(arr)

#access
print(arr[5])

print("-------------------------------------------------------------------------")

#list

lst= [3,4,44.65,"hello",'a',-9,False,4,6]
print(lst)
print(type(lst))

#modify
lst[4]="ggv";
print(lst);

#access
print(lst[6])

print("------------------------------------------------------------------------")

#sets

st = {3,5,2,4,6,5,2}
print(st)
print(type(st))

print("------------------------------------------------------------------------")

#range

rg= range(3)
print(rg)
print(type(rg))

for i in rg:
    print(i)

av= range(-4)
print(av)

for i in av:
    print(i)

print("------------------------------------------------------------------------")
