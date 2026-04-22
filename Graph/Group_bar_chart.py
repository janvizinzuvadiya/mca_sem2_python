import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('stationary.xlsx')
print(df)

year = [2023,2024,2025]
x = df['pen']
x1 = df['pencil']
xaxis = np.arange(len(year))
plt.bar(xaxis-0.2,x,width=0.2,label='Pen')
plt.bar(xaxis+0.2,x1,width=0.2,label='Pencil')
plt.xticks(xaxis,year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales of Pen and Pencil')
plt.legend()
plt.show()