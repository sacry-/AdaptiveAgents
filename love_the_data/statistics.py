# coding: utf-8
from __future__ import division

from nltk import FreqDist
from syntax import tokenize
from syntax import remove_stop_words, remove_urls, remove_special_characters
from syntax import stem_and_lemmatize


def statistic_hash(text):
  h = {}

  h["tokens"] = tokens = tokenize(remove_urls(text))
  tokens_sc = remove_special_characters(tokens)

  h["lex_div"] = lexical_diversity(tokens_sc)

  tokens_sc_sw = remove_stop_words(tokens_sc)
  h["freq_dist"] = freq_dict(frequency(tokens_sc_sw))

  stems, lemmas = stem_and_lemmatize(tokens_sc_sw)
  h["stem"] = { "stems" : stems, "size" : len(stems), "lex_div" : lexical_diversity(stems) }
  h["lemmas"] = { "lemmas" : lemmas, "size" : len(lemmas), "lex_div" : lexical_diversity(lemmas) }
  freqs = freq_dict(frequency([word.lower() for word in lemmas]))
  h["lexicon"] = { 
    "freq_dist" : freqs,
    "size" : len(freqs.keys()),
    "avg_word_size" : reduce(lambda a,x: a + len(x), freqs.keys(), 0) / len(freqs.keys())
  }

  return h

def lexical_diversity(tokens):
  return len(set(tokens)) / len(tokens)

def frequency(tokens):
  return FreqDist(tokens)

def freq_dict(fdist):
  return dict((k, v) for k, v in fdist.iteritems())



