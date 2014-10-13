import urllib2
import json 
import ast

BASE = "/Users/sacry/dev/uni/s5/la/AdaptiveAgents/wiki_parse/"
base_url = "http://en.wikipedia.org/w/api.php?"

def category(cmtitle):
  return {
    "format" : "json",
    "action" : "query",
    "list" : "categorymembers",
    "cmtitle" : urllib2.quote(cmtitle, ''),
    "cmlimit" : 100
  }

def article(title="Biological dark matter"):
  return {
    "format" : "json",
    "action" : "query",
    "titles" : urllib2.quote(title, ''),
    "prop" : "revisions",
    "rvprop" : "content"
  }

def load_json(fname):
  data = ""
  with open (BASE + fname + ".json", "r") as myfile:
    data = myfile.read()
  return ast.literal_eval(data)

def save_json(h, fname):
  json_data = json.dumps(h, indent=2, sort_keys=True).encode('utf8')
  with open(BASE + fname + ".json", 'w+') as json_file:
    json_file.write(json_data)

def hash_to_data(h):
  return "&".join(["%s=%s" % (k, v) for (k, v) in h.iteritems()])

def get_all(cat, limit=0):
  cat = hash_to_data(category(cat))
  query = "%s%s" % (base_url, cat)
  print query

  def get_all_by(query, titles, code=""):
    tmp = query + ("&" + code if code else "")
    str_resp = urllib2.urlopen(tmp).read()
    dict_resp = ast.literal_eval(str_resp)
    titles += [node["title"] for node in dict_resp["query"]["categorymembers"]]
    
    if dict_resp.has_key("query-continue"):
      code = dict_resp["query-continue"]["categorymembers"]["cmcontinue"]
      return get_all_by(query, titles, "cmcontinue=%s" % code)
    else:
      return titles

  titles = get_all_by(query, [], "")

  result = []
  for sub_category in titles:
    if sub_category.find("Category:") != -1 and limit < 1:
      print "%s. %s" % (limit, sub_category)
      result.append({"name": sub_category.split(":")[-1], "titles" : get_all(sub_category, limit + 1)})
    else:
      result.append(sub_category)

  return result

def flatten_to_titles(hs):
  ls = []
  print hs
  for elem in hs["titles"]:
    if type(elem) == type("string"):
      ls.append(elem)
    else:
      ls += flatten_to_titles(elem)
  return ls

def get_all_articles(fname):
  all_titles = flatten_to_titles(load_json(fname))
  for title in all_titles:
    query = "%s%s" % (base_url, hash_to_data(article(title)))
    print query



# titles = get_all("Category:Biology")
# save_json({"name":"Biology", "titles" : titles}, "bio_titles2")


get_all_articles("bio_titles2")



