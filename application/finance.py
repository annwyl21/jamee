# import the data manipulation and visualisation tools
import pandas as pd
from matplotlib import pyplot as plt

# import a module to connect to sql and open a local connection to the local server assigned to the variable 'cnx'
import mysql.connector
cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='test_finance')

# create a class
class Finance:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return f"My name is {self.name}."
    
    # code to connect to the database, call a stored procedure and return a list of pieces of data
    def database_grab_list(self):
        mycursor = cnx.cursor()
        mycursor.callproc('data_out_list')
        data_list = []
        for result in mycursor.stored_results():
            for returned_list in result:
                for tuple in returned_list: 
                    list_item = tuple
                    data_list.append(list_item)
        return data_list
        # tells the database connection where to look and assigns that to a variable
        # uses that variable to tell the database connection to run a stored procedure
        # stored results takes the data now stored in the mycursor variable as an iterable
        # cycles through that list and unpacks the tuples
        # collects the strings and adds them into the empty list and returns the list

    # code to create a pie chart using a list
    def create_pie(self, my_list):
        df = pd.DataFrame({'expenditure': my_list, 'spending': [50, 50]})
        plt.figure(figsize=(6,4))
        plt.subplot()
        plt.pie(df['spending'], autopct='%d%%')
        plt.axis('equal')
        plt.title("Test Pie Chart")
        plt.legend(df['expenditure'], loc='upper right', bbox_to_anchor=(1,1), fontsize=7)
        plt.savefig('application/static/images/piechart2.png', transparent=True)
        # creates a dataframe that matplot can use
        # creates the size of the pie chart
        # tells the computer to create the pie chart
        # which data to use and to display a whole figure percentage
        # put that pie chart (with a transparent background) in a saved file 

    
