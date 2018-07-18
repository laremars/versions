from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import formatters
import numpy as np
import pandas as pd
  
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
    #p = figure(plot_width=700, plot_height=700)#regular entry
    p = figure(sizing_mode='scale_width', plot_height=700)
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