import bottle
import json
import data
import process
import os.path

@bottle.route('/')
def index():
  html = bottle.static_file("index.html", root='.')
  return html

@bottle.route('/script.js')
def jsfile():
  js = bottle.static_file("script.js", root='.')
  return js

@bottle.route('/barchart')
def barchart():
  values = data.read_values('saved_data.csv')
  newdict = {}
  for i in values:
    newdict[i[0]] = 0
  for j in values:
    newdict[j[0]] +=1
  cleaned = process.remove_min(newdict, 20)
  return json.dumps(cleaned)

@bottle.route('/piechart')
def piechart():
  values = data.read_values('saved_data.csv')
  dict = {}
  for i in values:
    dict[i[4]] = 0
  for j in values:
    dict[j[4]] += 1
  return json.dumps(dict)

@bottle.post('/linechart')
def linechart():
  values = data.read_values('saved_data.csv')
  return json.dumps(values)
    
def startup( ):
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads = ['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)
            
startup()
bottle.run(host='0.0.0.0',port=8080)