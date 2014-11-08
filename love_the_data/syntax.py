# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import re
import enchant # pip install pyenchant
from nltk import word_tokenize
from nltk import data
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

from utils import persistence_path
from io_utils import read
from ast import literal_eval


STOPS = literal_eval(read(persistence_path() + "/love_the_data/stop_words.txt"))
SPECIAL = literal_eval(read(persistence_path() + "/love_the_data/special_characters.txt"))
EN_US_DICT = enchant.Dict("en_US")
EN_GB_DICT = enchant.Dict("en_GB") 

def is_num(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def remove_noise(tokens):
  return [rm_special(token) for token in tokens if is_not_crap(token)]

def rm_special(token):
  return re.sub("[\.\\\/\|,;\:\-\_\*\+\&\%\$\!\?\#]", "", token)

def is_not_crap(x):
  return (
    # should not be empty
    x and
    # not be in stopwords
    not x in STOPS and 
    # not be in specials
    not re.match('(^\W+|\W+$)', x) and
    not x in SPECIAL and
    # should not be a num
    not is_num(x) and 
    # should be larger than 1 i.e. not "a" etc.
    len(x) > 1
  )

def remove_stop_words(tokens):
  return filter(is_not_crap, tokens)

def superior_tokenize(s):
  sent_detector = data.load('tokenizers/punkt/english.pickle')
  sentences = []
  for sentence in sent_detector.tokenize(s.strip()):
    if "See also" in sentence:
      return sentences
    if not any(delim in sentence for delim in ["http", "www", "://", "ISBN"]):
      sentences += word_tokenize(sentence)
  return sentences

def word_is_valid(word):
  return (
    # word should not be none
    word and 
    # word should be valid in a english dictionary
    (EN_US_DICT.check(word) and EN_GB_DICT.check(word)) or
    # average word length for biology assuming that the english word_list
    # does not contain specialized biology words
    (len(word) > 7 and
    # weird words containing large sequences of numbers are also included through
    # the lengths argument...
    not re.match(r'(\d{2,}.+|\w+\d{2,})', word))
  )

def lemmatize(tokens):
  wordnet_lemmatizer = WordNetLemmatizer()
  for token in tokens:
    if word_is_valid(token):
      yield wordnet_lemmatizer.lemmatize(token)

def stem(tokens):
  porter = PorterStemmer()
  for token in tokens:
    if word_is_valid(token):
      yield porter.stem(token).lower()


def train_stops(s):
  return re.match(r'^https?:\/\/.*[\r\n]*', s, flags=re.MULTILINE) or re.match('(^\W+|\W+$)', s)



