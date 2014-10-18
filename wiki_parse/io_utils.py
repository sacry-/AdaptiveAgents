import sys
import os
import json 
import ast

# String
def relative_path():
  return "%s/" % os.path.realpath('') 

# String -> Dictionary 
def load_json(fname):
  data = ""
  with open (relative_path() + fname + ".json", "r") as myfile:
    data = myfile.read()
  return ast.literal_eval(data)

# Dictionary -> String -> Unit 
def save_json(h, fname):
  json_data = json.dumps(h, indent=2, sort_keys=True).encode('utf8')
  with open(relative_path() + fname + ".json", 'w+') as json_file:
    json_file.write(json_data)

# JsonHash -> List[String] 
def flatten_hash(h):
  for t in h["titles"]:
    if type(t) == type({}):
      for j in flatten_hash(t):
        yield j
    else:
      yield t