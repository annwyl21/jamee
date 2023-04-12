# import the data manipulation and visualisation tools
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

# create a class
class Finance:

    def debt_calculator(self, debt_data):
        monthsoryears = debt_data[5]
        debt_term = debt_data[4]
        interest_rate = debt_data[3]
        debt_amount = debt_data[1]
        if monthsoryears == 'months':
            loan_term = debt_term
        else:
            loan_term = debt_term*12
        interest_rate = interest_rate/100
        annual_interest = int(debt_amount) * interest_rate
        monthly_interest = annual_interest/12        
        total_interest = monthly_interest*loan_term
        return total_interest + int(debt_amount)
    
    def savings_calculator(self, savings_data):

        
        interest_rate = savings_data[4]/100
        principal_amount = savings_data[1]
        savings_term_in_years = savings_data[5]
        monthly_amount_saved = savings_data[3]

        interest = principal_amount*interest_rate*savings_term_in_years
        saved = (savings_term_in_years*12)*monthly_amount_saved

        return principal_amount + saved + interest

    def dashboard_weekly_calculator(self, test_list):
        # ready to code
        return [231, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def dashboard_annual_calculator(self, test_list):
        return [12000, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def generate_debt_report(self, average_debt_data, debt_type_frequency):
        average_debt_data = f"{average_debt_data:,.2f}"
        with open('./file_output/debt_file.txt', 'w') as debt_file:
            debt_file.write("Debt Calculator\nWhen people visit our site they use our debt calculator to find out how much they will repay in total over the repayment period.\nThe average amount of debt people search for is GBP" + average_debt_data + ".\nThose debts are usually in the form of a " + debt_type_frequency[0][0] + '.\n')
        with open('./file_output/debt_file.txt', 'a') as still_debt_file:
            for tuple_item in debt_type_frequency:
                still_debt_file.write(str(tuple_item[1]) + ' searches about a ' + tuple_item[0] + '\n')


    # code to create a pie chart using a list
    def create_pie(self, headers_list, user_list):
        plt.switch_backend('Agg') 
        colours = sns.color_palette('deep')
        df = pd.DataFrame({'expenditure': headers_list, 'spending': user_list})
        plt.figure(figsize=(6,4))
        plt.subplot()
        plt.pie(df['spending'], colors=colours, autopct='%d%%')
        plt.axis('equal')
        #plt.title("Test Pie Chart")
        #plt.legend(df['expenditure'], loc='upper right', bbox_to_anchor=(1,1), fontsize=7)
        plt.savefig('application/static/images/piechart.png', transparent=True)
        # use beautiful seaborn colours
        # creates a dataframe that matplot can use
        # creates the size of the pie chart
        # tells the computer to create the pie chart
        # which data to use and to display a whole figure percentage
        # put that pie chart (with a transparent background) in a saved file 


    # code to create a stacked bar chart using a list
    def create_stacked_bar(self, user_list, comparison_list):
        #c = sns.color_palette('deep')
        plt.switch_backend('Agg') 
        expenditure = [user_list[0], comparison_list[0]]
        housing = [user_list[1], comparison_list[1]]
        groceries = [user_list[2], comparison_list[2]]
        bills = [user_list[3], comparison_list[3]]
        fuel = [user_list[4], comparison_list[4]]
        train = [user_list[5], comparison_list[5]]
        bus = [user_list[6], comparison_list[6]]
        cafe = [user_list[7], comparison_list[7]]
        holiday = [user_list[8], comparison_list[8]]
        clothes = [user_list[9], comparison_list[9]]
        x = range(2)
        bills_bottom = np.add(housing, groceries)
        fuel_bottom = np.add(bills_bottom, bills) 
        train_bottom = np.add(fuel_bottom, fuel)
        bus_bottom = np.add(train_bottom, train)
        cafe_bottom = np.add(bus_bottom, bus)
        holiday_bottom = np.add(cafe_bottom, cafe)
        clothes_bottom = np.add(holiday_bottom, holiday)
        plt.figure(figsize=(10, 8))
        ax = plt.subplot()
        plt.bar(x, housing)
        plt.bar(x, groceries, bottom = housing)
        plt.bar(x, bills, bottom = bills_bottom)
        plt.bar(x, fuel, bottom = fuel_bottom) 
        plt.bar(x, train, bottom = train_bottom)
        plt.bar(x, bus, bottom = bus_bottom)
        plt.bar(x, cafe, bottom = cafe_bottom)
        plt.bar(x, holiday, bottom = holiday_bottom)
        plt.bar(x, clothes, bottom = clothes_bottom)
        ax.set_xticks(range(len(expenditure)))
        ax.set_xticklabels((expenditure))
        #plt.title("Stacked bar chart: Comparison of Spending Distribution for Mortgage Paying Households")
        plt.xlabel("Comparison")
        plt.ylabel("Spending Type in £'s")
        #plt.legend(("Housing", "Food and Drink", "Energy Bills", "Fuel", "Train Fares", "Bus Fares", "Eating and Drinking", "Holidays", "Clothes and Footwear"))
        plt.savefig('application/static/images/barstack.png', transparent=True)
        # this can be created using a dataframe but I didn't learn that, I might have to to use the nice seaborn colours
        # assign the list variables to the appropriate y_axis categories
        # define the number of columns in the stacked bar chart
        # calculations to add up the height of the stacks
        # each time taking the height of the existing stack and adding on the previous stacked bar
        # then create the graph, define the size of the output and the bars to stack up for 2 columns
        # for example to display the cost of fuel, use the start position (bottom) for the stacked bar as the sum of all the values (fuel_bottom) of the heights of the other bars
        # just have 2 markers (x-ticks) on the x-axis because the length of the expenditure list is 2
        # use the strings in the expenditure list to label (xticklabels) those markers
        # add titles, legend etc and save






