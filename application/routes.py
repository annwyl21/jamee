from flask import render_template
from application import app
from application.finance import Finance

# imports and database connection here are only to make the example page work, for our actual site we are using them from the class page
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

import mysql.connector
cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='test_finance')




@app.route('/index')
def index():
    return render_template('index.html', title='ChipIn Home Page')



@app.route('/articles')
def articles():
    return render_template('articles.html', title='Articles')



@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')



@app.route('/form')
def form_page():
    return render_template('form_page.html', title='Form Page')



@app.route('/dashboard')
def dashboard():

    # create an instance of the class
    dashboard = Finance("dashboard")

    # create the list from the database and assign to a variable
    user_spending = dashboard.database_grab_list()

    # currently using hard-coded data to create graphs - this will be replaced by the above link to databases and stored procesdures when they have been written
    headers_list = ['housing', 'food and drink', 'energy bills', 'petrol or diesel', 'train fares', 'bus fares', 'eating and drinking', 'holidays', 'clothes and footwear']
    pie_user_list = [981, 372, 107, 102, 15, 35, 382, 115, 161]
    user_list = ['My Spending', 981, 372, 107, 102, 15, 35, 382, 115, 161]
    comparison_list = ['UK Average', 1054, 368, 112, 98, 18, 18, 26, 128, 181]
    
    # create a pie chart
    dashboard.create_pie(headers_list, pie_user_list)

     # create a stacked bar chart
    dashboard.create_stacked_bar(user_list, comparison_list)

    return render_template('dashboard.html', title='Dashboard', user_spending=user_spending) #key=value pairs (my_variable_on_html_page = this_thing_here_on this page)



@app.route('/admin')
def admin():
    
    # create an instance of the class
    admin = Finance("admin")

    # create the list from the database and assign to a variable
    user_spending = admin.database_grab_list()

    return render_template('admin.html', title='Admin', data_list=user_spending)







################################################################################################
# code above here - everything below here is for the example page and it is messy, sometimes intentionally messy to show our progress

@app.route('/example')
def example():
    
    # code to connect to the database, call a stored procedure and return 1 piece of data
    mycursor = cnx.cursor()
    mycursor.callproc('data_out')
    the_data = []
    for result in mycursor.stored_results():
        the_data.append(result.fetchall())
    for item in the_data:
        my_data = item.pop(0)
   
    # create an instance of the class
    use_class = Finance("example")

    # create the list from the database and assign to a variable
    list_of_data_from_database = use_class.database_grab_list()

    # use the class to create a graph
    use_class.create_pie(list_of_data_from_database)

    # created a test class and added a graph method - see example page for resulting problem that we solved by moving the class to another page
    class Test:
        def __init__(self, name):
            self.name = name
        def get_name(self):
            return f"My name is {self.name}."
        
        def create_pie(self, my_variable):
            #seaborn palette choices: deep, muted, pastel, bright, dark, and colorblind
            colours = sns.color_palette('deep')#[0:5] I think this is how many colours we want
            df = pd.DataFrame({'expenditure': [my_variable], 'spending': [100]})
            plt.figure(figsize=(6,4))
            plt.subplot()
            plt.pie(df['spending'], colors = colours, autopct='%d%%')
            plt.title("Test Pie Chart")
            plt.legend(df['expenditure'])
            plt.savefig('application/static/images/piechart1.png', transparent=True)
            #return - the class method doesn't return anything so it sends back 'None' as an output which is then displayed on our webpage
        
        def database_insert(self, value): #  not sure if this works until I get a form working
            mycursor = cnx.cursor()
            data_to_insert = value
            args=[data_to_insert]
            mycursor.callproc('add_data', args)
            cnx.commit()
        
    # create an instance of that class
    create_single_instance = Test('Some Name')

    return render_template('example.html', title='Working Example Page', call_my_class=create_single_instance, my_data=my_data) #key=value pairs (my_variable = this_thing_here)
