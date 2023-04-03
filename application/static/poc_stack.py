from matplotlib import pyplot as plt
import numpy as np

expenditure = ['My Spending', 'Average Spending']
rent = [500, 200]
bills = [80, 100]
council_tax = [100, 80]
groceries = [50, 80]
other = [80, 350]

# number of columns in the stacked bar chart
x = range(2)

# calculations to add up the height of the stacks
c_bottom = np.add(rent, bills)
g_bottom = np.add(c_bottom, council_tax)
o_bottom = np.add(g_bottom, groceries)

# code to create the graph
plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(x, rent)
plt.bar(x, bills, bottom = rent)
plt.bar(x, council_tax, bottom = c_bottom)
plt.bar(x, groceries, bottom = g_bottom) # for 2 columns, display the value in the groceries list, use the start position for the colour as the sum of all the values of the heights of the other bars
plt.bar(x, other, bottom = o_bottom)

# just have 2 markers on the x-axis because the length of the expenditure list is 2
ax.set_xticks(range(len(expenditure)))
# use the strings in the expenditure list to label those markers
ax.set_xticklabels((expenditure))

plt.title("Stacked bar chart showing a comparison of spending distribution")
plt.xlabel("Comparison")
plt.ylabel("Spending Type £")
plt.legend(("Rent", "Bills", "Council Tax", "Groceries", "Other"))

plt.savefig('application/static/barstack.png')

