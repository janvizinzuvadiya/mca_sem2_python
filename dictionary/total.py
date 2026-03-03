# ask stiudent to enter the number of elements in dictionary and then ask user to enter key and value and store it in dictionary and print the dictionary
n = int(input("Enter the number of elements in dictionary: "))
d = {}
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print(d)

# enter subject name and get marks

sub = input("Enter subject name: ")
if sub in d:
    print("Marks in", sub, "is", d[sub])
else:
    print("Subject not found in dictionary")

a1  = d.get(sub , -1)
if a1 == -1:
    print("Subject not found in dictionary")
else:
    print("Marks in", sub, "is", a1)