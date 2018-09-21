from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import Roomate

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ResetPassword(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Reset Password')

class NewPassword(FlaskForm):
    password = PasswordField('Password',validators=[Required()])
    password_repeat = PasswordField('Repeat Password', validators=[Required(),EqualTo('password')])
    submit = SubmitField('Change Password')