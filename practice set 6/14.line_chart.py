# 14. Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.

import matplotlib.pyplot as plt

# BSE Sensex data (example values for last 10 years)
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
sensex = [28000, 26000, 34000, 36000, 41000, 48000, 59000, 61000, 65000, 72000]

# plot line chart
plt.plot(years, sensex, marker='o',linestyle='--')

# labels and title
plt.xlabel("Year")
plt.ylabel("BSE Sensex Index")
plt.title("BSE Index in Last 10 Years")

# show graph
plt.show()  