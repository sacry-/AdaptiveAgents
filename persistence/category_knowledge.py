from os import listdir, name, getenv
from os.path import isfile, join, realpath
from socket import gethostname


USED_CATEGORIES = ["Biology", "Physics", "Chemistry"]

def saved_titles(depth):
  p = category_path()
  result = []
  for f in listdir(p):
    if f.endswith(".json"):
      name = f.split(".")
      if name[0][-1] == str(depth):
        result.append(name[0])
  return result

def category_path():
  return "%s/categories" % persistence_path()