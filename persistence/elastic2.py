# coding: utf-8
import math
from elasticsearch import Elasticsearch
from utils import good_title

# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds

class Elastic2():

  def __init__(self, host='localhost', port=9200, index="biology", doc_type="title"):
    self.es = Elasticsearch([{'host': host, 'port' : port}])
    self.index = index
    self.doc_type = doc_type
    print "connection established to %s:%s for index: %s" % (host, port, index)

  def dummy(self):
    self.es.index(index=self.index, doc_type="dummy", id="dummy", body={"dummy" : "dummy"})

  def title_exists(self, title):
    le_search = {"query" : {
        "term" : {"_id" : title}
      }}
    r = self.es.count(index=self.index, doc_type=self.doc_type, body=le_search)
    return r["count"] > 0

  def count(self,le_search={"query" : {"match_all" : {}}}):
    return self.es.count(index=self.index, doc_type=self.doc_type, body=le_search)["count"]

  def get_single_article(self, title):
    return self.es.get(index=self.index, doc_type=self.doc_type, id=title)["_source"]

  def get_multiple_articles(self, titles):
    for title in titles:
      yield self.get_single_article(title)

  def add_multiple_articles(self, all_articles):
    for article in all_articles:
      title = article["title"]
      print "Added %s" % title
      self.es.index(index=self.index, doc_type=self.doc_type, id=title, body=article)

  def flush_all(self):
    if raw_input() != "flush":
      return
    print "started deleting all"
    self.es.delete(index="*", master_timeout=60000)
    print "all deleted: %s elements counted" % self.es.count(index="_all")

  def all_unpersisted_titles(self, titles):
    result = []
    for title in titles:
      if not self.title_exists(good_title(title)):
        result.append(title)
    return result
  
  def update_articles(self, titles):
    for (title, stats) in titles:
      self.update_article(title, {"doc" : stats})

  def update_article(self, title, information_as_hash):
    self.es.update(self.index, self.doc_type, title, {"doc" : information_as_hash})

  def all_titles(self):
    le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
    r = self.es.search(index=self.index, doc_type=self.doc_type, size=25000, body=le_search)
    return map(lambda x: x["_id"], r['hits']["hits"])

  def retrieve_scroll_id(self, _size=100):
    query = {"query" : {"match_all" : {}}}
    first_response = self.es.search(index=self.index, doc_type=self.doc_type, body=query, search_type="scan", scroll="1m", size=_size)  
    return first_response['_scroll_id']

  def scroll_by_id(self, _scroll_id):
    return self.es.scroll(scroll_id=_scroll_id, scroll= "1m")

  def generator_scroll(self, _index, _doc_type, _size=100):
    _id = self.retrieve_scroll_id(_size)
    content = [""]
    while _id and content:
      data = self.scroll_by_id(_id)
      content = data["hits"]["hits"]
      yield content
      _id = data['_scroll_id']

  def stats_of(self, title):
    return self.get_single_article(title)["stats"]

  def freq_dist_of(self, title):
    return self.stats_of(title)['lemmas']["freq_dist"]

  def term_freq(self, title, word):
    try:
      count, _ = self.freq_dist_of(title).get(word)
      return count
    except:
      return 0

  def inverse_doc_freq(self, t):
    n = 0
    for d in titles:
      if t in self.freq_dist_of(title):
        n += 1
    if n == 0:
      print "Term %s doesn't occur in any documents!" % t
      n = 1 # beware of division by zero.
    return log(abs_D / n )

