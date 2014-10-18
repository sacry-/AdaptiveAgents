from elasticsearch import Elasticsearch
from wiki_api import good_title

# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds

# all_titles(es, "biology", "title")
def all_titles(es, _index, _doc_type):
  le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
  r = es.search(index=_index, doc_type=_doc_type, size=10000, body=le_search)
  return map(lambda x: x["_id"], r['hits']["hits"])

def get_single_article(es, _index, _doc_type, _id):
  return es.get(index=_index, doc_type=_doc_type, id=_id)["_source"]

# add_multiple_articles(es, "biology", "title", all_articles)
def add_multiple_articles(es, _index, _doc_type, all_articles):
  for article in all_articles:
    title = article["title"]
    print "Added %s" % title
    es.index(index=_index, doc_type=_doc_type, id=title, body=article)

def flush_all(es):
  es.delete(index="_all")

def all_unpersisted_titles(es, _index, _doc_type, titles):
  persisted_titles = all_titles(es, _index, _doc_type)
  result = []
  for title in titles:
    normalized_title = good_title(title)
    if not normalized_title in persisted_titles:
      result.append(title)
  return result



