from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class Login(FlaskForm):
    name1 = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True})
    submit1 = SubmitField('Login')
    
class Register(FlaskForm):
    name2 = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True})
    submit2 = SubmitField('Register')

class QueryParams(FlaskForm):
    A = StringField('A')
    Really = StringField('Really')
    Big = StringField('Big')
    List = StringField('List')
    Of = StringField('Of')
    Potential = StringField('Potential')
    Query = StringField('Query')
    Parameters = StringField('Parameters')
    daterange = StringField('Date Range', validators=[DataRequired()])
    submit3 = SubmitField('Register')
