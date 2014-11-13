# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from elastic import Elastic
from io_utils import save_json
from statistics import Statistics


def update_single_document(es):
  titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
            "brian_dale", "dependence_receptor", "despeciation", "biologist", "biology"]
  articles = list(es.get_multiple_articles("biology", "title", titles))
  s = Statistics(articles[0])
  print s
  # es.update_article("biology", "title", "biology", h)
  save_json("love_the_data", "sample_statistics", s.as_dict())

# time needed: 46.898816 for articles: 1000 forall ~> 2hours (95k)
def time_statistics(es):
  n = 0
  t1 = time.clock()
  try:
    for articles in es.generator_scroll("biology", "title", 5):
      for source in map(lambda a: a["_source"], articles):
        s = Statistics(source["content"])
        s.as_dict()
        n += 1
      t = time.clock() - t1
      print "%s articles processed, time needed: %s" % (n, t)
  except:
    pass
  t = time.clock() - t1
  print "time needed: %s for articles: %s" % (t, n)

def update_biology_with_stats(es, override):
  c = 0
  for articles in es.generator_scroll("biology", "title", 25):
    for source in map(lambda a: a["_source"], articles):
      if not source.has_key("stats") or override:
          s = Statistics(source["content"])
          es.update_article("biology", "title", source["title"], s.as_dict())
      c += 1
    print "%s articles processed" % c

es = Elastic()
time_statistics(es)

