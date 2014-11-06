# coding: utf-8

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)


import re
from nltk import word_tokenize, data
from nltk.corpus import stopwords
from utils import persistence_path
from io_utils import save, read
from ast import literal_eval


STOPS = literal_eval(read(persistence_path() + "/love_the_data/stop_words.txt"))
URLS = re.compile(r'''(?i)\b((?:https?:(//|\\)|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''')

def is_num(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def remove_urls(text):
  return re.sub(URLS, "", text)

def remove_stop_words(tokens):
  return filter(lambda x: x not in STOPS and not is_num(x), tokens)

def train_stops(s):
  return re.match(r'^https?:\/\/.*[\r\n]*', s, flags=re.MULTILINE) or re.match('^\W{1,2}$', s)

def tokenize(s):
  return word_tokenize(s)

def sentence_tokenize(s):
  sent_detector = data.load('tokenizers/punkt/english.pickle')
  sentences = []
  for sentence in sent_detector.tokenize(s.strip()):
    if sentence.find("See also") != -1:
      return sentences
    sentences.append(tokenize(sentence))
  return sentences





