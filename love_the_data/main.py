# coding: utf-8
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

for articles in es.generator_scroll("biology", "title"):
  for content in map(lambda a: a["_source"]["content"], articles):
    h = statistic_hash(content)
    lexi += h["lex_div"]
    c += 1
    print lexi / c
  if c >= 1000:
    break

print "time needed: %s for articles: %s" % (time.clock() - t1, c)

