from wtforms import IntegerField, SubmitField, BooleanField, SelectField, StringField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm


class BasicForm(FlaskForm):
    username = StringField('Your name')
    homeowner = BooleanField('Homeowner')
    salary = IntegerField('Gross Salary')
    other = IntegerField('Other')
    food_drink = IntegerField('Food and Drink (groceries)')
    housing = IntegerField('Housing (rent or mortgage payments)')
    energy = IntegerField('Energy Bills')
    petrol = IntegerField('Petrol or Diesel')
    train = IntegerField('Train Fares')
    bus = IntegerField('Bus Fares')
    eating = IntegerField('Eating and Drinking (takeouts, pubs, coffee shops)')
    holidays = IntegerField('Holidays')
    clothes = IntegerField('Clothes and Footwear')
    submit = SubmitField('Submit')

class DebtForm(FlaskForm):
    debt_amount = IntegerField('Debt Amount')
    debt_repayment = IntegerField('Minimum Repayment')
    debt_interest = IntegerField('Debt Interest Rate (APR)')
    debt_term = IntegerField('Debt Term in months')
    debt_type = SelectField('debt_type', choices=[('Personal Loan', 'Personal Loan'), ('Mortgage', 'Mortgage'), ('Overdraft', 'Overdraft'), ('Car Loan', 'Car Loan'), ('Credit Card', 'Credit Card'), ('Store or catalogue', 'Store or Catalogue'), ('BNPL', 'BNPL Buy Now, Pay Later'), ('Other', 'Other, eg. Payday Loan')])
    submit = SubmitField('Submit')

class SavingsForm(FlaskForm):
    savings_lump = IntegerField('Initial Lump Sum')
    monthly_saving_amount = IntegerField('Monthly amount saved')
    savings_interest = IntegerField('Savings Interest Rate (APR)')
    savings_term = IntegerField('Savings Term in Years')
    savings_goal = StringField('My Savings Goal')
    submit = SubmitField('Submit')
    
    
class ComparisonForm(FlaskForm):
    username = StringField('Username')
    debt1_amount = IntegerField('Debt Amount')
    debt1_repayment = IntegerField('Minimum Repayment')
    debt1_interest = IntegerField('Debt Interest Rate (APR)')
    debt1_type = SelectField('debt_type', choices=[('Personal Loan', 'Personal Loan'), ('Mortgage', 'Mortgage'), ('Overdraft', 'Overdraft'), ('Car Loan', 'Car Loan'), ('Credit Card', 'Credit Card'), ('Store or catalogue', 'Store or Catalogue'), ('BNPL', 'BNPL Buy Now, Pay Later'), ('Other', 'Other, eg. Payday Loan')])

    debt2_amount = IntegerField('Debt Amount')
    debt2_repayment = IntegerField('Minimum Repayment')
    debt2_interest = IntegerField('Debt Interest Rate (APR)')
    debt2_type = SelectField('debt_type', choices=[('Personal Loan', 'Personal Loan'), ('Mortgage', 'Mortgage'), ('Overdraft', 'Overdraft'), ('Car Loan', 'Car Loan'), ('Credit Card', 'Credit Card'), ('Store or catalogue', 'Store or Catalogue'), ('BNPL', 'BNPL Buy Now, Pay Later'), ('Other', 'Other, eg. Payday Loan')])


    debt3_amount = IntegerField('Debt Amount')
    debt3_repayment = IntegerField('Minimum Repayment')
    debt3_interest = IntegerField('Debt Interest Rate (APR)')
    debt3_type = SelectField('debt_type', choices=[('Personal Loan', 'Personal Loan'), ('Mortgage', 'Mortgage'), ('Overdraft', 'Overdraft'), ('Car Loan', 'Car Loan'), ('Credit Card', 'Credit Card'), ('Store or catalogue', 'Store or Catalogue'), ('BNPL', 'BNPL Buy Now, Pay Later'), ('Other', 'Other, eg. Payday Loan')])

    submit = SubmitField('Submit')
