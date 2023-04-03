import pandas as pd
from matplotlib import pyplot as plt

# creates a dataframe that matplot can use
df = pd.DataFrame({
    'expenditure': ['rent', 'council tax', 'bills', 'groceries', 'other'],
    'spending': [500, 80, 100, 50, 10]
})

# creates the size of the pie chart
plt.figure(figsize=(6,4))
# tells the computer to create the pie chart
plt.subplot()
# which data to use and to display a whole figure percentage
plt.pie(df['spending'], autopct='%d%%')
plt.title("Pie Chart to show spending distribution")
plt.legend(df['expenditure'], loc='upper right')

# put that pie chart in a saved file
plt.savefig('application/static/piechart.png')
