# import mysql.connector

# con = mysql.connector.connect(host='localhost',user='root',password='',database='test')

# cur = con.cursor()

# cur.execute("create table stud(name varchar(255), age int)")

# cur.execute("insert into stud values('amily',22),('disha',23),('siddhesh',21)")

# con.commit()

# cur.execute('select * from stud where name = %s',('disha',))

# result = cur.fetchall()

# print(result)





























# Practice set 6
# 1. Create a file with file name sample.txt,
# accept some data from the user and store it in the file.

# data = input("Enter values to insert into Text File->")
# f = open('sample.txt','w')
# f.write(data)
# print(f'Successfully written {data} into the file sample.txt')
# f.close()

# 2. Display the data stored in the sample.txt file (created in question 1).

# f = open('sample.txt','r')
# out = f.read()
# print(out)
# f.close()

# 3. Accept some data from the user and append it into the file sample.txt 
# (created in question 1), also the data in the file.

# data = input("enter data->")
# f = open('sample.txt','a')
# f.write(data)
# f.close()

# 4. Accept the file name from the user, check the availability of the file:
#  i), If the file exists display the data on the screen,
#  ii). If the file is not available, display the appropriate message.

# import os

# fname = input('Enter File name->')
# if(os.path.isfile(fname)):
#     with open(fname,'r') as f:
#         data = f.read()
#         print(data)
# else:
#     print('File not found')

# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: 
    # i). No. of characters,
    # ii). No. of words and
    # iii). No. of lines
# b. If the file does exist, than display the appropriate message.

# import os

# fname = input('enter fiel name->')

# if(os.path.isfile(fname)):
#     line_count = 0
#     char_count = 0
#     word_count = 0

#     f = open(fname,'r')
    
#     for line in f:
#         line_count += 1
#         words = line.split()
#         word_count += len(words)
#         char_count += len(line)

#     print('lines->',line_count)
#     print('words->',word_count)
#     print('character->',char_count)
#     f.close()
# else:
#     print('File not found')
    
# 6. Create and open the binary file with 'with' option. 
# Store names of all the subjects you study in semester 
# 2. Ask user to enter the subject number they wanted to see and display that subject name.









# 7. Create a file named 'img1', store image into it. 
# Open another file named 'img2", copy the same image as in the file 'img1'. 
# Also store both files into the zip file named 'imp img.

# f = open('img1.jpg','rb')
# data = f.read()

# f1 = open('img2.jpg','wb')
# f1.write(data)

# f.close()
# f1.close()

# import zipfile

# z = zipfile.ZipFile('img.zip','w',zipfile.ZIP_DEFLATED)
# z.write('img1.jpg')
# z.write('img2.jpg')
# z.close()



# 8. Create a file with 'with' option, name it as 'marks.dat".
# 1). Accept subject name and marks from the user, 
# store the data in the file. ii. Give three options to the user: 
# a). To view whole file, 
# b). Accept and edit the marks of a subject user want to change.
# iii). Exit








# 9. Create a regular expression that:
# a). Identifies and display the string starting with 's' and having 4 characters.
# b). Splits the string where some special characters are found.
# c). Display the word starting with number.
# d). Display the word having 3 or 4 or 5 characters.
# e). Display only the dates from the string.
# f). Create a string with name of the person and his Aadhar number, display only Aadhar number.
# g). Display all the words that starts with 'at' or 'ap',
# h). Check if the string starts with 'at' than display appropriate message and otherwise.

# import re

# str = "at sun1 snow atm attop apple 3ways 23-04-2025 !! atmosphere dd sushi apartment 04-02-2004 # 7days hello@ &kite"
# ans = re.findall(r'\bs\w{3}\b',str)
# print(ans)
# ans = re.split(r'[^\w]+',str)
# print(ans)
# ans = re.findall(r'\b\d\w*\b',str)
# print(ans)
# ans = re.findall(r'\b\w{3,5}\b' ,str)
# print(ans)
# ans = re.findall(r'\b\d{2}-\d{2}-\d{4}\b',str)
# print(ans)

# str1 = "bhimsen 2003-4532-4875"
# ans = re.findall(r'\b\d{4}-\d{4}-\d{4}\b',str1)  
# print(ans)

# ans = re.findall(r'\ba[tp]\w+\b',str)
# print(ans)

# ans = re.match(r'at',str)
# if(ans):
#     print("String starts with 'at'")
# else:
#     print("String does not start with 'at'")


# 11. Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform
# following operations:
# a). Display first three records
# b). Display last five records
# c). Display only Name and City
# d). Display employee who belongs to Mumbai
# e). Display employee name who belongs to Mumbai
# f). Display employee whose salary is more than 25000

# dict = {
#     'e1': {'empid': 101, 'name': 'John', 'city': 'New York', 'salary': 5000},
#     'e2': {'empid': 102, 'name': 'Jane', 'city': 'London', 'salary': 60000},
#     'e3': {'empid': 103, 'name': 'Bob', 'city': 'Mumbai', 'salary': 70000},
#     'e4': {'empid': 104, 'name': 'Alice', 'city': 'Tokyo', 'salary': 800},
#     'e5': {'empid': 105, 'name': 'Mike', 'city': 'Mumbai', 'salary': 9000},
#     'e6': {'empid': 106, 'name': 'Sarah', 'city': 'Berlin', 'salary': 100000},
#     'e7': {'empid': 107, 'name': 'David', 'city': 'Madrid', 'salary': 110000},
#     'e8': {'empid': 108, 'name': 'Emily', 'city': 'Rome', 'salary': 120000},
#     'e9': {'empid': 109, 'name': 'Chris', 'city': 'Mumbai', 'salary': 1300},
#     'e10': {'empid': 110, 'name': 'Lisa', 'city': 'Beijing', 'salary': 1400}
# }
# import pandas as pd

# df = pd.DataFrame(dict).T
# print(df.head(3))
# print(df.tail(5))
# print(df[['name','city']])
# print(df[df['city']=='Mumbai'])
# print(df[df['salary']>25000])

# 12. Create an xlsx file store marks of five subjects, plot the data on the bar graph.

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     'Subject': ['Python', 'Data Structures', 'Operating Systems', 'Networking', 'Mathematics'],
#     'Marks': [85, 92, 78, 88, 95]
# }

# df = pd.DataFrame(data)
# df.to_excel('Subject_Marks.xlsx', index=False)

# df = pd.read_excel('data.xlsx')
# print(df)

# x = df['subject']
# y = df['mark']
# colors = ['pink', 'lightgreen', 'lightblue', 'lightgray', 'lightyellow']

# plt.bar(x,y , color=colors)
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.title('Subejct Marks Graph')

# plt.show()

# 13. Take five income source of the Government and display it on the pie chart.

# import matplotlib.pyplot as plt
# x = ['Income Tax','GST','Corporate Tax','Customs Duty','Excise Duty']
# y = [30,25,20,15,10]

# plt.pie(y,labels=x,colors=colors,startangle=140)
# plt.show()

# 14. Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.
import matplotlib.pyplot as plt

# x = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
# y = [25000,28000,30000,32000,35000,38000,40000,42000,45000,48000,50000,52000]

# plt.plot(x,y,marker='o',color='green',linestyle=':')
# plt.xlabel('Year')
# plt.ylabel('BSE Index')
# plt.title('BSE Index in Last 10 Years')
# plt.show()

# 15. Plot the grouped bar graph using the appropriate data.

import numpy as np
import matplotlib.pyplot as plt

x = ['Maths','Physics','Chemistry','Eng']
y1 = [80,90,85,70]
y2 = [82,88,83,72]
y3 = [84,92,87,75]

xaxis = np.arange(len(x))

width = 0.4

plt.bar(xaxis -0.2,y1,width, label='Y1')
plt.bar(xaxis +0.2,y2,width, label='Y2')

plt.xlabel('Subjects')
plt.ylabel('Marks')
# plt.xticks(xaxis,x)
plt.title('Marks of 3 Students in 4 Subjects')

plt.show()