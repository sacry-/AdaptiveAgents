import urllib2
import ast


BASE_URL = "http://en.wikipedia.org/w/api.php?"

# Dictionary -> String
def query_from_hash(h):
  return "&".join(["%s=%s" % (k, v) for (k, v) in h.iteritems()])

# String -> Dictionary
def category(cmtitle):
  return {
    "format" : "json",
    "action" : "query",
    "list" : "categorymembers",
    "cmtitle" : urllib2.quote(cmtitle, ''),
    "cmlimit" : 100
  }

# String -> Dictionary
def article(title="Biological dark matter"):
  return {
    "format" : "json",
    "action" : "query",
    "titles" : urllib2.quote(title, ''),
    "prop" : "revisions",
    "rvprop" : "content"
  }

# String -> Dictionary
def fire_query(query):
  str_resp = urllib2.urlopen(query).read()
  dict_resp = ast.literal_eval(str_resp)
  if dict_resp.has_key("error"):
    raise "Error Firing query to wikipedia! %s" % query
  else:
    return dict_resp

# Dictionary -> String
def query_by_data(data):
  return "%s%s" % (BASE_URL, query_from_hash(data))

# String -> Int -> JsonHash
def categories_by_depth(category_string, limit):
  query = query_by_data(category(category_string))
  titles = fetch_continued_titles(query, [], "")
  return categories_of_next_depth(titles, limit)

# String -> List[String] -> String -> List[String]
def fetch_continued_titles(query, titles, code):
  query_with_possible_code = "%s%s" % (query, ("&" + code if code else ""))
  dict_resp = fire_query(query_with_possible_code)
  titles += [node["title"] for node in dict_resp["query"]["categorymembers"]]
    
  if dict_resp.has_key("query-continue"):
    code = dict_resp["query-continue"]["categorymembers"]["cmcontinue"]
    return fetch_continued_titles(query, titles, "cmcontinue=%s" % code)
  else:
    return titles

# JsonHash -> Int -> JsonHash
def categories_of_next_depth(titles, limit):
  result = []
  print limit
  for sub_category in titles:
    if sub_category.find("Category:") != -1 and limit > 0:
      result.append({
        "name" : sub_category.split(":")[-1], 
        "titles" : categories_by_depth(sub_category, limit - 1)
      })
    else:
      result.append(sub_category)
  return result

# List[String] -> Unit
def fetch_articles_by_titles(title_list):
  for title in title_list:
    query = query_by_data(article(title))
    response = fire_query(query)
    print response

