from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignupForm(FlaskForm):
    First_Name = StringField('First Name',validators=[DataRequired()])
    Last_Name = StringField('Last Name',validators=[DataRequired()])
    Email = StringField('Email',validators=[DataRequired(), Email()])
    Password = PasswordField('Password',validators=[DataRequired()])
    Mobile_number= StringField('Mobile Number',validators=[DataRequired()])
	