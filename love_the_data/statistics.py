# coding: utf-8

from __future__ import division

from nltk import FreqDist, pos_tag
from syntax import wiki_tokenize
from syntax import remove_noise
from syntax import lemmatize, stemmatize
from syntax import word_complexity
from syntax import pos_tag, lemmatize_by_pos_tags

def statistic_hash(text, h={}):
  # Before clean up
  tokens = wiki_tokenize(text)
  h["lex_div"] = lexical_diversity(tokens)
  # After clean up
  tokens_rn = remove_noise(tokens)
  h["avg_word_size"] = average_word_size(tokens_rn)
  lemmas = list(stemmatize(tokens_rn))
  h["lemmas"] = lemmas_hash(lemmas)
  return { "stats" : h }

def new_statistic_hash(text, h={}):
  tokens = wiki_tokenize(text)
  h["pos_tag"] = pos_tags = pos_tag(" ".join(tokens))
  h["lex_div"] = lexical_diversity(tokens)
  tokens_rn = remove_noise(tokens)
  h["avg_word_size"] = average_word_size(tokens_rn)
  h["lemmas"] = list(lemmatize_by_pos_tags(pos_tags))
  return { "stats" : h }

def lemmas_hash(lemmas):
  freqs, avg_lemma_complexity = freq_dict(frequency([word.lower() for word in lemmas]))
  words = freqs.keys()
  return { 
    "freq_dist" : freqs,
    "lex_div" : lexical_diversity(lemmas),
    "size" : len(words),
    "avg_lemma_complexity": avg_lemma_complexity,
    "avg_word_size" : average_word_size(words)
  }

def average_lemma_complexity(accumulated_complexity, lemma_size):
  try:
    return accumulated_complexity / lemma_size
  except:
    return 0

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
  d = {}
  acc_word_complexity = 0
  for lemma, count in fdist.iteritems():
    complexity = word_complexity(lemma)
    d[lemma] = (count, complexity)
    acc_word_complexity += complexity
  return (d, 
    average_lemma_complexity(acc_word_complexity, len(fdist.keys()))
  )


