from wtforms import IntegerField, SubmitField
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
    debt_term = IntegerField('Debt Term in Whole Years')
    submit = SubmitField('Submit')
    
    
