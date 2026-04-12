# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage

class MovieForm (FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    description= TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[DataRequired(),FileAllowed(['png','jpg'])])
