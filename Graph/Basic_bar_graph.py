import matplotlib.pyplot as plt

fruits = ['Apple','Banana','Mango','Orange']
price = [100,200,300,400]

# vertical bars graph
plt.bar(fruits,price,label='Price')

# horizontal bars graph
# plt.barh(fruits,price,label='Price')

plt.xlabel('Fruits')
plt.ylabel('Price')

plt.legend()
plt.show()