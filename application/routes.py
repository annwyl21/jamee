from flask import render_template, request
from application import app
from application.finance import Finance
from application.forms import BasicForm, DebtForm, ComparisonForm, SavingsForm
from application.data_provider_service import DataProviderService

# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()

# instantiating an object of Finance class
Finance = Finance()

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
        other = form.other.data
        food_drink = form.food_drink.data
        housing = form.housing.data
        energy = form.energy.data
        petrol = form.petrol.data
        train = form.train.data
        bus = form.bus.data
        eating = form.eating.data
        holidays = form.holidays.data
        clothes = form.clothes.data


        if not salary or not housing:
            error = 'Please fill in the required Salary and Housing fields.'
        else:
            new_data = DATA_PROVIDER.add_form_data(salary, other, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes)
            data = []
            data += [food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes]
            return render_template('dashboard.html', data=data, new_data=new_data)

    return render_template('form.html', title='Form Page', form=form, message=error)


@app.route('/dashboard')
def dashboard():

    comparison_list = DATA_PROVIDER.get_average_monthly_expense_data_for_graph()
    comparison_list.insert(0, 'UK Average')

    # currently using hard-coded user data to create graphs
    headers_list = ['housing', 'food and drink', 'energy bills', 'petrol or diesel', 'train fares', 'bus fares', 'eating and drinking', 'holidays', 'clothes and footwear']
    pie_user_list = [981, 372, 107, 102, 15, 35, 382, 115, 161]
    user_list = ['My Spending', 981, 372, 107, 102, 15, 35, 382, 115, 161]
    
    Finance.create_pie(headers_list, pie_user_list)
    Finance.create_stacked_bar(user_list, comparison_list)

    # grab data to create average UK spending table
    av = DATA_PROVIDER.get_average_monthly_expense_data_for_page_table()
    # create a dictionary to use for spending loops
    headers_to_user_input = {key:value for key, value in zip(headers_list, pie_user_list)}

    return render_template('dashboard.html', title='Dashboard', uk_average=av, user_list=headers_to_user_input) #key=value pairs (my_variable_on_html_page = this_thing_here_on this page)




@app.route('/admin')
def admin():
    average_debt_data = DATA_PROVIDER.average_debt_report() # returns a decimal object
    average_debt = int(average_debt_data) # recast decimal object as an integer
    average = f"{average_debt:,.02f}" # make the integer a formatted string with thousand separator and 2 decimal places for pence
    debt_type_frequency = DATA_PROVIDER.frequency_debt_report()   
    Finance.generate_debt_report(average_debt_data, debt_type_frequency)

    average_savings_data = DATA_PROVIDER.average_savings_report() # returns a decimal object
    average_savings = int(average_savings_data) # recast decimal object as an integer
    avg = f"{average_savings:,.02f}" # make the integer a formatted string with thousand separator and 2 decimal places for pence
    savings_type_frequency = DATA_PROVIDER.frequency_savings_report()   
    Finance.generate_savings_report(average_savings_data, savings_type_frequency)

    return render_template('admin.html', title='Reports', average_debt_data = average, debt_type = debt_type_frequency, average_savings_data=avg, savings_type=savings_type_frequency )



@app.route('/savings_calculator_form', methods=['GET', 'POST'])
def calculate_savings():
    external_link_money_saving_expert = 'https://www.moneysavingexpert.com/'
    savings_info = []
    error3 = ''
    form = SavingsForm()
    if request.method == 'POST':
        savings_lump = form.savings_lump.data
        monthly_saving_amount = form.monthly_saving_amount.data
        savings_interest = form.savings_interest.data
        savings_term = form.savings_term.data
        savings_goal = form.savings_goal.data
        if not savings_lump:
            # if any of those are False/ empty
            error3 = 'Please enter an initial lump sum and a savings goal'
        else:
            if not savings_interest:
                savings_interest = 6
            if not savings_term:
                savings_term = 20
            if not monthly_saving_amount:
                monthly_saving_amount = 0
            if not savings_goal:
                savings_goal = 'rainy day'
            new_savings_id = DATA_PROVIDER.add_savings_data(savings_lump, savings_goal, monthly_saving_amount, savings_interest, savings_term)
            savings_data = DATA_PROVIDER.get_data_from_id('savings', 'savings_total_id', new_savings_id)
            print(savings_data)
            calculated_total_savings = Finance.savings_calculator(savings_data)
            calculated_total_savings = f"{calculated_total_savings:,.02f}"
            return render_template('savings_calculator.html', total=calculated_total_savings, savings_data=savings_data)

    return render_template('savings_calculator_form.html', form=form, message=error3, external_link_money_saving_expert=external_link_money_saving_expert)


@app.route('/debt_calculator_form', methods=['GET', 'POST'])
def calculate_debt():
    external_link_investopedia = 'https://www.investopedia.com/terms/d/debt.asp'
    error = ''
    form = DebtForm()
    if request.method == 'POST':
        debt_type = form.debt_type.data
        debt_amount = form.debt_amount.data
        debt_interest = form.debt_interest.data
        debt_term = form.debt_term.data
        debt_monthsyears = form.monthsyears.data
        if not debt_amount:
            # if any of those are False/ empty follow this condition to enter default form values
            if not debt_amount:
                error = 'Please enter a debt amount'
        else:
            # an explanation of extra data in form:
            # name='' is the field of data that we want to capture it would be equivalent to {{ form.field_name.data }}
            # value='' is the default value we want to be captured if the user leaves this blank
            # placeholder='' is the prompt that we want to be shown so the user understands what data to enter but also that the user needs to enter it
            if not debt_interest:
                debt_interest = 5
            if not debt_term:
                debt_term = 5
            if not debt_monthsyears:
                debt_monthsyears = 'years'
            new_debt_id = DATA_PROVIDER.add_debt_data(debt_amount, debt_type, debt_interest, debt_term, debt_monthsyears)
            debt_data = DATA_PROVIDER.get_data_from_id('debt', 'debt_total_id', new_debt_id)
            print(debt_data)
            calculated_total_debt = Finance.debt_calculator(debt_data)
            calculated_total_debt = f"{calculated_total_debt:,.02f}"
            return render_template('debt_calculator.html', total=calculated_total_debt, debt_data=debt_data)
    return render_template('debt_calculator_form.html', form=form, message=error, external_link_investopedia=external_link_investopedia)



@app.route('/debt_comparison_form', methods=['GET', 'POST'])
def debt_comparison():
    comparison_info = []
    error = ''
    form = ComparisonForm()
    if request.method == 'POST':
        debt1_type = form.debt1_type.data
        debt1_amount = form.debt1_amount.data
        min1_repayment = form.debt1_repayment.data
        debt1_interest = form.debt1_interest.data

        debt2_type = form.debt2_type.data
        debt2_amount = form.debt2_amount.data
        min2_repayment = form.debt2_repayment.data
        debt2_interest = form.debt2_interest.data

        debt3_type = form.debt3_type.data
        debt3_amount = form.debt3_amount.data
        min3_repayment = form.debt3_repayment.data
        debt3_interest = form.debt3_interest.data

        if not debt1_amount or not min1_repayment:
            error = 'Please enter a debt amount, minimum repayment and rate of interest'
        else:
            if not debt1_interest:
                debt1_interest=0
            if not debt2_amount or not min2_repayment:
                debt2_amount=0
                debt2_interest=0
                min2_repayment=0
            if not debt3_amount or not min3_repayment:
                debt3_amount=0
                debt3_interest=0
                min3_repayment=0
            DATA_PROVIDER.add_debt_data(debt1_amount, debt1_type, debt1_interest)
            DATA_PROVIDER.add_debt_data(debt2_amount, debt2_type, debt2_interest)
            DATA_PROVIDER.add_debt_data(debt3_amount, debt3_type, debt3_interest)

            debt_1 = [debt1_amount, debt1_interest, min1_repayment]
            debt_2 = [debt2_amount, debt2_interest, min2_repayment]
            debt_3 = [debt3_amount, debt3_interest, min3_repayment]

            comparison_info = [debt_1, debt_2, debt_3]
            print(comparison_info)
            #Finance.debt_comparison_calc(comparison_info) # Add the name of your function here
            #return render_template('comparison_results.html') # Add the name of your html comparison results page here

            # sort all the nested lists using the 2nd element, don't ask me how this works I am not sure I can re-think it!!!!
            debt_stack = comparison_info.sort(key = lambda debt_interest: debt_interest[1] )
            print(debt_stack)
            


    return render_template('debt_comparison_form.html', form=form, message=error)




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





