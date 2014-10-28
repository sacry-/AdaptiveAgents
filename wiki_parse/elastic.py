from elasticsearch import Elasticsearch
from wiki_api import good_title, fetch_articles_by_titles
import time

# localhost:9200/biology/title/[:article_title]
# i.e. localhost:9200/biology/title/biologist
# i.e. localhost:9200/biology/title/bioactive_plant_food_compounds

class Elastic():

  def __init__(self, host='localhost', port=9200):
    self.es = Elasticsearch([{'host': host, 'port' : port}])

  def dummy(self, _index):
    self.es.index(index=_index, doc_type="dummy", id="dummy", body={"dummy" : "dummy"})

  def title_exists(self, _index, _doc_type, title):
    le_search = {"query" : {
        "term" : {"_id" : title}
      }}
    r = self.es.count(index=_index, doc_type=_doc_type, body=le_search)
    return r["count"]

  def get_single_article(self, _index, _doc_type, _id):
    return self.es.get(index=_index, doc_type=_doc_type, id=_id)["_source"]

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

  def fetch_articles_and_add_to_elastic_search(self, titles, _index, _doc_type):
    group_factor, done = 10, 0
    grouped_titles = [titles[i:i+group_factor] for i in range(0, len(titles), group_factor)]
    last, acc = 0, 0
    for sub_titles in grouped_titles:
      before = time.time()
      all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
      self.add_multiple_articles(_index, _doc_type, all_articles)
      end = time.time() - before
      acc += end
      done += group_factor
      self.print_download_status(len(titles), done, acc)

  def print_download_status(self, titles_size, done, acc):
    articles_to_go = titles_size - done
    needed = ((acc / done) * articles_to_go) / 60
    print "%s articles and %s mins to go" % (articles_to_go, needed)
      
  def all_titles(self, _index, _doc_type):
    le_search = {"fields" : ["title"], "query" : { "match_all" : {}}}
    r = self.es.search(index=_index, doc_type=_doc_type, size=25000, body=le_search)
    return map(lambda x: x["_id"], r['hits']["hits"])


