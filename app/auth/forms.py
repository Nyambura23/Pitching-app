from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from models import User

# class RegisterUserForm(FlaskForm):
# 	username = StringField('Username', validators=[DataRequired()], description="Username")
# 	email = StringField('Email', validators=[DataRequired(), Email()])
# 	password = PasswordField('Password', validators=[DataRequired()])
# 	confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
# 	submit = SubmitField('Create Account')

# class LoginUserForm(FlaskForm):
# 	username = StringField('Username', validators=[DataRequired()])
# 	password = PasswordField('Password', validators=[DataRequired()])
# 	login = SubmitField('Sign In')

    # def validate_email(self,data_field):
    #         if User.query.filter_by(email =data_field.data).first():
    #             raise ValidationError('There is an account with that email')

    # def validate_username(self,data_field):
    #     if User.query.filter_by(username = data_field.data).first():
    #         raise ValidationError('That username is taken')