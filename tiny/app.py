from flask import render_template, url_for, flash, redirect, request, abort, Response, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_unbreakable_key_yo'

class Login(FlaskForm):
    name1 = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True})
    submit1 = SubmitField('Login')
    
class Register(FlaskForm):
    name2 = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True})
    submit2 = SubmitField('Register')

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    name_exists = True
    form1 = Login()
    form2 = Register()
    #if request.method == "POST":
    if form1.validate_on_submit() and form1.submit1.data:
        name=form1.name1.data
        if name_exists:#simulates querying the db
            flash("Login Successful:  "+name, 'success')
            return render_template('index.html', form1=form1, form2=form2, name=name)
        else:
            flash("The name, "+name+", is not reflected in the database. Please Do Better. ", 'warning')
            return render_template('index.html', form1=form1, form2=form2)
    if form2.validate_on_submit() and form2.submit2.data:
        #Register user in db
        name=form2.name2.data
        name_not_taken = True
        if name_not_taken:#simulates querying the db to check against existing names
            flash("Registration Successful", 'success')
            flash("This username, "+name+", will henceforth persist allowing cached historical queries to be more conveniently rendered.", 'info')
            return render_template('index.html', form1=form1, form2=form2, name=name, first_time=True)
    
    return render_template('index.html', form1=form1, form2=form2)

@app.route("/logged_in", methods=['GET', 'POST'])
def logged_in():
    name='Larry'#find name in session
    return render_template('logged_in.html')


@app.route("/macros")
def macros():
    return render_template('macros.html')

	
if __name__ == '__main__':
    app.run(debug=True)