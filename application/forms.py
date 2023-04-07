from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm


class BasicForm(FlaskForm):
    salary = StringField('Salary')
    other = StringField('Other')
    rent = StringField('Rent/Mortgage')
    electricity = StringField('Electricity')
    gas = StringField('Gas')
    water = StringField('Water')
    council = StringField('Council Tax')
    phone = StringField('Phone Bill')
    subscriptions = StringField('Subscriptions')
    savings = StringField('Savings/CTF')
    submit = SubmitField('Submit')
