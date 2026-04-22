import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_excel('stationary.xlsx')
print(df)

year = [2023,2024,2025] 
x = df['Pen']
x1 = df['Pencil']

xaxis = np.arange(len(year))
plt.bar(xaxis,x,label='Pen')
plt.bar(xaxis,x1,bottom=x,label='Pencil')
plt.xticks(xaxis,year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales of Pen and Pencil')
plt.legend()
plt.show()