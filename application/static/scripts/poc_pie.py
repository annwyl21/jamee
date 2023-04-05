import pandas as pd
from matplotlib import pyplot as plt

# creates a dataframe that matplot can use
df = pd.DataFrame({
    'expenditure': ['housing', 'food and drink', 'energy bills', 'petrol or diesel', 'train fares', 'bus fares', 'eating and drinking', 'holidays', 'clothes and footwear'],
    'spending': [368, 771, 112, 98, 18, 26, 285, 128, 181]
})

# creates the size of the pie chart
plt.figure(figsize=(6,4))
# tells the computer to create the pie chart
plt.subplot()
# which data to use and to display a whole figure percentage
plt.pie(df['spending'], autopct='%d%%')
plt.axis('equal')
plt.title("Spending distribution for Average UK Household - Renting")
plt.legend(df['expenditure'], loc='upper right', bbox_to_anchor=(1,1), fontsize=7)

# put that pie chart in a saved file
plt.savefig('application/static/images/piechart.png')
