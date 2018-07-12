# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:23:49 2018

@author: tnjdonegan
"""
import pymongo
import pandas as pd
from datetime import datetime
import re

CLIENT = pymongo.MongoClient('mongodb://10.73.40.95:27017/')

def build_where(form, d={}):
    """
    form: FlaskForm (forms.py) containing user input
    return mongo where dict arg
    """
    try:
        dr = form.daterange.data
        start_date = datetime.strptime(dr[0:10], '%m/%d/%Y')
        end_date = datetime.strptime(dr[13::], '%m/%d/%Y')
        d['DATE'] = {'$gte':start_date,'$lte':end_date}
            
        if form.line.data != 'all':
            d['LINE'] = form.line.data
            
        pn = form.part_number.data.lower()
        if pn != 'all':
            if 'tn' in pn:
                pn = pn.replace('tn','')
            if 'x' in pn or len(pn.split('-')[1]) < 4:
                pn = pn.replace('x','')
                #treat last digit as any digit: -123x
                d['PART_NUMBER'] = re.compile('(%s)[0-9]' % (pn))
            else:
                d['PART_NUMBER'] = pn
                
        if form.process_type.data != 'all':
            d['PROCESS'] = form.process_type.data
            
        if str(form.tester.data)[2:-2] != 'all':    #['all'] -> all
            d['TESTER_NAME'] = form.tester.data

    except:
        return 'bad input: ***' + str(d) + '***'
        
    try: #specific to fail_stats
        return str(form.by_fields.data)
    except:
        pass
    return d
 
def query(product, col, where, project={'_id':0}):
    """
    return list result from mongo query
    """
    db = CLIENT[product]
    result = list(db[col].aggregate([
                    {'$unwind':'$TEST'},
                    {'$match': where},
                    {'$project': project}
                    ]))
    return result

def csv(unwound_data):
    """
    unwound_data: list of dicts returned from mongo unwind aggregation (assumes len>0)
    return: serve flattened csv to user
    """
    
    fieldnames = list(unwound_data[0].keys())
    if 'TEST' in unwound_data[0].keys():
        for key in unwound_data[0]['TEST']:
            fieldnames.append(key)
    fieldnames.remove('TEST')
    fieldnames = str(fieldnames)[1:-1].replace("'","")

    s = ''
    for row in unwound_data:
        if 'TEST' in row.keys():
            for key in row['TEST']:
                row[key] = row['TEST'][key]
            row.pop('TEST')
            for k in row:
                s += str(row[k]) + ', '
        #s += '\n'
        s = s[:-2] + '\n' #remove trailing comma and and new line
            
    csv_content = fieldnames + '\n' + s
    return csv_content

def fail_rate(unwound_data):
    """
    unwound_data: list of dicts returned from mongo unwind aggregation
    return fail rates by tester
    """
    df = pd.DataFrame(pd.io.json.json_normalize(unwound_data))
    df.index = df['DATETIME']
    df2 = df.groupby([pd.Grouper(freq='d'),'PART NUMBER','PROCESS'])
    df2 = 1 - df2['OK'].sum()/df2['OK'].count()    
    return df2

def ecu_by_icc(col):
    """
    ECU Failures by ICC tester
    """
    #get ECU failures
    where = build_where_dict({'OK':False, 'PROCESS':'ECU'})
    result = query_mongo(where, {'ID':1, '_id':0}, col)
    df = df = pd.DataFrame(pd.io.json.json_normalize(result))

    #get the ICC tester that passed those IDs
    where = build_where_dict({'ID':{'$in':list(df['ID'])}, 'PROCESS':'ICC', 'OK':True})
    result = query_mongo(where, {'TESTER NAME':1, '_id':0}, col)
    df = pd.DataFrame(pd.io.json.json_normalize(result))
    df2 = df.groupby('TESTER NAME').size()
#    if plot:
#        df2.plot.bar(title='Count of ECU failures by ICC tester')
    return df2
    
 