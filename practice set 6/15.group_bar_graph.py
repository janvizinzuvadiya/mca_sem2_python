# 15. Plot the grouped bar graph using the appropriate data.

import matplotlib.pyplot as plt
import numpy as np

# data
top_brands = ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo']
revenue_2023 = [100, 85, 60, 45, 35]
revenue_2024 = [115, 95, 70, 55, 45]

x = np.arange(len(top_brands))
width = 0.35

plt.bar(x - width/2, revenue_2023, width, label='2023', color='skyblue')
plt.bar(x + width/2, revenue_2024, width, label='2024', color='lightcoral')

plt.xlabel('Top Brands')
plt.ylabel('Revenue (Billion USD)')
plt.title('Mobile Brands Revenue (2023 vs 2024)')
plt.xticks(x)
plt.legend()
plt.show()