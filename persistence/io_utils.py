import os
import json 
import ast
from category_knowledge import category_path


def save(text, content):
  with open(text, 'w+') as f:
    f.write(content)

def read(text):
  t = ""
  with open(text, 'r') as f:
    t = f.read()
  return t

def create_file_name(field, depth):
  return ("%s_titles_%s" % (field, depth)).lower()

def json_path(fname):
  if os.name == 'nt':
    return "%s\\%s.%s" % (category_path(), fname, "json")
  return "%s/%s.%s" % (category_path(), fname, "json")

# String -> Dictionary 
def load_json(fname):
  return ast.literal_eval(read(json_path(fname)))

# Dictionary -> String -> Unit 
def save_json(h, fname):
  json_data = json.dumps(h, indent=2, sort_keys=True).encode('utf8')
  save(json_path(fname), json_data)

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

