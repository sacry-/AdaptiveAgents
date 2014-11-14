import time
import sys
from elastic_old import Elastic
from rediss import Rediss
from category_knowledge import USED_CATEGORIES


# brew/apt-get? install redis
# sudo pip install redis-py
# sudo pip install redisdl
# DONE! :-)


es = Elastic()
rss = Rediss()

n = 0
items_per_pull = 10 # 5 shards * 10 = 50
t = time.clock()
try:
  for category in ["biology", "physics", "chemistry"]: #map(lambda s: s.lower(), USED_CATEGORIES):
    print "category: %s" % category
    for articles in es.generator_scroll(category, "title", items_per_pull):
      c = map(lambda a: (a["_source"]["title"], a["_source"]["content"]), articles)
      rss.add_articles_and_pos_tags(category, c)
      n += len(articles)
      t1 = time.clock() - t
      print "%s articles processed, time needed: %s" % (n, t1)
except:
  print "Unexpected error:", sys.exc_info()[0]
  pass
t1 = time.clock() - t
print "time needed: %s for articles: %s" % (t1, n)