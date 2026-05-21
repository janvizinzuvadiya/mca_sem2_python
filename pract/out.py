import matplotlib.pyplot as plt

x = [45,23,54,68,98,24]
y = ["a","b","c","d","e","f"]

plt.bar(y,x)
plt.title("Bar Chart")
plt.show()

# x = [23,45,65,23,78]
# y = ['pen','pencil','calculator','books','eraser']

# clr = ['r','p','b','y','c']
# plt.pie(x,labels=y,colors=clr)

# plt.title("Pie Chart")
# plt.show()

# import matplotlib.pyplot as plt
# # Sample data
# hours = [1, 2, 3, 4, 5, 6, 7, 8]
# scores = [35, 40, 50, 55, 65, 70, 75, 85]
# # Create scatter plot
# plt.scatter(hours, scores)
# # Labels and title
# plt.xlabel("Study Hours") 
# plt.ylabel("Exam Scores")
# plt.title("Study Hours vs Exam Scores")
# #Show grid for better readability
# plt.grid()
# # Display plot
# plt.show()


#Create an area plot
# import numpy as np
# import matplotlib.pyplot as plt
# #create data
# x = range(1,6)
# y = [1,4,6,2,4]
# #area plot
# plt.fill_between(x,y)
# plt.title('Area plot')
# plt.show()

# Stacked bar graph
# import matplotlib.pyplot as plt
# import numpy as np
# # Data
# months = ['Jan', 'Feb', 'Mar']
# pencil = [50, 60, 70]
# pen = [30, 40, 50]
# # X-axis positions
# x = np.arange(len(months))
# # Stacked bar graph
# plt.bar(x, pencil, label='Pencil')
# plt.bar(x, pen, bottom=pencil, label='Pen') # stacked on top
# # Labels and title
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Monthly Stationary Sales")
# # X-axis ticks
# plt.xticks(x, months)
# # Legend
# # plt.legend()
# plt.show()


#Calling the function
# lst=[10,11,12,13,14]
# print(lst,id(lst))
# def modify(lst):
#     lst.append(15)
#     print(lst,id(lst))
# modify(lst)
# print(lst,id(lst))

# [10, 11, 12, 13, 14] 132528603843392
# [10, 11, 12, 13, 14, 15] 132528603843392
# [10, 11, 12, 13, 14, 15] 132528603843392




# Program to pass an integer to a fucnction and modify it.

# def modify(a):
#     a=16
#     print('The value of a inside the function is',a, id(a))

# #Calling the function
# a=7
# modify(a)
# print('The value of a outside the function is',a,id(a))

# Output:
# The value of a inside the function is 16 <68571360>
# The value of a outside the function is 7 <68571120>