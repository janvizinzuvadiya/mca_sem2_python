# 10. Do as directed:
# a). Name the package used to deal with data frame.
# b). Name the package used to deal with data .xlsx file.
# c). Name the function used to read the .csv file.
# d). Name the function used to read the xlsx file.
# e). Name the function used to read the tuple.

import pandas as pd
import numpy as np
import openpyxl

# a) Package used to deal with DataFrame
# 👉 pandas

# b) Package used to deal with .xlsx file
# 👉 openpyxl (also used with pandas)

# c) read .csv file
data = pd.read_csv("file.csv")
print(data)

# d) read .xlsx file
data = pd.read_excel("file.xlsx")
print(data)

# e) read the tuple
t = eval("(1, 2, 3)")
print(t)
