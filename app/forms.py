from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, 
from wtforms.validators import DataRequired, 

class PokeSearchForm(FlaskForm):
    name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField()

#class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #submit = SubmitField()