from matplotlib import pyplot as plt
import numpy as np

expenditure = ['My Spending', 'UK Average']
housing = [981, 1054]
groceries = [372, 368]
bills = [107, 112]
fuel = [102, 98]
train = [15, 18]
bus = [35, 26]
cafe = [382, 128]
holiday = [115, 128]
clothes = [161, 181]

# number of columns in the stacked bar chart
x = range(2)

# calculations to add up the height of the stacks
bills_bottom = np.add(housing, groceries)
fuel_bottom = np.add(bills_bottom, bills) # each time taking the height of the existing stack and adding on the previous stacked bar
train_bottom = np.add(fuel_bottom, fuel)
bus_bottom = np.add(train_bottom, train)
cafe_bottom = np.add(bus_bottom, bus)
holiday_bottom = np.add(cafe_bottom, cafe)
clothes_bottom = np.add(holiday_bottom, holiday)

# code to create the graph
plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(x, housing)
plt.bar(x, groceries, bottom = housing)
plt.bar(x, bills, bottom = bills_bottom)
plt.bar(x, fuel, bottom = fuel_bottom) # for 2 columns, display the cost of fuel, use the start position for the stacked bar as the sum of all the values of the heights of the other bars
plt.bar(x, train, bottom = train_bottom)
plt.bar(x, bus, bottom = bus_bottom)
plt.bar(x, cafe, bottom = cafe_bottom)
plt.bar(x, holiday, bottom = holiday_bottom)
plt.bar(x, clothes, bottom = clothes_bottom)

# just have 2 markers on the x-axis because the length of the expenditure list is 2
ax.set_xticks(range(len(expenditure)))
# use the strings in the expenditure list to label those markers
ax.set_xticklabels((expenditure))

plt.title("Stacked bar chart: Comparison of Spending Distribution for Mortgage Paying Households")
plt.xlabel("Comparison")
plt.ylabel("Spending Type in £'s")
plt.legend(("Housing", "Food and Drink", "Energy Bills", "Fuel", "Train Fares", "Bus Fares", "Eating and Drinking", "Holidays", "Clothes and Footwear"))

plt.savefig('application/static/barstack.png')

