import os
from datetime import datetime
import pandas as pd
from io import StringIO
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, Response, Flask
from string import Template
from server import app
from server.forms import *
from server.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from server import mongofuns
from server import bokehfuns
import gc
import pymongo

CLIENT = pymongo.MongoClient('mongodb://10.73.40.95:27017/')

@app.route("/nope")
def home():
    return render_template('home.html', title='Home') #title is passed into macro in layout.html


@app.route("/tricky_nav", methods=['GET', 'POST'])
def tricky_nav():
    form1 = main_form()
    if form1.validate_on_submit():
        where = mongofuns.build_where(form1)
        unwound_data = mongofuns.query(form1.product.data, form1.step_name.data, where)
        if not unwound_data:
            return Response('returned no records: CLIENT.' + str(form1.product.data) + '.' + str(form1.step_name.data) + 
            '.find(' + str(mongofuns.build_where(form1)) + ')')
        if form1.output.data == 'csv':
            csv_content = mongofuns.csv(unwound_data)
            return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})

        #http://biobits.org/bokeh-flask.html
        if form1.output.data == 'plot':
            if form1.report_type.data == 'histogram':
                script,div = bokehfuns.hist_comp(unwound_data)
            elif form1.report_type.data == 'time_series':
                script,div = bokehfuns.time_comp(unwound_data)
            return render_template('meas_stats.html', title='Measurement Stats', form1=form1, script=script, div=div)

    form2 = main_form()
    if form2.validate_on_submit():
        where = mongofuns.build_where(form2)
        unwound_data = mongofuns.query(form2.product.data, form2.step_name.data, where)
        if not unwound_data:
            return Response('returned no records: CLIENT.' + str(form2.product.data) + '.' + str(form2.step_name.data) + 
            '.find(' + str(mongofuns.build_where(form2)) + ')')
        if form2.output.data == 'csv':
            csv_content = mongofuns.csv(unwound_data)
            return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})

        #http://biobits.org/bokeh-flask.html
        if form2.output.data == 'plot':
            if form2.report_type.data == 'histogram':
                script,div = bokehfuns.hist_comp(unwound_data)
            elif form2.report_type.data == 'time_series':
                script,div = bokehfuns.time_comp(unwound_data)
            return render_template('meas_stats.html', title='Measurement Stats', form2=form2, script=script, div=div)
    return render_template('tricky_nav.html', title='Trickyness', form1=form1, form2=form2)

@app.route("/", methods=['GET', 'POST'])
@app.route("/testing", methods=['GET', 'POST'])
def testing():
    import time
    gc.collect()
    form1 = main_form()
    form2 = bokeh_form()
  
    myquery = { 
             "FAIL_COUNT": { "$gt": 1500 , "$lt": 1659 },
             "LINE": "TX2" 
    }

    doc = list(CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST": 1 }))
    flash(str(doc) +' The returned list omits assigned id and TEST  items, where the results are limited to two.','info')

    #if request.method == 'POST':
    if form1.submit1.data:
        flash('Form 1 has validated','successs')
        where = mongofuns.build_where(form1)
        flash(where)
        #unwound_data = mongofuns.query(form1.product.data, form1.step_name.data, where)
        unwound_data =''
        if not unwound_data:
            return Response('returned no records: CLIENT.' + str(form1.product.data) + '.' + str(form1.step_name.data) + \
            '.find(' + str(mongofuns.build_where(form1)) + ')')
        if form1.output.data == 'csv':
            csv_content = mongofuns.csv(unwound_data)
            return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})

        #http://biobits.org/bokeh-flask.html
        elif form1.output.data == 'plot':
            if form1.report_type.data == 'histogram':
                script,div = bokehfuns.hist_comp(unwound_data)
            elif form1.report_type.data == 'time_series':
                script,div = bokehfuns.time_comp(unwound_data)
            return render_template('meas_stats.html', title='Measurement Stats', form1=form1, script=script, div=div, doc=doc)
        elif form2.submit2.data:
            flash('Form 2 submitted.', 'success')
        return render_template('testing.html', title='ThisTest', description='If I\'m here, you just submitted form 2:', form1=form1, form2=form2, doc=doc)
    return render_template('testing.html', title='ThisTest', description='This describes the intended contents of this endpoint:', form1=form1, form2=form2, doc=doc)


@app.route("/landing_page", methods=['GET', 'POST'])
def landing():
    
    gc.collect()
    form1 = main_form()
    form2 = bokeh_form()
    
    myquery = { 
             "FAIL_COUNT": { "$gt": 1500 },
             "LINE": "TX2" 
    }
    
    doc = list(CLIENT.TX.IOFF.find(myquery,{ "_id": 0, "TEST":0 }))
    
    flash(str(doc) +' The returned list omits assigned _id and TEST  items, where the results are limited to two.','info')

    return render_template('landing_page.html', title='Initialization', description='Hopefully, this form will serve as an intialization for following content:', form1=form1, form2=form2, doc=doc)


@app.route("/query_map", methods=['GET', 'POST'])
def query_map():
    
    gc.collect()
    
    form1 = main_form()
    form2 = bokeh_form()
    
    return render_template('query_map.html', title='Query Map', description='Clickable interaction for form progression', form1=form1, form2=form2)


@app.route("/drag_drop", methods=['GET', 'POST'])
def drag_drop():
    
    gc.collect()
    form1 = main_form()
    form2 = bokeh_form()
    
    return render_template('drag_drop.html', title='Query Map', description='Drag and drop interaction for form progression', form1=form1, form2=form2)



@app.route("/off_site", methods=['GET', 'POST'])
def off_site():
    
    gc.collect()
    
    form1 = main_form()
    form2 = bokeh_form()
    
    if form1.submit1.data:
        flash('Form 1 has validated','successs')

        return render_template('off_site.html', title='Off-Site', description='If I\'m here, you just submitted form 2:', form1=form1, form2=form2)
    
    return render_template('off_site.html', title='Off-Site Nav-Style', description='Something a little quicker for structuring queries:', form1=form1, form2=form2)




@app.route('/charts/')
def line_route():
    chart = pygal.Line()
    #define chart here
    chart = chart.render_data_uri()
    return render_template( 'charts.html', chart = chart)


@app.route("/meas_stats", methods=['GET', 'POST'])
def meas_stats():
    form1 = main_form()
    form2 = bokeh_form()
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

        #http://biobits.org/bokeh-flask.html
        if form1.output.data == 'plot':
            if form1.report_type.data == 'histogram':
                script,div = bokehfuns.hist_comp(unwound_data)
            elif form1.report_type.data == 'time_series':
                script,div = bokehfuns.time_comp(unwound_data)
            return render_template('meas_stats.html', title='Measurement Stats', form1=form1, script=script, div=div)
    if form2.validate_on_submit():
        flash('Form 2 has validated','success')
        
    return render_template('meas_stats.html', title='Measurement Stats', form1=form1, form2=form2)

@app.route("/fail_stats", methods=['GET', 'POST'])
def fail_stats():
    form = main_form()
    flash([(x.name,x.data) for x in form])

    if form.validate_on_submit():
        7+i
        where = mongofuns.build_where(form)
        project = {'PART NUMBER':1, 'OK':1, 'PROCESS':1, 'DATETIME':1, '_id':0}
        unwound_data = mongofuns.query(form.product.data, 'OK', where, project)
        df = fail_rate(unwound_data)
        
        if form.output.data == 'csv':
            buf = StringIO()
            csv_content = df.to_csv(buf)
            flash(csv_content)
            return Response(csv_content,  mimetype='text/csv', headers={'Content-disposition':'attachment; filename=test.csv'})


    return render_template('fail_stats.html', title='Fail Stats', form=form)


@app.route("/macros")
def macros():
    return render_template('macros.html')

#This is a proof of concept for dynamic URLs, but I need an API key for full functionality
HTML_TEMPLATE = Template("""
<h1>Hello ${place_name}!</h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")

@app.route('/<some_place>')
def some_place_page(some_place):
    return(HTML_TEMPLATE.substitute(place_name=some_place))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
