# coding: utf-8
from __future__ import division

import nltk
import math
from nltk import FreqDist, pos_tag
from syntax import wiki_tokenize
from syntax import remove_noise
from syntax import lemmatize, stemmatize
from syntax import pos_tag, stem_with_pos_tags
from syntax import LETTER_FREQ
from math import sqrt
import random
import time

# if this is set to true, then call Frequencies(..., rfeature) with rfeature as an extra argument.
# this makes calls to tf and idf much faster and there is no overhead in loading at the beginning.
REDIS_HAS_IDFS = True

class Frequencies():

  def __init__(self, rpos, category, rfeature=None):
    if rfeature:
        self.rfeature = rfeature
    self.titles = map(lambda x: rpos.real_title(x), rpos.keys("%s*" % category))
    self.rpos = rpos
    # freqs = {"biologist": Frequency(...), "despiciation": Frequency(...), ...}
    if not REDIS_HAS_IDFS:
        self.freqs = dict((title, Frequency(ptags)) for title, ptags in zip(self.titles, rpos.values_by_titles(category, self.titles)))
    else:
        self.freqs = {}
    self.num_of_docs = len(self.titles)
    self.cache = {} # saches calls of idf(t)
    self.cat = category

  # Term -> Float
  def idf(self, t):
    if REDIS_HAS_IDFS:
        return self.rfeature.value_by_title(self.cat, t) or 0
    if self.cache.has_key(t):
      return self.cache[t]
    n = reduce(lambda acc, freq: acc + freq.idf(t), self.freqs.values(), 0)
    try:
      result = math.log(self.num_of_docs / float(n))
      self.cache[t] = result
      return result
    except:
      return 0
  
  # term frequency of term t in document d. if document d doesn't exist, it returns 0
  # Term -> Title -> Int
  def tf(self, t, title):
    if REDIS_HAS_IDFS:
        self.freqs[title] = Frequency(self.rpos.value_by_title(self.cat, title))
    if not self.freqs.has_key(title):
        return 0
    return self.freqs[title].tf(t)
    
  # Term -> Title -> Float
  def w(self, t, d):
    return self.tf(t,d) * self.idf(t)
  
  # Title ( -> Int) -> [(Term,Float)]
  def feature_vector(self, d, maxLen=25):
    self.tf("dummy",d) # force self.freqs[d] to be loaded
    words = self.freqs[d].words()
    print "[2] %s len: %s" % (diff(), self.freqs[d].size())
    
    weighted_vector = map(lambda t: (t, self.w(t,d)) , words)
    # this is the bottle neck. this is why, calculating the feature vector takes so long.
    # it take ~15 seconds for a signel article with ~954 words.
    # this could be optimized by implementing multi get for tf, idf and weight. this will make this faster definitely.
    
    fvector = sorted(weighted_vector, key=lambda x:-x[1]) # sort by weight descending
    return fvector[0:maxLen]

class Frequency():

  def __init__(self, pos_tags):
    self.pos_tags = pos_tags # {"words" : {"tags" : counts}}

  def tf(self, t):
    return sum(self.pos_tags.get(t, {}).values())

  def idf(self, t):
    if self.pos_tags.has_key(t):
      return 1
    else:
      return 0

  def words(self):
    return self.pos_tags.keys()

  def size(self):
    return len(self.words())


def average_by(f, words, default):
  try:
    return reduce(lambda a,x: a + f(x), words, 0) / len(words)
  except:
    return default

def avg_and_stddev_by(f, ls, default): # http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Incremental_algorithm
  n = 0
  mean = default
  m2 = 0
  for x in ls:
    n += 1
    y = f(x)
    delta = y - mean
    mean += delta/n
    m2 += delta*(y - mean)
  if (n < 2):
    return mean, 0
  stddev = sqrt(m2/(n - 1))
  return mean, stddev

def lexical_diversity(tokens):
  try:
    return len(set(tokens)) / len(tokens)
  except:
    return 0

# See word_complexity_demo.py. not official or scientific. I just invented something which works ok.
def word_complexity(w):
  l = len(w)
  if l == 0:
    return 0
  pre = word_complexity(w[0:l-1])
  weight = (1 - LETTER_FREQ.get(w[l-1].lower(), 1))
  return pre + (1 - pre)*pow(weight, 40)



