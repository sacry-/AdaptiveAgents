import os
import json 
import ast
from utils import persistence_path

def json_category_path(fname):
  return "%s/categories/%s.%s" % (persistence_path(), fname, "json")

def save(apath, content):
  with open(apath, 'w+') as f:
    f.write(content)

def read(apath):
  t = ""
  with open(apath, 'r') as f:
    t = f.read()
  return t

def create_file_name(field, depth):
  return ("%s_titles_%s" % (field, depth)).lower()

# String -> Dictionary 
def load_json(fname):
  return ast.literal_eval(read(json_category_path(fname)))

# Dictionary -> String -> Unit 
def save_json(h, fname):
  json_data = json.dumps(h, indent=2, sort_keys=True).encode('utf8')
  save(json_category_path(fname), json_data)

# JsonHash -> List[String] 
# JsonHash ~>
# { "titles" : [
#    "Biology", 
#    "More Biology",
#    { "name" : "sub_category of Biology", 
#      "titles" : ["Biology2", "", {..}] }
# ]} 
# -> ["Biology", "More Biology", "Biology2", ..]
def flatten_hash(h):
  for t in h["titles"]:
    if type(t) == type({}):
      for j in flatten_hash(t):
        yield j
    else:
      yield t

