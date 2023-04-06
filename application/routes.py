from flask import render_template, redirect
from application import app
from application.finance import Finance

# imports and database connection here are only to make the example page work, for our actual site we are using them from the class page
import pandas as pd
from matplotlib import pyplot as plt
import mysql.connector
cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='test_finance')




@app.route('/')
def home():
    return render_template('index.html', title='ChipIn Home Page')

# This is a good place to use a redirect because / and /index are both routes to the home page, I think?

@app.route('/index')
def index():
    return render_template('index.html', title='ChipIn Home Page')



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

    return render_template('dashboard.html', title='Dashboard', user_spending=user_spending) #key=value pairs (my_variable_on_html_page = this_thing_here_on this page)



@app.route('/admin')
def admin():
    
    # create an instance of the class
    admin = Finance("admin")

    # create the list from the database and assign to a variable
    user_spending = dashboard.database_grab_list()

    return render_template('admin.html', title='Admin', data_list=user_spending)



# Repeated Routes to Benefits - Pretty Sure there is a better way to do this, they just feed in different data into the same page, there must be a conditional!
@app.route('/child_benefit')
def child_benefit():
    child_benefit = Finance("child_benefit")
    list_of_information_to_display_on_page = child_benefit.database_grab_list()
    return render_template('articles.html', title='Child Benefit', variable=list_of_information_to_display_on_page[0])

@app.route('/housing_benefit')
def housing_benefit():
    housing_benefit = Finance("housing_benefit")
    list_of_information_to_display_on_page = housing_benefit.database_grab_list()
    return render_template('articles.html', title='Housing Benefit', variable=list_of_information_to_display_on_page[1])

@app.route('/esa')
def esa():
    esa = Finance("esa")
    list_of_information_to_display_on_page = esa.database_grab_list()
    return render_template('articles.html', title='ESA', variable=list_of_information_to_display_on_page[0])

@app.route('/jsa')
def jsa():
    jsa = Finance("jsa")
    list_of_information_to_display_on_page = jsa.database_grab_list()
    return render_template('articles.html', title='JSA', variable=list_of_information_to_display_on_page[1])

@app.route('/universal_credit')
def universal_credit():
    universal_credit = Finance("universal_credit")
    list_of_information_to_display_on_page = universal_credit.database_grab_list()
    return render_template('articles.html', title='Universal Credit', variable=list_of_information_to_display_on_page[0])

@app.route('/benefit_cap')
def benefit_cap():
    benefit_cap = Finance("benefit_cap")
    list_of_information_to_display_on_page = benefit_cap.database_grab_list()
    return render_template('articles.html', title='benefit_cap', variable=list_of_information_to_display_on_page[1])







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
            df = pd.DataFrame({'expenditure': [my_variable], 'spending': [100]})
            plt.figure(figsize=(6,4))
            plt.subplot()
            plt.pie(df['spending'], autopct='%d%%')
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
