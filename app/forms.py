from app import db
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired,Email

class ProfileForm(FlaskForm):
    firstName = StringField("First Name",validators=[DataRequired()])
    lastName = StringField("Last Name",validators=[DataRequired()])
    gender = SelectField("Gender",choices=[('male','Male'),('female','Female')])
    email = StringField("Email",validators=[DataRequired(),Email()])
    location = StringField("location",validators=[DataRequired()])
    biography = TextAreaField("Biography",validators=[DataRequired()])
    Pic = FileField("Profile Picture",validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])