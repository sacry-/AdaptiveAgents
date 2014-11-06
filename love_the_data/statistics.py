# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)


from elastic import Elastic
from nltk import FreqDist
from syntax import tokenize, remove_stop_words, remove_urls
from io_utils import save_json


def statistic_hash(text):
  h = {}
  tokens = tokenize(remove_urls(text))
  h["lex_div"] = lexical_diversity(tokens)
  tokens_no_stops = remove_stop_words(tokens)
  h["freq_dist"] = freq_dict(frequency(tokens_no_stops))
  h["lexicon"] = h["freq_dist"].keys()

  return h

def lexicon(tokens):
  return list(set(tokens))

def lexical_diversity(tokens):
  return len(set(tokens)) / len(tokens)

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())


titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
          "brian_dale", "dependence_receptor", "despeciation"]
es = Elastic()
articles = list(es.get_multiple_articles("biology", "title", titles))
h = statistic_hash(articles[0])
# save_json(h, "sample_statistics")




