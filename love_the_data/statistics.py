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


class Frequencies():

  def __init__(self, rss, category):
    self.titles = map(lambda x: rss.real_title(x), rss.all_pos_keys("%s*" % category))
    self.freqs = map(Frequency, rss.get_pos_tags(category, self.titles))
    self.cache = {}

  def idf(self, t):
    if self.cache.has_key(t):
      return cache[t]
    n = reduce(lambda acc, freq: acc + freq.idf(t), self.freqs, 0)
    try:
      result = math.log(len(self.titles) / n)
      self.cache[t] = result
      return result
    except:
      return 0

class Frequency():

  def __init__(self, pos_tags):
    self.pos_tags = pos_tags # {"words" : {"tags" : counts}}
    self.fdist = None

  def tf(self, t):
    return sum(self.pos_tags.get(t, {}).values())

  def idf(self, t):
    if self.pos_tags.has_key(t):
      return 1
    else:
      return 0

  def fdist(self):
    if not self.fdist:
      self.fdist = FreqDist(self.pos_tags.keys())
    return self.fdist

  def words(self):
    return self.fdist().keys()

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



