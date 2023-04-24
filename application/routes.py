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
    
    
 
@app.route('/articles')
def articles():
    return render_template('articles.html', title='Articles')

@app.route('/savingarticle')
def savingarticle():
    return render_template('savingarticle.html', title='3 Top Ways Save in 2023')

@app.route('/discount_article')
def discount_article():
    return render_template('discount_article.html', title='Top Places to Find Money-Saving Discounts')

@app.route('/debt_mentalhealtharticle')
def debt_mentalhealtharticle():
    return render_template('debt_mentalhealtharticle.html', title='Debt and Mental Health')


@app.route('/dashboard_form', methods=['GET', 'POST'])
def form_input():
    error = ""
    form = BasicForm()
    if request.method == 'POST':
        username = form.username.data
        homeowner = form.homeowner.data
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
        if not username or not salary or not housing:
            error = 'Please fill in the required Username, Salary and Housing fields.'
        
        else:
            user_id = DATA_PROVIDER.add_username(username)
            DATA_PROVIDER.add_income_data(user_id, 'salary', salary)
            DATA_PROVIDER.add_income_data(user_id, 'other', other)
            DATA_PROVIDER.add_form_data(user_id, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes)
            
            user_data = DATA_PROVIDER.get_form_data(user_id)   
            if salary > 75_000:
                average_data = 11
                salary_data = '75K+ pa'
            elif salary > 55_000:
                average_data = 9
                salary_data = 'between 55K and 75K pa'
            elif salary > 45_000:
                average_data = 7
                salary_data = 'between 45K and 55K pa'
            elif salary > 35_000:
                average_data = 5
                salary_data = 'between 35K and 45K pa'
            else:
                average_data = 3
                salary_data = 'less than 25K pa'

            if homeowner:
                salary_comparison = 1
            else:
                salary_comparison = 2
                average_data +=1
            
            uk_average_homeowner_data = DATA_PROVIDER.get_form_data(average_data)
            salary_comparison_data = DATA_PROVIDER.get_form_data(salary_comparison)

            Finance.create_pie(user_data)
            Finance.create_stacked_bar(user_data, salary_comparison_data, uk_average_homeowner_data)

            uk_average_household_data = Finance.create_table(salary_comparison_data)
            weekly = Finance.dashboard_weekly_calculator(user_data)
            monthly = Finance.dashboard_monthly_calculator(user_data)
            annual = Finance.dashboard_annual_calculator(user_data)
           
            return render_template('dashboard.html', title='Dashboard', average=uk_average_household_data, weekly = weekly, monthly=monthly, annual=annual, salary_data=salary_data)

    return render_template('dashboard_form.html', title='Form Page', form=form, message=error)



@app.route('/site_statistics')
def site_statistics():
    average_debt_data = DATA_PROVIDER.average_debt_report() # returns a decimal object
    average_debt = int(average_debt_data) # recast decimal object as an integer
    average = f"{average_debt:,.02f}" # make the integer a formatted string with thousand separator and 2 decimal places for pence
    debt_type_frequency = DATA_PROVIDER.frequency_debt_report()   
    Finance.generate_debt_report(average_debt_data, debt_type_frequency)

    average_savings_data = DATA_PROVIDER.average_savings_report()
    average_savings = int(average_savings_data)
    avg = f"{average_savings:,.02f}"
    savings_type_frequency = DATA_PROVIDER.frequency_savings_report()   
    Finance.generate_savings_report(average_savings_data, savings_type_frequency)

    return render_template('site_statistics.html', title='Site Statistics and Reports', average_debt_data = average, debt_type = debt_type_frequency, average_savings_data=avg, savings_type=savings_type_frequency )



@app.route('/savings_calculator_form', methods=['GET', 'POST'])
def calculate_savings():
    external_link_money_saving_expert = 'https://www.moneysavingexpert.com/'
    error3 = ''
    form = SavingsForm()
    if request.method == 'POST':
        savings_lump = form.savings_lump.data
        monthly_saving_amount = form.monthly_saving_amount.data
        savings_interest = form.savings_interest.data
        savings_term = form.savings_term.data
        savings_goal = form.savings_goal.data
        if not savings_interest:
            savings_interest = 5
        if not savings_term:
            savings_term = 10
        if not monthly_saving_amount:
            monthly_saving_amount = 50
        if not savings_goal:
            savings_goal = 'rainy day'
        new_savings_id = DATA_PROVIDER.add_savings_data(savings_lump, savings_goal, monthly_saving_amount, savings_interest, savings_term)
        saving_instance = DATA_PROVIDER.get_saving_data_from_id('savings', 'savings_total_id', new_savings_id)
        
        calculated_total_savings = Finance.savings_calculator(saving_instance)
        calculated_total_savings = f"{calculated_total_savings:,.02f}"
        return render_template('savings_calculator.html', total=calculated_total_savings, savings_data=saving_instance)

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
        if not debt_amount:
            error = 'Please enter a debt amount'
        else:
            new_debt_id = DATA_PROVIDER.add_debt_data(debt_amount, debt_type, debt_interest, debt_term=debt_term)
            debt_instance = DATA_PROVIDER.get_debt_data_from_id('debt', 'debt_total_id', new_debt_id)
            
            calculated_total_debt = Finance.debt_calculator(debt_instance)
            calculated_total_debt = f"{calculated_total_debt:,.02f}"
            return render_template('debt_calculator.html', total=calculated_total_debt, debt_data=debt_instance)
    return render_template('debt_calculator_form.html', form=form, message=error, external_link_investopedia=external_link_investopedia)



@app.route('/debt_comparison_form', methods=['GET', 'POST'])
def debt_comparison():
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

        if not debt1_amount or not min1_repayment or not debt1_interest:
            error = 'Please enter a debt amount, minimum repayment and rate of interest'
        else:
            # at the moment this only works if you enter all 3 debts, it needs a conditional and some more code to make it work if just 2 debts are entered
            # this was such a cool feature, I wish it wasn't a feature add-on and was more of our MVP centre piece it would have been awesome to have properly coded this as a team
            debt1_id = DATA_PROVIDER.add_debt_data(debt1_amount, debt1_type, debt1_interest, repayment=min1_repayment)
            debt2_id = DATA_PROVIDER.add_debt_data(debt2_amount, debt2_type, debt2_interest, repayment=min2_repayment)
            debt3_id = DATA_PROVIDER.add_debt_data(debt3_amount, debt3_type, debt3_interest, repayment=min3_repayment)
            
            debt_object1 = DATA_PROVIDER.get_debt_data_from_id('debt', 'debt_total_id', debt1_id)
            debt_object2 = DATA_PROVIDER.get_debt_data_from_id('debt', 'debt_total_id', debt2_id)
            debt_object3 = DATA_PROVIDER.get_debt_data_from_id('debt', 'debt_total_id', debt3_id)
            
            # send the debt objects into the comparison calc to find out how long each debt takes to pay off using each debt repayment approach (stack, snowball, avalanche)
            Finance.debt_comparison_calc(debt_object1, debt_object2, debt_object3)

            #sort the objects ready for display on the page
            nested_list = [debt_object1, debt_object2, debt_object3]
            order_list = [1, 2, 3]
            stack_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_debt_interest(), reverse=True) # sort the debt objects, largest interest rate first
            stack_dict = {order:debt_object for order, debt_object in zip(order_list, stack_approach)}

            snowball_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_debt_total_figure())  # sorted by loan size ascending
            snowball_dict = {order:debt_object for order, debt_object in zip(order_list, snowball_approach)}

            avalanche_approach = sorted(nested_list, key=lambda debt_object: debt_object.get_debt_total_figure(), reverse=True)  # sorted by loan size descending
            avalanche_dict = {order:debt_object for order, debt_object in zip(order_list, avalanche_approach)}
            # uses a dictionary to hold the order to avoid an object refernce problem
            # In Python 3.6, the built-in dict class now keeps its items ordered as well

            return render_template('debt_calculator.html', stack_dict=stack_dict, snowball_dict=snowball_dict, avalanche_dict=avalanche_dict)

    return render_template('debt_comparison_form.html', form=form, message=error)




# Repeated Routes to Different Benefits
@app.route('/<benefit_name>')
def benefits(benefit_name):
    # Grab 3 pieces of information from a returned tuple; url-endpoint, how-data and what-data to auto-complete fields
    info_benefits = DATA_PROVIDER.get_benefits_data(benefit_name)
    if benefit_name == 'child-benefit':
        return render_template('benefits_template.html', title='Child Benefit', data=info_benefits[0])
    elif benefit_name == 'housing-benefit':
        return render_template('benefits_template.html', title='Housing Benefit', data=info_benefits[0])
    elif benefit_name == 'employment-support-allowance':
        return render_template('benefits_template.html', title='ESA', data=info_benefits[0])
    elif benefit_name == 'jobseekers-allowance':
        return render_template('benefits_template.html', title='JSA', data=info_benefits[0])
    elif benefit_name == 'universal-credit':
        return render_template('benefits_template.html', title='Universal Credit', data=info_benefits[0])
    else:
        return render_template('index.html', title='Home Page')


