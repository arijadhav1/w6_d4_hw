from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('email', validators= [DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit_button = SubmitField()

class CarForm(FlaskForm):
    make = StringField('make')
    model = StringField('model')
    year = DecimalField('year', places=2)
    color = StringField('color')
    description = StringField('description')
    price = DecimalField('price', places=2)
    miles_per_gallon = StringField('miles_per_gallon')
    max_speed = StringField('max_speed')
    seats = StringField('seats')
    submit_button = SubmitField()