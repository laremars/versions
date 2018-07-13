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
    if form1.validate_on_submit() and form1.submit1.data:#Login
        name=form1.name1.data
        title = "User - "+name
        description = "Please choose an option to proceed:"
        if name_exists:#simulates querying the db
            flash("Login Successful:  "+name, 'success')
            return render_template('index.html', name=name, form3=form3, title=title, description=description)
        else:
            flash("The name, "+name+", is not reflected in the database. Please Do Better. ", 'warning')
            return render_template('index.html', form1=form1, form2=form2)
        
    if form2.validate_on_submit() and form2.submit2.data:#Register
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
        '''
    if form1.validate_on_submit():
    flash('Form 1 has validated','successs')
    where = mongofuns.build_where(form1)
    unwound_data = mongofuns.query(form1.product.data, form1.step_name.data, where)
    if not unwound_data:
        return Response('returned no records: CLIENT.' + str(form1.product.data) + '.' + str(form1.step_name.data) + \
        '.find(' + str(mongofuns.build_where(form1)) + ')')
    if form1.output.data == 'csv':
        csv_content = mongofuns.csv(unwound_data)
        return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})
        '''
    if form3.validate_on_submit() and form3.submit3.data:#Query Fields
        where = mongofuns.build_where(form3)
        #flash("where: "+str(where), 'warning')
        
        unwound_data = mongofuns.query(form3.product.data, form3.step_name.data, where)
        flash("unwound: "+str(unwound_data), 'warning')
        if not unwound_data:
            return Response('returned no records: CLIENT.' + str(form3.product.data) + '.' + str(form3.step_name.data) + 
            '.find(' + str(mongofuns.build_where(form3)) + ')')
        if form3.output.data == 'csv':
            csv_content = mongofuns.csv(unwound_data)
            return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})

        #http://biobits.org/bokeh-flask.html
        if form3.output.data == 'plot':
            if form3.report_type.data == 'histogram':
                script,div = bokehfuns.hist_comp(unwound_data)
            elif form3.report_type.data == 'time_series':
                script,div = bokehfuns.time_comp(unwound_data)
            return render_template('index.html', title='Measurement Stats', form1=form1, form2=form2, form3=form3, script=script, div=div)
        
        '''
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
        '''
        return redirect(url_for(('home')))#must use redirect and url_for to run the function instead of merely rendering the provided html document
    flash(form3.errors, 'info')
    return render_template('index.html', form1=form1, form2=form2, pleb=pleb, description=description, title=title)

@app.route("/gen_query", methods=['GET', 'POST'])
def logged_in():
    gc.collect()
    
    
    myquery = { 
             "FAIL_COUNT": { "$gt": 1500 , "$lt": 1659 },
             "LINE": "TX2" 
    }

    doc = list(CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST": 1 }))
    flash(str(doc) +' The returned list omits assigned id and TEST  items, where the results are limited to two.','info')
    
    
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