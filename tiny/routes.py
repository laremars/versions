from flask import render_template, url_for, flash, redirect, request, abort, Response
from tiny.forms import Login, Register, QueryParams, bokeh_form, main_form
from tiny import app
from tiny import mongofuns
from tiny import bokehfuns
import gc
import pymongo
import pandas as pd
CLIENT = pymongo.MongoClient('mongodb://10.73.40.95:27017/')



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    title = "TD Data Interface"
    description = "Login or register to continue:"
    name_exists = True
    pleb = True #future secure access implementations
    form1 = Login()
    form2 = Register()
    form3 = main_form()
    #if request.method == "POST":
    if form1.validate_on_submit() and form1.submit1.data:
        name=form1.name1.data
        title = "User - "+name
        description = "Please choose an option to proceed:"
        if name_exists:#simulates querying the db
            flash("Login Successful:  "+name, 'success')
            return render_template('index.html', name=name, form3=form3, title=title, description=description)
        else:
            flash("The name, "+name+", is not reflected in the database. Please Do Better. ", 'warning')
            return render_template('index.html', form1=form1, form2=form2)
    if form2.validate_on_submit() and form2.submit2.data:
        #Register user in db
        name=form2.name2.data
        description = "Please choose an option to proceed:"
        title = "New User - "+name
        name_not_taken = True
        if name_not_taken:#simulates querying the db to check against existing names
            flash("Registration Successful: "+name, 'success')
            #flash("This username, "+name+", will henceforth persist allowing cached historical queries to be more conveniently rendered.", 'info')
            return render_template('index.html', name=name, first_time=True, form3=form3, description=description, title=title)
        else:
            flash("Name Taken: Please Be Original", 'warning')
            return render_template('index.html', form1=form1, form2=form2, pleb=pleb)
        
    if form3.validate_on_submit() and form3.submit3.data:
        testers = form3.tester.data
        #",".join([str(x) for x in testers])
        tstring = ",".join(map(str,testers))
        flash("POST", 'success')
        flash("daterange: "+form3.daterange.data, 'info')
        flash("report_type: "+form3.report_type.data, 'info')
        flash("output: "+form3.output.data, 'info')
        flash("product: "+form3.product.data, 'info')
        flash("step_name: "+form3.step_name.data, 'info')
        flash("part_number: "+form3.part_number.data, 'info')
        flash("line: "+form3.line.data, 'info')
        flash("process_type: "+form3.process_type.data, 'info')
        flash("tester: "+tstring, 'info')
        return render_template('logged_in.html')
    return render_template('index.html', form1=form1, form2=form2, pleb=pleb, description=description, title=title)

@app.route("/gen_query", methods=['GET', 'POST'])
def logged_in():
    return render_template('logged_in.html')


@app.route("/macros")
def macros():
    return render_template('macros.html')

@app.route("/footer")
def footer():
    return render_template('footer.html')

	
if __name__ == '__main__':
    app.run(debug=True)
    
'''

To install all dependencies, run the below command in a virtual env
pip install -r requirements.txt

'''