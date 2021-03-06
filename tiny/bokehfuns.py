from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import formatters, ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.layouts import gridplot, widgetbox
import numpy as np
import pandas as pd
import datetime as datetime
  
def test_histogram():
    #create data
    measured = np.random.normal(0, 0.5, 1000)
    hist, edges = np.histogram(measured, density=True, bins=50)
    # Create the plot
    p = figure(title='test - generated distribution')
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
        fill_color="#036564", line_color="#033649")

    # Embed plot into HTML via Flask Render
    script, div = components(p)
    #return render_template("bok.html", script=script, div=div)
    return script, div

def hist_comp(unwound_data):
    df = pd.DataFrame(pd.io.json.json_normalize(unwound_data))
    hist, edges = np.histogram(df['TEST.VALUE'], density=True, bins=20)
    p = figure(plot_width=700, plot_height=700)#regular entry
    #p = figure(sizing_mode='scale_width', plot_height=700)#So big!
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])  
    script, div = components(p)  
    return script, div
    
def time_comp(unwound_data):
    df = pd.DataFrame(pd.io.json.json_normalize(unwound_data))
    p = figure()
    x = df['TEST.DATETIME']
    p.circle(x, df['TEST.VALUE'])
    p.xaxis.formatter = formatters.DatetimeTickFormatter(days=["%Y-%m-%d"])
    #add limits
    if 'LOWER LIMIT' in df.columns:
        p.line(x, df['LOWER LIMIT'], line_color='red')
    if 'NOMINAL' in df.columns:    
        p.line(x, df['NOMINAL'], line_color='green')
    if 'UPPER LIMIT' in df.columns:
        p.line(x, df['UPPER LIMIT'], line_color='red')    
    script, div = components(p)  
    return script, div

def box_whisker(data):
    """
    data: mongo list result with fields DATE,LL,NOM,UL,Q1,Q3,MEAN,MAX,MIN
    """
    #https://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html
  #%%  
    df = pd.DataFrame(pd.io.json.json_normalize(data))
    df2 = pd.DataFrame(df['STATS.QUARTILES'].tolist(), columns=['Q1','Q2','Q3'])
    df.pop('STATS.QUARTILES')
    df = pd.concat([df, df2], axis=1)

    figs = []
    for name,group in df.groupby('TESTER_NAME'):
        #somehow combine data for dates
        top = float(pd.to_numeric(group.UPPER_LIMIT).mode() + group['STATS.STDEV'].min())
        bot = float(pd.to_numeric(group.LOWER_LIMIT).mode() - group['STATS.STDEV'].min())
        p = figure(title=name, y_range=(bot,top))
        x = group['DATE']
    
        #stems
        p.segment(x, group['STATS.MAX'], x, group['Q3'])
        p.segment(x, group['STATS.MIN'], x, group['Q1'])
        
        #boxes
        w = datetime.timedelta(days=0.75)    #lucky guess
        p.vbar(x, w, group['Q1'], group['Q2'], fill_color="#E08E79", line_color="black")
        p.vbar(x, w, group['Q2'], group['Q3'], fill_color="#3B8686", line_color="black")
        
        # whiskers (squares are easier)
        p.square(x, group['STATS.MIN'])
        p.square(x, group['STATS.MAX'])
        
        #limits
        p.line(x, group['UPPER_LIMIT'], line_color="red")
        p.line(x, group['NOMINAL'], line_color="green")
        p.line(x, group['LOWER_LIMIT'], line_color="red")
        p.xaxis.formatter = formatters.DatetimeTickFormatter(days=["%Y-%m-%d"])
        figs.append(p)
        #%%
    '''    
    #show table
    td = {'TESTER_NAME' : list(df.TESTER_NAME),
            'DATE' : list(df.DATE.astype(str)),
          'LOG_FILE' : list(df.LOG_FILE)}
    source = ColumnDataSource(td)
    cols = [TableColumn(field='TESTER_NAME', title='Tester'),
            TableColumn(field='DATE', title='Date'),
            TableColumn(field='LOG_FILE', title='Log File Link')]
    w = sum([fig.plot_width for fig in figs]) #spans all plots
    table = DataTable(source=source, columns=cols, width=w)
    grid = gridplot([figs, [widgetbox(table)]])
    '''
    grid = gridplot([figs])
    script, div = components(grid)
    return script, div