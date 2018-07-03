from flask import render_template, url_for, flash, redirect, request, abort, Response, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_unbreakable_key_yo'

class Login(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired()])
    submit1 = SubmitField('Login')
    
class Register(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired()])
    submit2 = SubmitField('Register')

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    form1 = Login()
    form2 = Register()
    #if request.method == "POST":
    if form1.validate_on_submit() and form1.submit1.data:
        name=form1.name.data
        flash("Welcome back,  "+name, 'success')
        flash("Would you like to see your most recent queries?", 'info')
        return redirect(url_for('home'))
    if form2.validate_on_submit() and form2.submit2.data:
        name=form2.name.data
        flash("Registration Successful", 'success')
        flash("This username, "+name+", will henceforth persist allowing cached historical queries to be more conveniently rendered.", 'info')
        return redirect(url_for('home'))
    
    return render_template('index.html', form1=form1, form2=form2)

@app.route("/macros")
def macros():
    return render_template('macros.html')

	
if __name__ == '__main__':
    app.run(debug=True)