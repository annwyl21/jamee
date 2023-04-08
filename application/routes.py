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

    dashboard = Finance('dashboard')

    # currently using hard-coded data to create graphs - this will be replaced by the above link to databases and stored procesdures when they have been written
    headers_list = ['housing', 'food and drink', 'energy bills', 'petrol or diesel', 'train fares', 'bus fares', 'eating and drinking', 'holidays', 'clothes and footwear']
    pie_user_list = [981, 372, 107, 102, 15, 35, 382, 115, 161]
    user_list = ['My Spending', 981, 372, 107, 102, 15, 35, 382, 115, 161]
    comparison_list = ['UK Average', 1054, 368, 112, 98, 18, 18, 26, 128, 181]
    
    # create a pie chart
    dashboard.create_pie(headers_list, pie_user_list)

    # create a stacked bar chart
    dashboard.create_stacked_bar(user_list, comparison_list)

    return render_template('dashboard.html', title='Dashboard') #key=value pairs (my_variable_on_html_page = this_thing_here_on this page)




@app.route('/admin')
def admin():
    
      return render_template('admin.html', title='Admin')




# Repeated Routes to Different Benefits
@app.route('/<benefit_name>')
def benefits(benefit_name):
    
    if benefit_name == 'child_benefit':
        return render_template('articles.html', title='Child Benefit')
    elif benefit_name == 'housing_benefit':
        return render_template('articles.html', title='Housing Benefit')
    elif benefit_name == 'esa':
        return render_template('articles.html', title='ESA')
    elif benefit_name == 'jsa':
        return render_template('articles.html', title='JSA')
    elif benefit_name == 'universal_credit':
        return render_template('articles.html', title='Universal Credit')
    else:
        return render_template('articles.html', title='benefit_cap')


