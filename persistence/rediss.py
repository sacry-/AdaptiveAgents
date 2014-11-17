import os, sys
p = "%s/../love_the_data" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import redis
import redisdl
import ast
from syntax import Words
from utils import persistence_path


LEVAL = ast.literal_eval


'''
Redis has as its default 16 local different db tables (0-15).
0 is the default connection. To make use of "two" redis instances
for performance we connect to db0 (rs_raw) for the text and
db1 (rs_pos) for the tagged form of the text. Internally whenever we call
for articles the raw db and for tags the pos db. Simple...
'''
class Rediss():

  def __init__(self, host="localhost", port=6379):
    self.host = host
    self.port = port
    self.rs_raw = redis.Redis(host=self.host, port=self.port, db=0)
    self.rs_pos = redis.Redis(host=self.host, port=self.port, db=1)

  def article_key(self, prefix, title):
    return "%s-content:%s" % (prefix, title)

  def pos_tag_key(self, prefix, title):
    return "%s-pos:%s" % (prefix, title)

  def add_article(self, category, title, content):
    self.rs_raw.set(self.article_key(category, title), content)

  def add_pos_tag(self, category, title, content):
    self.rs_pos.set(self.pos_tag_key(category, title), Words(content).tags())

  def add_articles(self, category, c):
    for (title, content) in c:
      self.add_article(category, title, content)

  def add_pos_tags(self, category, c):
    for (title, content) in c:
      self.add_pos_tag(category, title, content)

  def add_articles_and_pos_tags(self, category, c):
    self.add_articles(category, c)
    self.add_pos_tags(category, c)

  def get_article(self, category, title):
    return self.rs_raw.get(self.article_key(category, title))

  def get_articles(self, category, titles):
    return self.rs_raw.mget(map(lambda t: self.article_key(category, t), titles))

  def get_pos_tag(self, category, title):
    s = self.rs_pos.get(self.pos_tag_key(category, title))
    if s:
      return LEVAL(s)
    return {}

  def get_pos_tags(self, category, titles):
    keys = map(lambda t: self.pos_tag_key(category, t), titles)
    for tags in self.rs_pos.mget(keys):
      if tags:
        yield LEVAL(tags)

  def all_article_keys(self, pattern="*"):
    for key in self.rs_raw.keys(pattern): 
      yield key

  def all_pos_keys(self, pattern="*"):
    for key in self.rs_pos.keys(pattern): 
      yield key

  def dump(self):
    for _db in [0, 1]:
      with open('%scategories/dump%s.json' % (persistence_path(), _db), 'w+') as f:
        redisdl.dump(f, db=_db, host=self.host, port=self.port, encoding='iso-8859-1', pretty=True)

  def restore(self):
    for _db in [0, 1]:
      with open('%scategories/dump%s.json' % (persistence_path(), _db), "r+") as f:
        redisdl.load(f, db=_db, host=self.host, port=self.port)

  def flushall(self):
    if raw_input("type 'flush' to kill data") == "flush":
      self.rs_raw.flushall()
      print "all dbs are empty now!"

  def flushdb(self):
    response = raw_input("type '0' or '1' to kill data for db")
    if response == "0":
      self.rs_raw.flushdb()
    elif response == "1":
      self.rs_pos.flushdb()
    else:
      return
    print "db%s is empty now!" % response


def test():
  titles = ["fluorenylmethyloxycarbonyl_chloride", "biology", 
  "biologist", "biological_ornament", "birth", "cell_population_data",
  "brian_dale", "dependence_receptor", "despeciation"]
  rss = Rediss()
  for elem in rss.get_pos_tags("biology", titles):
    print elem

# test()
# rss = Rediss()






''' Examples from nosql
def string_to_hash(json_string):
  return ast.literal_eval(json_string)

def get_key(r_server, plz):
  return string_to_hash(r_server.get(plz))

def get_city_and_state_r(r_server, plz):
  res = get_key(r_server, plz)
  return (res["city"], res["state"])

def plz_for_town_r(r_server, town):
  return r_server.lrange(town, 0, r_server.llen(town))

def plz_for_town_slow(r_server, town):
  for key in r_server.keys("[0-9][0-9]*"):
    if get_key(r_server, key)["city"] == town:
      yield key

def plz_for_town(r_server, town):
  return r_server.lrange(town, 0, r_server.llen(town))
'''




