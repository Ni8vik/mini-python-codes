import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'age': [23, 45, 31, 35, 50],
    'salary': [50000, 80000, 60000, 75000, 90000],
    'department': ['IT', 'Sales', 'IT', 'Sales', 'HR']
})

# Simple scatter plot
sns.scatterplot(x='age', y='salary', hue='department', data=data)
plt.show()

# Boxplot
sns.boxplot(x='department', y='salary', data=data)
plt.show()