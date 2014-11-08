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
  keys = freqs.keys()
  keys_size = len(keys)
  return { 
    "freq_dist" : freqs,
    "size" : keys_size,
    "avg_word_size" : reduce(lambda a,x: a + len(x), keys, 0) / keys_size
  }

def lexical_diversity(tokens):
  return len(set(tokens)) / len(tokens)

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())



