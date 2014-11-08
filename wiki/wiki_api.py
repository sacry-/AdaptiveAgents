# coding: utf-8
import urllib2
import ast
import re
import time
import sys
from clean_and_parse import clean_parse

# Mhhhh... https://wikipedia.readthedocs.org/en/latest/code.html#api
# https://pypi.python.org/pypi/wikipedia/1.3.1 ... :-(

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
  str_resp = "{}"
  try:
    str_resp = urllib2.urlopen(query).read()
  except:    
    print "retrying to connect to wikipedia.."
    return fire_query(query)
  dict_resp = ast.literal_eval(str_resp)
  if dict_resp.has_key("error"):
    raise "Error Firing query to wikipedia! %s" % query
    sys.exit()
  else:
    return dict_resp

# Dictionary -> String
def query_by_data(data):
  return "%s%s" % (BASE_URL, query_from_hash(data))

# String -> Int -> JsonHash
def categories_by_depth(category_string, limit):
  print "Category: %s Limit: %s" % (category_string, limit)
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
  for sub_category in titles:
    if sub_category.find("Category:") != -1 and limit > 0:
      result.append({
        "name" : sub_category.split(":")[-1], 
        "titles" : categories_by_depth(sub_category, limit - 1)
      })
    else:
      result.append(sub_category)
  return result

# JsonHash -> Dictionary[ String -> { Int, String } ]
def fetch_body_from_article_response(nested_response_hash):
  response_hash = nested_response_hash["query"]["pages"]
  page_id, body = response_hash.items()[0]
  content = ""
  if body.has_key("revisions"):
    content = body["revisions"][0]["*"]
  title = good_title(body["title"])
  print "Fetched Title: %s" % title
  return { 
    "page_id" : page_id, 
    "title" : title, 
    "content" : clean_parse(content)
    }

# List[String] -> List[Json]
def fetch_articles_by_titles(title_list, limit):
  collected_articles = []
  for title in title_list:
    if limit < 1: 
      return collected_articles
    query = query_by_data(article(title))
    response = fire_query(query)
    article_hash = fetch_body_from_article_response(response)
    collected_articles.append(article_hash)
    limit -= 1
  return collected_articles

