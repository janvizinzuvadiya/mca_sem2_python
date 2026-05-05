# 11. Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform
# following operations:
# a). Display first three records.
# b). Display last five records
# c). Display only Name and City.
# d). Display employee who belongs to Mumbai
# e). Display employee name who belongs to Mumbai
# f). Display employee whose salary is more than 25000

# creating dictionary with 10 employee records

employees = {
    1: {"name": "Ravi", "city": "Mumbai", "salary": 30000},
    2: {"name": "Amit", "city": "Delhi", "salary": 20000},
    3: {"name": "Neha", "city": "Mumbai", "salary": 28000},
    4: {"name": "Pooja", "city": "Pune", "salary": 22000},
    5: {"name": "Karan", "city": "Mumbai", "salary": 26000},
    6: {"name": "Anjali", "city": "Rajkot", "salary": 24000},
    7: {"name": "Rahul", "city": "Surat", "salary": 27000},
    8: {"name": "Sneha", "city": "Mumbai", "salary": 21000},
    9: {"name": "Vikas", "city": "Delhi", "salary": 29000},
    10: {"name": "Meena", "city": "Mumbai", "salary": 32000}
}

# convert dictionary into list for easy access
emp_list = list(employees.items())


# a) Display first three records
print("a) First three records:")
for i in emp_list[:3]:
    print(i)


# b) Display last five records
print("\nb) Last five records:")
for i in emp_list[-5:]:
    print(i)


# c) Display only Name and City
print("\nc) Name and City:")
for id, data in employees.items():
    print(data["name"], "-", data["city"])


# d) Display employee who belongs to Mumbai
print("\nd) Employees from Mumbai:")
for id, data in employees.items():
    if data["city"] == "Mumbai":
        print(id, data)


# e) Display employee name who belongs to Mumbai
print("\ne) Names of employees from Mumbai:")
for id, data in employees.items():
    if data["city"] == "Mumbai":
        print(data["name"])


# f) Display employee whose salary is more than 25000
print("\nf) Employees with salary > 25000:")
for id, data in employees.items():
    if data["salary"] > 25000:
        print(data["name"], "-", data["salary"])