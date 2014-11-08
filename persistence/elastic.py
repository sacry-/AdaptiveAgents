# coding: utf-8
from elasticsearch import Elasticsearch
from utils import good_title


# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds

class Elastic():

  def __init__(self, host='localhost', port=9200):
    self.es = Elasticsearch([{'host': host, 'port' : port}])
    print "connection established to %s:%s" % (host, port)

  def dummy(self, _index):
    self.es.index(index=_index, doc_type="dummy", id="dummy", body={"dummy" : "dummy"})

  def title_exists(self, _index, _doc_type, title):
    le_search = {"query" : {
        "term" : {"_id" : title}
      }}
    r = self.es.count(index=_index, doc_type=_doc_type, body=le_search)
    return r["count"] > 0

  def get_single_article(self, _index, _doc_type, _id):
    return self.es.get(index=_index, doc_type=_doc_type, id=_id)["_source"]

  def get_multiple_articles(self, _index, _doc_type, ids):
    for _id in ids:
      yield self.get_single_article(_index, _doc_type, _id)["content"]

  def add_multiple_articles(self, _index, _doc_type, all_articles):
    for article in all_articles:
      title = article["title"]
      print "Added %s" % title
      self.es.index(index=_index, doc_type=_doc_type, id=title, body=article)

  def flush_all(self):
    if raw_input() != "flush":
      return
    print "started deleting all"
    self.es.delete(index="*", master_timeout=60000)
    print "all deleted: %s elements counted" % self.es.count(index="_all")

  def all_unpersisted_titles(self, _index, _doc_type, titles):
    result = []
    for title in titles:
      if not self.title_exists(_index, _doc_type, good_title(title)):
        result.append(title)
    return result
      
  def all_titles(self, _index, _doc_type):
    le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
    r = self.es.search(index=_index, doc_type=_doc_type, size=25000, body=le_search)
    return map(lambda x: x["_id"], r['hits']["hits"])

  def retrieve_scroll_id(self, _index, _doc_type, _size=100):
    query = {"query" : {"match_all" : {}}}
    first_response = self.es.search(index=_index, doc_type=_doc_type, body=query, search_type="scan", scroll="1m", size=_size)  
    return first_response['_scroll_id']

  def scroll_by_id(self, _index, _doc_type, _scroll_id):
    return self.es.scroll(scroll_id=_scroll_id, scroll= "1m")

  def generator_scroll(self, _index, _doc_type, _size=100):
    _id = self.retrieve_scroll_id(_index, _doc_type, _size)
    content = [""]
    while _id and content:
      data = self.scroll_by_id(_index, _doc_type, _id)
      content = data["hits"]["hits"]
      yield content
      _id = data['_scroll_id']





