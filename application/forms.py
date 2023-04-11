from wtforms import IntegerField, SubmitField, RadioField, SelectField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm


class BasicForm(FlaskForm):
    salary = IntegerField('Salary')
    other = IntegerField('Other')
    food_drink = IntegerField('Food and Drink')
    housing = IntegerField('Housing')
    energy = IntegerField('Energy Bills')
    petrol = IntegerField('Petrol or Diesel')
    train = IntegerField('Train Fares')
    bus = IntegerField('Bus Fares')
    eating = IntegerField('Eating and Drinking')
    holidays = IntegerField('Holidays')
    clothes = IntegerField('Clothes and Footwear')
    submit = SubmitField('Submit')

class DebtForm(FlaskForm):
    debt_amount = IntegerField('Debt Amount')
    debt_interest = IntegerField('Debt Interest Rate (APR)')
    debt_term = IntegerField('Debt Term in')
    monthsyears = RadioField('label', choices=[('months','Months'),('years','Years')])
    debt_type = SelectField('debt_type', choices=[('mortgage', 'Mortgage'), ('overdraft', 'Overdraft'), ('personal_loan', 'Personal Loan'), ('car_loan', 'Car Loan'), ('credit-Card', 'Credit Card'), ('store_catalogue', 'Store/ Catalogue'), ('BNPL', 'BNPL Buy Now, Pay Later'), ('other', 'Other, eg. Payday Loan')])
    submit = SubmitField('Submit')
    
    
