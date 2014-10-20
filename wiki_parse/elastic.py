from elasticsearch import Elasticsearch
from wiki_api import good_title, fetch_articles_by_titles

# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds

# all_titles(es, "biology", "title")
def all_titles(es, _index, _doc_type):
  le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
  r = es.search(index=_index, doc_type=_doc_type, size=25000, body=le_search)
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

def fetch_articles_and_add_to_elastic_search(es, titles, _index, _doc_type):
  es.index(index=_index, doc_type="dummy", id="dummy", body={"dummy" : "dummy"})
  unpersisted_titles = all_unpersisted_titles(es, _index, _doc_type, titles)
  size_title, size_unpersisted = len(titles), len(unpersisted_titles)
  print "total titles: %s, to go: %s, persisted: %s" % (size_title, size_unpersisted, size_title - size_unpersisted)
  grouped_titles = [unpersisted_titles[i:i+10] for i in range(0, len(unpersisted_titles), 10)]
  for sub_titles in grouped_titles:
    all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
    add_multiple_articles(es, _index, _doc_type, all_articles)
  print "Done Loading %s articles in total. For index=%s and doc_type=%s" % (size_unpersisted, _index, _doc_type)
















