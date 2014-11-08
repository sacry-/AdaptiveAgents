# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import re
# brew install enchant
# sudo pip install pyenchant
import enchant
from nltk import word_tokenize
from nltk import data
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
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

def remove_special_characters(tokens):
  return [re.sub("[\.\\\/\|,;\:\-\_\*\+\&\%\$\!\?\#]", "", s) for s in tokens]

def remove_urls(text):
  return re.sub(URLS, "", text)

def remove_stop_words(tokens):
  return filter(lambda x: x not in STOPS and not is_num(x) and len(x) > 1, tokens)

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

def stem_and_lemmatize(tokens):
  porter = PorterStemmer()
  wordnet_lemmatizer = WordNetLemmatizer()
  d = enchant.Dict("en_US")
  results = ([], [])
  for token in tokens:
    if token and d.check(token):
      results[0].append(porter.stem(token))
      results[1].append(wordnet_lemmatizer.lemmatize(token))
  return results





