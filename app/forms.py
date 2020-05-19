from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.widgets import TextArea
from flask_wtf.file import FileField,FileRequired,FileAllowed

class CreatGroup(FlaskForm):
    Groupname=StringField('GroupName', validators=[InputRequired()]) 
    Description= StringField('Group Description',validators=[DataRequired()],widget=TextArea())

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignupForm(FlaskForm):
    First_Name = StringField('First Name',validators=[DataRequired()])
    Last_Name = StringField('Last Name',validators=[DataRequired()])
    Username = StringField('Username',validators=[DataRequired()])
    Gender = SelectField(label='Gender',validators=[DataRequired()],choices=[('Male','Male'),('Female','Female')])
    DOB = DateField('Date of Birth', validators=[DataRequired()],format='%Y-%m-%d')
    Email = StringField('Email',validators=[DataRequired(), Email()])
    Password = PasswordField('Password',validators=[DataRequired()])
    Mobile_number= StringField('Mobile Number',validators=[DataRequired()])
    RelationShipStatus = SelectField(label='Relation Ship Status',validators=[DataRequired()],choices=[('Single','Single'),('Married','Married')])
    Bio = StringField('Describe Your Self ',validators=[DataRequired()],widget=TextArea())

class EditprofileForm(FlaskForm):
    First_Name = StringField('First Name',validators=[DataRequired()])
    Last_Name = StringField('Last Name',validators=[DataRequired()])
    Gender = SelectField(label='Gender',validators=[DataRequired()],choices=[('Male','Male'),('Female','Female')])
    DOB = DateField('Date of Birth', validators=[DataRequired()],format='%Y-%m-%d')
    Email = StringField('Email',validators=[DataRequired(), Email()])
    Mobile_number= StringField('Mobile Number',validators=[DataRequired()])
    RelationShipStatus = SelectField(label='Relation Ship Status',validators=[DataRequired()],choices=[('Single','Single'),('Married','Married')])
    Bio = StringField('Bio ',validators=[DataRequired()],widget=TextArea())
    Street=StringField('Address (Street)',validators=[DataRequired()])
    City=StringField('Address (City)',validators=[DataRequired()])

class CommentForm(FlaskForm):
    Comments=StringField('Message',validators=[DataRequired()],widget=TextArea())

class SearchForm(FlaskForm):
    Search=StringField('Search',validators=[DataRequired()])

class PostForm(FlaskForm):
    Post = StringField('Whats on your Mind',validators=[DataRequired()],widget=TextArea())
	
class Photo(FlaskForm):
    photo=FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png'])])