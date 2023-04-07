from flask import render_template, request
from application import app
from application.finance import Finance
from application.forms import BasicForm
from application.data_provider_service import DataProviderService

# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title='ChipIn Home Page')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/form', methods=['GET', 'POST'])
def form_input():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        salary = form.salary.data
        rent = form.rent.data

        if len(salary) == 0 or len(rent) == 0:
            error = 'Please fill in the required Salary and Rent/Mortgage fields.'
        else:
            return 'Thank you!'
            # new_person_id = DATA_PROVIDER.add_person(first_name, last_name)
            #
            # success = 'Person with ID ' + str(new_person_id) + ' was created. Thank you!'
            # return render_template('success.html', success_message=success)

    return render_template('form.html', title='Form Page', form=form, message=error)


@app.route('/dashboard')
def dashboard():

    # create an instance of the class
    dashboard = Finance("dashboard")

    # create the list from the database and assign to a variable
    # user_spending = dashboard.database_grab_list()

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
    
      return render_template('admin.html', title='Admin')




# Repeated Routes to Different Benefits
@app.route('/<benefit_name>')
def benefits(benefit_name):
    info = Finance("benefits").database_grab_list()
    if benefit_name == 'child_benefit':
        return render_template('articles.html', title='Child Benefit', variable=info[0])
    elif benefit_name == 'housing_benefit':
        return render_template('articles.html', title='Housing Benefit', variable=info[1])
    elif benefit_name == 'esa':
        return render_template('articles.html', title='ESA', variable=info[0])
    elif benefit_name == 'jsa':
        return render_template('articles.html', title='JSA', variable=info[1])
    elif benefit_name == 'universal_credit':
        return render_template('articles.html', title='Universal Credit', variable=info[0])
    else:
        return render_template('articles.html', title='benefit_cap', variable=info[1])







################################################################################################
# code above here - everything below here is for the example page and it is messy, sometimes intentionally messy to show our progress

# import mysql.connector
# cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='test_finance')

@app.route('/example', methods=['GET', 'POST'])
def example():
    
    # code to connect to the database, call a stored procedure and return 1 piece of data
    # mycursor = cnx.cursor()
    # mycursor.callproc('data_out')
    # the_data = []
    # for result in mycursor.stored_results():
    #     the_data.append(result.fetchall())
    # for item in the_data:
    #     my_data = item.pop(0)

    # created a test class and added a graph method - see example page for resulting problem that we solved by moving the class to another page
    class Test:
        def __init__(self, name):
            self.name = name
        def get_name(self):
            return f"My name is {self.name}."
        
        def create_pie_chart(self, my_variable):
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
        
        # def database_insert(self, value): #  not sure if this works until I get a form working
        #     mycursor = cnx.cursor()
        #     data_to_insert = value
        #     args=[data_to_insert]
        #     mycursor.callproc('add_data', args)
        #     cnx.commit()
        
    return render_template('example.html', title='Working Example Page') #key=value pairs (my_variable = this_thing_here)

