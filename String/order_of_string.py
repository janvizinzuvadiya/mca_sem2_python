# display all element s of the  string in forward and reverse order

s = 'Hello'
#while Loop
#forward:

n = len(s)
i = 0
while i<n:
    print(s[i],end=' ')
    i+=1
print()

#reverse
i = 1
n = len(s)
while(i<=n):
    print(s[-i],end=' ')
    i+=1


#for Loop
for i in s:
    print(i,end='')
print()

#reverse
for i in s[::-1]:
    print(i,end='')