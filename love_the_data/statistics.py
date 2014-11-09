# coding: utf-8

from __future__ import division

from nltk import FreqDist, pos_tag
from syntax import wiki_tokenize
from syntax import remove_noise
from syntax import lemmatize, stemmatize
from syntax import word_complexity

def statistic_hash(text, h={}):
  # Before clean up
  tokens = wiki_tokenize(text)
  # h["pos_tag"] = pos_tag(tokens) # COSTS A LOT OF TIME ;( roughly 5-6x times slower..
  h["lex_div"] = lexical_diversity(tokens)
  # After clean up
  tokens_rn = remove_noise(tokens)
  h["avg_word_size"] = average_word_size(tokens_rn)
  lemmas = list(stemmatize(tokens_rn))
  h["lemmas"] = lemmas_hash(lemmas)
  h["lexicon"] = lexicon(lemmas)
  return h

def lemmas_hash(lemmas):
  return { 
    "lemmas" : lemmas, 
    "size" : len(lemmas),
    "lex_div" : lexical_diversity(lemmas),
    "avg_lemma_complexity": average_lemma_complexity(lemmas),
    "lemma_complexities": dict([(l, word_complexity(l))for l in lemmas])
  }

def lexicon(lemmas):
  freqs = freq_dict(frequency([word.lower() for word in lemmas]))
  words = freqs.keys()
  return { 
    "freq_dist" : freqs,
    "size" : len(words),
    "avg_word_size" : average_word_size(words)
  }

def average_lemma_complexity(lemmas):
    return average_by(word_complexity, lemmas, 0)

def average_word_size(words):
    return average_by(len, words, 0)

def average_by(f, words, default):
  try:
    return reduce(lambda a,x: a + f(x), words, 0) / len(words)
  except:
    return default

def lexical_diversity(tokens):
  try:
    return len(set(tokens)) / len(tokens)
  except:
    return 0

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())

