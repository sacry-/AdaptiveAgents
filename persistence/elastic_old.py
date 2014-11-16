# coding: utf-8
from elasticsearch import Elasticsearch
from utils import good_title
import math

# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds
  
titles_cache = {}

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

  def count(self, _index, _doc_type, le_search={"query" : {"match_all" : {}}}):
    return self.es.count(index=_index, doc_type=_doc_type, body=le_search)["count"]

  def get_single_article(self, _index, _doc_type, _id):
    return self.es.get(index=_index, doc_type=_doc_type, id=_id)["_source"]

  def get_multiple_articles(self, _index, _doc_type, ids):
    for _id in ids:
      yield self.get_single_article(_index, _doc_type, _id)["content"]

  def get_multiple_sources(self, _index, _doc_type, ids):
    for _id in ids:
      yield self.get_single_article(_index, _doc_type, _id)

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
  
  def update_articles(self, _index, _doc_type, titles):
    for (title, stats) in titles:
      self.update_article(_index, _doc_type, title, {"doc" : stats})

  def update_article(self, _index, _doc_type, title, information_as_hash):
    self.es.update(_index, _doc_type, title, {"doc" : information_as_hash})

  def add_statistics(self, _index, title, information_as_hash):
    self.es.index(index=_index + "_stats", doc_type="stats", id=title, body=information_as_hash)

  def all_titles(self, _index, _doc_type):
    le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
    r = self.es.search(index=_index, doc_type=_doc_type, size=25000, body=le_search)
    return map(lambda x: x["_id"], r['hits']["hits"])

  def retrieve_scroll_id(self, _index, _doc_type, _size=100):
    _body = {"query" : {"match_all" : {}}}
    first_response = self.es.search(index=_index, doc_type=_doc_type, body=_body, search_type="scan", scroll="59m", size=_size)  
    return first_response['_scroll_id']

  def scroll_by_id(self, _index, _doc_type, _scroll_id):
    return self.es.scroll(scroll_id=_scroll_id, scroll= "5m")

  def generator_scroll(self, _index, _doc_type, _size=100):
    _id = self.retrieve_scroll_id(_index, _doc_type, _size)
    content = [""]
    while _id and content:
      data = self.scroll_by_id(_index, _doc_type, _id)
      content = data["hits"]["hits"]
      yield content
      _id = data['_scroll_id']

  def stats_of(self, _index, _doc_type, title):
    return self.get_single_article(_index, _doc_type, title)["stats"]

  def freq_dist_of(self, _index, _doc_type, title):
    return self.stats_of(_index, _doc_type, title)['lemmas']["freq_dist"]

  def term_freq(self, _index, _doc_type, title, word):
    try:
      count, _ = self.freq_dist_of(_index, _doc_type, title).get(word)
      return count
    except:
      return 0
  
  def inverse_doc_freq(es, index, doc_type, t):
    n = 0
    for d in es.get_titles(index, doc_type):
      if t in es.freq_dist_of(index, doc_type, title):
        n += 1
    if n == 0:
      print "Term %s doesn't occur in any documents!" % t
      n = 1 # beware of division by zero.
    return log(abs_D / n )
  
  def preload_titles(self, index, doc_type):
    if not titles_cache.has_key(index):
        titles_cache[index]=self.all_titles(index, doc_type)

  def get_titles(self, index, doc_type):
    if not titles_cache.has_key(index):
        self.preload_titles(index, doc_type)
    return titles_cache[index]




