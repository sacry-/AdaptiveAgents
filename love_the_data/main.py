# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from elastic import Elastic
from io_utils import save_json
from statistics import statistic_hash


es = Elastic()
''' Some Test case
titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
          "brian_dale", "dependence_receptor", "despeciation", "biologist", "biology"]
articles = list(es.get_multiple_articles("biology", "title", titles))
h = statistic_hash(articles[0])
save_json(h, "sample_statistics")
'''

t1 = time.clock()
c = 0
lexi = 0
s1 = set([])
# time needed: 46.898816 for articles: 1000
try:
  for articles in es.generator_scroll("biology", "title", 25):
    for content in map(lambda a: a["_source"]["content"], articles):
      h = statistic_hash(content)
      lexi += h["lex_div"]
      s2 = set(h["lexicon"]["freq_dist"].keys())
      s3 = s1.union(s2)
      try:
        diff = (len(s2) / len(s1)) * 100
      except:
        diff = 0
      s1 = s3
      c += 1
      print "%s. %s <~> %s set=%s with diff %s" % (c, lexi / c, h["lex_div"], len(s1), diff)
except:
  pass

print "time needed: %s for articles: %s" % (time.clock() - t1, c)





