# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from elastic import Elastic
from io_utils import save_json
from statistics import statistic_hash


def single_test(es):
  titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
            "brian_dale", "dependence_receptor", "despeciation", "biologist", "biology"]
  articles = list(es.get_multiple_articles("biology", "title", titles))
  h = statistic_hash(articles[0])
  save_json("love_the_data", "sample_statistics", h)


# time needed: 46.898816 for articles: 1000 forall ~> 2hours (95k)
def multiple_test(es):
  n = 0
  biology_words = set([])
  biology_average_word_size = 0

  t1 = time.clock()
  try:
    for articles in es.generator_scroll("biology", "title", 25):
      for source in map(lambda a: a["_source"], articles):
        h = statistic_hash(source["content"])
        new_words = set(h["lexicon"]["freq_dist"].keys())
        biology_average_word_size += h["avg_word_size"]
        s3 = biology_words.union(new_words)
        biology_words = s3
        n += 1
      print "%s articles processed, lexicon has %s words" % (n, len(biology_words))
  except:
    pass
  t = time.clock() - t1
  print "time needed: %s for articles: %s" % (t, n)
  
  h = {
    "time" : t, 
    "avg_word_size" : biology_average_word_size / n, 
    "biology_words" : list(biology_words)
  }
  # save_json("love_the_data", "biology_words", h)


es = Elastic()
single_test(es)


