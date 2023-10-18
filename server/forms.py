from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from server.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=17)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')