# 12. Create an xlsx file store marks of five subjects, plot the data on the bar graph.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dataframe with marks in five subjects
df = pd.DataFrame({
    "Subject": ["Maths", "Science", "English", "History", "Geography"],
    "Marks": [85, 90, 78, 82, 76]
})
print(df)

# Plot the data on a bar graph
plt.figure(figsize=(8, 6))
plt.bar(df["Subject"], df["Marks"])

# Add labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks of Five Subjects")

# Display the graph
plt.show()