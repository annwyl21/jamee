from flask import render_template
from application import app
#from finance import Finance # problem to solve, where does the class need to be for the application to see it

# import a module to connect to sql
import mysql.connector

# open a local connection to the local server
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

    mycursor = cnx.cursor()
    mycursor.callproc('data_out')
    the_data = []
    for result in mycursor.stored_results():
        the_data.append(result.fetchall())
    for item in the_data:
        my_data = item.pop(0)

    # create a class
    class Finance:

        def __init__(self, name):
            self.name = name
        
        def get_name(self):
            return f"My name is {self.name}."
    
    # create an instance of that class
    create_instance = Finance('Ellen')

    return render_template('dashboard.html', title='Dashboard', call_my_class=create_instance, my_data=my_data) #key=value pairs (my_variable = this_thing_here)

