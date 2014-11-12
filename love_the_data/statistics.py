# coding: utf-8

from __future__ import division

from nltk import FreqDist, pos_tag
from syntax import wiki_tokenize
from syntax import remove_noise
from syntax import lemmatize, stemmatize
from syntax import word_complexity
from syntax import pos_tag, lemmatize_by_pos_tags
from math import sqrt
import random

def statistic_hash(text):
  h = {}
  # Before clean up
  tokens = wiki_tokenize(text)
  # After clean up
  tokens_rn = remove_noise(tokens)
  lemmas = list(stemmatize(tokens_rn))
  h["lemmas"] = lemmas_hash(lemmas)
  return { "stats" : h }

def new_statistic_hash(text):
  h = {}
  tokens = wiki_tokenize(text)
  h["pos_tag"] = pos_tags = pos_tag(" ".join(tokens))
  h["lex_div"] = lexical_diversity(tokens)
  tokens_rn = remove_noise(tokens)
  h["avg_word_size"] = average_word_size(tokens_rn)
  h["lemmas"] = list(lemmatize_by_pos_tags(pos_tags))
  return { "stats" : h }

def lemmas_hash(lemmas):
  freqs, avg_lc, stddev_lc = freq_dict(frequency([word.lower() for word in lemmas]))
  words = freqs.keys()
  avg_ws, stddev_ws = avg_and_stddev_by(len, words, 0)
  return { 
    "freq_dist" : freqs,
    "lex_div" : lexical_diversity(lemmas),
    "size" : len(words),
    "avg_lemma_complexity": avg_lc,
    "dev_lemma_complexity": stddev_lc,
    "avg_word_size" : avg_ws,
    "dev_word_size" : stddev_ws
  }

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

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  d = {}
  acc_word_complexity = 0
  for lemma, count in fdist.iteritems():
    d[lemma] = (count, word_complexity(lemma))
  avg, stddev = avg_and_stddev_by(lambda x:x[1], d.values(), 0)
  return (d, avg, stddev)


