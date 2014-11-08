# coding: utf-8
from __future__ import division

from nltk import FreqDist
from syntax import superior_tokenize
from syntax import remove_noise
from syntax import stem, lemmatize


def statistic_hash(text, h={}):
  # Before clean up
  tokens = superior_tokenize(text)
  h["lex_div"] = lexical_diversity(tokens)
  # After clean up
  tokens_rn = remove_noise(tokens)
  lemmas = list(lemmatize(tokens_rn))
  h["lemmas"] = lemmas_hash(lemmas)
  h["lexicon"] = lexicon(lemmas)
  return h

def lemmas_hash(lemmas):
  return { 
    "lemmas" : lemmas, 
    "size" : len(lemmas), 
    "lex_div" : lexical_diversity(lemmas) 
  }

def lexicon(lemmas):
  freqs = freq_dict(frequency([word.lower() for word in lemmas]))
  words = freqs.keys()
  return { 
    "freq_dist" : freqs,
    "size" : len(words),
    "avg_word_size" : average_word_size(words)
  }

def average_word_size(words):
  try:
    return reduce(lambda a,x: a + len(x), words, 0) / len(words)
  except:
    return 0

def lexical_diversity(tokens):
  try:
    return len(set(tokens)) / len(tokens)
  except:
    return 0

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())



