from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BasicForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Add Name')

