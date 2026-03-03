s1 = int(input("Enter Student 1's Mark -> "))
s2 = int(input("Enter Student 2's Mark -> "))
s3 = int(input("Enter Student 3's Mark -> "))
s4 = int(input("Enter Student 4's Mark -> "))

print("\n--------------------------------------------------")

if s1 > s2 and s1 > s3 and s1 > s4:
    print("🏆 Student 1 scored the highest!")
    print("Marks:", s1)
elif s2 > s1 and s2 > s3 and s2 > s4:
    print("🏆 Student 2 scored the highest!")
    print("Marks:", s2)
elif s3 > s1 and s3 > s2 and s3 > s4:
    print("🏆 Student 3 scored the highest!")
    print("Marks:", s3)
elif s4 > s1 and s4 > s2 and s4 > s3:
    print("🏆 Student 4 scored the highest!")
    print("Marks:", s4)
else:
    print("Some students have equal marks or there’s a tie.")

print("--------------------------------------------------")
