# 13. Take five income source of the Government and display it on the pie chart.

import matplotlib.pyplot as plt

# data of income sources
sources = ["Income Tax", "GST", "Corporate Tax", "Custom Duty", "Excise Duty"]
values = [30, 25, 20, 15, 10]

# create pie chart
plt.pie(values, labels=sources, autopct='%1.1f%%')

# title
plt.title("Government Income Sources")

# show chart
plt.show()