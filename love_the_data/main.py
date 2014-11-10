# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from elastic import Elastic
from io_utils import save_json
from statistics import statistic_hash, new_statistic_hash


def update_single_document(es):
  titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
            "brian_dale", "dependence_receptor", "despeciation", "biologist", "biology"]
  articles = list(es.get_multiple_articles("biology", "title", titles))
  h = statistic_hash(articles[0])
  print h
  # es.update_article("biology", "title", "biology", h)
  save_json("love_the_data", "sample_statistics", h)


# time needed: 46.898816 for articles: 1000 forall ~> 2hours (95k)
def time_statistics(es):
  n = 0
  t1 = time.clock()
  try:
    for articles in es.generator_scroll("biology", "title", 5):
      for source in map(lambda a: a["_source"], articles):
        h = statistic_hash(source["content"])
        n += 1
      t = time.clock() - t1
      print "%s articles processed, time needed: %s" % (n, t)
  except:
    pass
  t = time.clock() - t1
  print "time needed: %s for articles: %s" % (t, n)

def update_biology_with_stats(es):
  c = 0
  for articles in es.generator_scroll("biology", "title", 25):
    for source in map(lambda a: a["_source"], articles):
      es.update_article("biology", "title", source["title"], statistic_hash(source["content"]))
      c += 1
    print "%s articles processed" % c


es = Elastic()
# multiple_test(es)
# update_single_document(es)
# print es.count("biology", "title")
# print es.stats_of("biology", "title", "biology")
# print es.freq_dist_of("biology", "title", "biology")
update_single_document(es)



