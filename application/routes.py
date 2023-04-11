from flask import render_template, request
from application import app
from application.finance import Finance
from application.forms import BasicForm
from application.forms import DebtForm
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

# https://www.codecademy.com/learn/learn-flask/modules/flask-templates-and-forms/cheatsheet
# consider using a redirect here so the submit of the form redirects to the template
@app.route('/form', methods=['GET', 'POST'])
def form_input():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        salary = form.salary.data
        housing = form.housing.data

        if salary or housing:
        # if len(salary) == 0 or len(housing) == 0:
            error = 'Please fill in the required Salary and Housing fields.'
        else:
            return 'Thank you!'
            # new_person_id = DATA_PROVIDER.add_person(first_name, last_name)
            #
            # success = 'Person with ID ' + str(new_person_id) + ' was created. Thank you!'
            # return render_template('success.html', success_message=success)

    return render_template('form.html', title='Form Page', form=form, message=error)


@app.route('/dashboard')
def dashboard():

    dashboard = Finance('dashboard')

    comparison_list = DATA_PROVIDER.get_average_monthly_expense_data_for_graph()
    comparison_list.insert(0, 'UK Average')

    # currently using hard-coded user data to create graphs
    headers_list = ['housing', 'food and drink', 'energy bills', 'petrol or diesel', 'train fares', 'bus fares', 'eating and drinking', 'holidays', 'clothes and footwear']
    pie_user_list = [981, 372, 107, 102, 15, 35, 382, 115, 161]
    user_list = ['My Spending', 981, 372, 107, 102, 15, 35, 382, 115, 161]
    
    # create a pie chart
    dashboard.create_pie(headers_list, pie_user_list)

    # create a stacked bar chart using data pulled from the database
    dashboard.create_stacked_bar(user_list, comparison_list)

    # grab data to create average UK spending table
    av = DATA_PROVIDER.get_average_monthly_expense_data_for_page_table()

    return render_template('dashboard.html', title='Dashboard', uk_average=av) #key=value pairs (my_variable_on_html_page = this_thing_here_on this page)




@app.route('/admin')
def admin():
    average_debt_data = DATA_PROVIDER.average_debt_report() # returns a decimal object
    average_debt = int(average_debt_data) # recast decimal object as an integer
    average = f"{average_debt:,.02f}" # make the integer a formatted string with thousand separator and 2 decimal places for pence
    debt_type_frequency = DATA_PROVIDER.frequency_debt_report()    
    Finance('report').generate_debt_report(average_debt_data, debt_type_frequency)
    return render_template('admin.html', title='Admin', average_debt_data = average, debt_type = debt_type_frequency)



@app.route('/debt_calculator_form', methods=['GET', 'POST'])
def calculate_debt():
    external_link_investopedia = 'https://www.investopedia.com/terms/d/debt.asp'
    debt_info = []
    error = ''
    form = DebtForm()
    if request.method == 'POST':
        debt_type = form.debt_type.data
        debt_amount = form.debt_amount.data
        debt_interest = form.debt_interest.data
        debt_term = form.debt_term.data
        debt_monthsyears = form.monthsyears.data
        debt_info += [debt_amount, debt_interest, debt_term, debt_monthsyears, debt_type]
        #print(debt_info)
        if not debt_amount or not debt_interest or not debt_term:
            # if any of those are False/ empty
            error = 'please enter values'
        else:
            new_debt_id = DATA_PROVIDER.add_debt_data(debt_amount, debt_type)
            dc = Finance('dc').simple_debt_calculator(debt_info)
            debt_info += [dc, new_debt_id]
            debt_info[5] = f"{debt_info[5]:,.02f}"
            return render_template('debt_calculator.html', debt_info=debt_info)
    return render_template('debt_calculator_form.html', form=form, message=error, external_link_investopedia=external_link_investopedia)




# Repeated Routes to Different Benefits
@app.route('/<benefit_name>')
def benefits(benefit_name):
    # Grab 3 pieces of information; url-endpoint, how-data and what-data to auto-complete fields
    unpacked_benefit_data_tuple = DATA_PROVIDER.get_benefits_data(benefit_name)
    if benefit_name == 'child-benefit':
        return render_template('articles.html', title='Child Benefit', data=unpacked_benefit_data_tuple)
    elif benefit_name == 'housing-benefit':
        return render_template('articles.html', title='Housing Benefit', data=unpacked_benefit_data_tuple)
    elif benefit_name == 'employment-support-allowance':
        return render_template('articles.html', title='ESA', data=unpacked_benefit_data_tuple)
    elif benefit_name == 'jobseekers-allowance':
        return render_template('articles.html', title='JSA', data=unpacked_benefit_data_tuple)
    elif benefit_name == 'universal-credit':
        return render_template('articles.html', title='Universal Credit', data=unpacked_benefit_data_tuple)
    else:
        return render_template('index.html', title='Home Page')





