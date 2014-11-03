from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from elastic import Elastic
from nltk import FreqDist
from syntax import tokenize

# collocation

def remove_stupid_characters(tokens):
  # Swaneets code
  return tokens

def lexical_diversity(text):
  return len(text) / len(set(text))

def frequency(text):
  return FreqDist(tokenize(text))

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())


titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
          "brian_dale", "dependence_receptor", "despeciation"]
es = Elastic()
# articles = list(es.get_multiple_articles("biology", "title", titles))



