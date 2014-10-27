from os import listdir, name
from os.path import isfile, join, realpath


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
  if name == 'nt':
    return "C:\\Users\\Swaneet\\github\\AdaptiveAgents\\wiki_parse\\categories\\"  # TODO: fixen how in windows.
  return "%s/categories/" % realpath('') 

