from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DateTimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



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

class main_form(FlaskForm):
    report_type = SelectField(u'Report Type', choices=[('none', 'None'), ('time_series', 'Time Series'), ('histogram', 'Histogram')], default='none')
    output = SelectField('Output Type', choices=[('csv','CSV'), ('plot','Plot')], default='csv')
    product = SelectField('Product', choices=[('TX','TX')], default='TX')
    step_name = StringField('Step Name', validators=[DataRequired()])
    part_number = StringField('Part Number', default='all', validators=[DataRequired()])    #doesn't update right without DataRequired
    line = SelectField('Line', choices=[('all','all'), ('TX1', 'TX1'), ('TX2', 'TX2'), ('TX3', 'TX3'), ('TX4', 'TX4')], default='all')
    process_type = SelectField('Process', choices=[('all','all'), ('ICC', 'ICC'), ('ECU', 'ECU')], default='TX')

    tester_list = ['all',
                   'T1ECU019','T1ECU025',
                   'T2ECU024','T2ECU027','T2ECU034','T2ECU048',
                   'T3ECU052','T3ECU053',
                   'T4ECU038','T4ECU051',
                   'T1ICC022','T1ICC026',
                   'T2ICC018','T2ICC023','T2ICC047',
                   'T3ICC050','T3ICC078',
                   'T4ICC039','T4ICC049']
    tester = SelectMultipleField('Tester Name', choices=[(x,x) for x in tester_list], default='TX')
    daterange = StringField('Date Range', validators=[DataRequired()])
    
    submit3 = SubmitField('Submit')

#class fail_form(main_form): #inherit from main_form
    #report_type = SelectField('Report Type', choices=[('fail_rate', 'Fail Rate'), ('tft', 'Total Fail Time'),
    #                                                   ('ebyi','ECU Failures by ICC Tester')], default='fail_rate')
    #by_fields = SelectMultipleField('By Fields', choices=[('TESTER NAME','Tester'), ('PART NUMBER', 'Part Number'), 
    #                                              ('PROCESS', 'Process'), ('LINE', 'Line')], validators=[DataRequired()], default='line')
    
class bokeh_form(FlaskForm):
    groupby = SelectMultipleField('By Fields', choices=[('TESTER NAME','Tester'), ('PART NUMBER', 'Part Number'), 
                                                          ('PROCESS', 'Process'), ('LINE', 'Line')], 
                                    validators=[DataRequired()], default='line')
    submit2 = SubmitField('Update')