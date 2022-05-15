from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Elevator','Elevator'),('Followup','Followup'),('Social','Social')],validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')
