#part 1
def gen_dictionary(data, key):
  acc = {}
  for i in data:
    v = 0
    if key in i:
      v = i[key]
      acc[v] = 0
  return acc

def total_matches(lod,k,v):
  acc = 0
  for i in lod:
    if k in i:
      if i[k] == v:
        acc += 1
  return acc

def total_matches_specific(lod,k,v,k2,v2):
  acc  = 0
  for i in lod:
    if i[k] == v:
      if i[k2] == v2:
        acc += 1
  return acc

def remove_min(data, integer):
  acc = {}
  for i in data:
    if data[i] > integer:
      acc[i] = data[i]
  return acc

