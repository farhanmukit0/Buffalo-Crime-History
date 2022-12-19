# PART 2

def list_dic_gen(list_str, list_lists):
  acc_list = []
  for j in list_lists:
    dict = {}
    r = 0    
    for i in list_str: 
      dict[i] = j[r]
      r += 1
    acc_list.append(dict)
  return acc_list


import csv
def read_values(filename):
  import csv
  with open(filename) as f:
    reader = csv.reader(f)
    acc1 = []
    for line in reader:
      acc1.append(line)
  return acc1[1:]


def list_gen(list_dict, list_str):
  acc1 = []
  for i in list_dict:
    acc2 = []
    for l in list_str:
      acc2.append(i[l])
    acc1.append(acc2)
  return acc1

def write_values(lists, filename):
  with open(filename, 'a') as f:
    writer = csv.writer(f)
    for list in lists:
      writer.writerow(list)
#part 3
import json
import urllib

def split_date(date):
  l = date.split('T')
  m = l[0].split('-')
  acc = []
  acc.append(int(m[0]))
  acc.append(int(m[1]))
  return acc

def fix_data(lod,k):
  m = lod
  for i in m:
    j = split_date(i[k])
    i['year'] = j[0]
    i['month'] = j[1]
  return m


import json
import urllib.request
def json_loader(url):
  x = urllib.request.urlopen(url)
  content_string = x.read().decode()
  content = json.loads(content_string)
  return content

def make_values_numeric(k,dict):
  d = dict
  for key in k:
    for i in d:
      val = d[i]
      if d[i] == d[key]:
        d[key] = int(d[key])
  return d

def save_data(lod,keys,filename):
  import csv
  with open(filename, 'w') as file:
    reader = csv.reader(file)
    writer = csv.writer(file)
    writer.writerow(keys)
    for d in lod:
      acc = []
      for i in keys:
        acc.append(d[i])
      writer.writerow(acc)

def load_data(file):
  import csv
  with open(file) as f:
    reader = csv.reader(f)
    rows = list(reader)
    acc = []
    header = rows[0]
    datarows = rows[1:]
    for i in datarows:
      accdic = {}
      n = 0
      for h in header:
        accdic[h] = i[n]
        n += 1
      acc.append(accdic)
  return acc
