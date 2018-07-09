from flask import render_template, url_for, flash, redirect, request, abort, Response, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import Login, Register, QueryParams

app = Flask(__name__)
app.config['SECRET_KEY'] = '880072237bb449637a697256a0e95a41'


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    name_exists = True
    pleb = True #future secure access implementations
    form1 = Login()
    form2 = Register()
    form3 = QueryParams()
    #if request.method == "POST":
    if form1.validate_on_submit() and form1.submit1.data:
        name=form1.name1.data
        if name_exists:#simulates querying the db
            flash("Login Successful:  "+name, 'success')
            return render_template('index.html', name=name, form3=form3)
        else:
            flash("The name, "+name+", is not reflected in the database. Please Do Better. ", 'warning')
            return render_template('index.html', form1=form1, form2=form2)
    if form2.validate_on_submit() and form2.submit2.data:
        #Register user in db
        name=form2.name2.data
        name_not_taken = True
        if name_not_taken:#simulates querying the db to check against existing names
            flash("Registration Successful: "+name, 'success')
            #flash("This username, "+name+", will henceforth persist allowing cached historical queries to be more conveniently rendered.", 'info')
            return render_template('index.html', name=name, first_time=True, form3=form3)
        else:
            flash("Name Taken: Please Do Better", 'warning')
            return render_template('index.html', form1=form1, form2=form2, pleb=pleb)
        
    return render_template('index.html', form1=form1, form2=form2, pleb=pleb)

@app.route("/logged_in", methods=['GET', 'POST'])
def logged_in():
    name='Larry'#find name in session
    return render_template('logged_in.html')


@app.route("/macros")
def macros():
    return render_template('macros.html')

@app.route("/footer")
def footer():
    return render_template('footer.html')

	
if __name__ == '__main__':
    app.run(debug=True)