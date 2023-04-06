# import the data manipulation and visualisation tools
import pandas as pd
from matplotlib import pyplot as plt

# create a class
class Finance:

    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return f"My name is {self.name}."
    
    def create_pie(self, my_list):
    # creates a dataframe that matplot can use
    df = pd.DataFrame({'expenditure': my_list, 'spending': [50, 50]})
    # creates the size of the pie chart
    plt.figure(figsize=(6,4))
    # tells the computer to create the pie chart
    plt.subplot()
    # which data to use and to display a whole figure percentage
    plt.pie(df['spending'], autopct='%d%%')
    plt.axis('equal')
    plt.title("Test Pie Chart")
    plt.legend(df['expenditure'], loc='upper right', bbox_to_anchor=(1,1), fontsize=7)
    # put that pie chart in a saved file
    plt.savefig('application/static/images/piechart.png', transparent=True)
    # return the image
    #return - what to return to remove the None

    
