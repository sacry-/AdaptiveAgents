# coding: utf-8

from __future__ import division

from nltk import FreqDist, pos_tag
from syntax import wiki_tokenize
from syntax import remove_noise
from syntax import lemmatize, stemmatize
from syntax import pos_tag
from syntax import LETTER_FREQ
from math import sqrt
import random


class Statistics():

  def __init__(self, text):
    self.tokens = wiki_tokenize(text)
    self.pos_tag = pos_tag(" ".join(self.tokens))
    self.tokens_without_noise = remove_noise(self.tokens)
    self.lemmas = Lemmas(self.tokens_without_noise)

  def as_dict(self):
    return {
      "stats" : {
        "pos_tags" : self.pos_tag,
        "lemmas" : self.lemmas.as_dict()
      }
    }

  def __repr__(self):
    return str(self.as_dict())


class Lemmas():

  def __init__(self, tokens):
    self.lemmas = list(stemmatize(tokens))
    frequencies = Frequencies(self.lemmas).create()
    self.frequency_distribution = frequencies.freq_dict
    self.lexical_diversity = lexical_diversity(self.lemmas)
    self.size = frequencies.size()
    self.average_lemma_complexity = frequencies.average_lc
    self.stddev_lemma_complexity = frequencies.stddev_lc
    self.average_and_stddev(frequencies.words())

  def as_dict(self):
    return {
      "freq_dist" : self.frequency_distribution,
      "lex_div" : self.lexical_diversity,
      "size" : self.size,
      "avg_lemma_complexity": self.average_lemma_complexity,
      "dev_lemma_complexity": self.stddev_lemma_complexity,
      "avg_word_size" : self.avgerage_word_size,
      "dev_word_size" : self.stddev_word_size
    }

  def average_and_stddev(self, words):
    a, b = avg_and_stddev_by(len, words, 0)
    self.avgerage_word_size = a
    self.stddev_word_size = b


class Frequencies():

  def __init__(self, lemmas):
    self.lemmas = lemmas
    self.fdist = FreqDist(self.lemmas)
    self.average_lc = 0
    self.stddev_lc = 0
    self.freq_dict = {}

  def create(self):
    self.freq_dict = {}
    acc_word_complexity = 0
    for lemma, count in self.fdist.iteritems():
      self.freq_dict[lemma] = (count, word_complexity(lemma))
    self.average_and_stddev(self.freq_dict.values())
    return self

  def average_and_stddev(self, d):
    a, b = avg_and_stddev_by(lambda x:x[1], d, 0)
    self.average_lc = a
    self.stddev_lc = b

  def words(self):
    return self.freq_dict.keys()

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



