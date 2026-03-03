# n = 1
# while n<=10:
#     print(n)
#     n+=1

# total = 0
# n = int(input('enter number:'))
# while n!=0:
#     total+=n
#     n= int(input('enter number:'))
#     print('_____',total)

# n = 5
# counter = 1
# while counter <=10:
#     a = n*counter
#     print(n, ' X ', counter , ' = ',a)
#     counter+=1

# a = 1
# while a>=1 and a<=10:
#     print(a)
#     a+=2

# a=2 
# while a>=1 and a<=10:
#     print(a)
#     a+=2

## 1 - for odd & 2 - for even

# ch = int(input('choose 1 | 2 ->'))
# if ch == 1:
#     a = 1
#     while a >= 1 and a <= 10:
#         print(a)
#         a+=2
# elif ch == 2:
#     a = 2
#     while a >=1 and a <= 10:
#         print(a)
#         a+=2
# else:
#     print("invalid input")

k = [2,6,8,9,47,3]
n = 0
while (n < len(k)):
    if k[n]%2 == 0:
        print(k[n])
    n+=1