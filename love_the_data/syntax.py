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
from io_utils import read, load_json
from ast import literal_eval

# Pos Tagging
from textblob import TextBlob
from textblob_aptagger import PerceptronTagger


STOPS = literal_eval(read(persistence_path() + "/love_the_data/stop_words.txt"))
SPECIAL = literal_eval(read(persistence_path() + "/love_the_data/special_characters.txt"))
LETTER_FREQ = dict(load_json("love_the_data","english-letter-frequencies")["letters"])
EN_US_DICT = enchant.Dict("en_US")
EN_GB_DICT = enchant.Dict("en_GB")
TAGGER = PerceptronTagger()
PORTER = PorterStemmer()
WN_LEMMATIZER = WordNetLemmatizer()
SENTENCE_DETECTOR = data.load('tokenizers/punkt/english.pickle')

def is_num(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def is_not_noisy(x):
  return (
    # should not be empty
    x and
    # not be in stopwords
    not (x in STOPS or 
    # not be in specials
    re.match('(^\W+|\W+$)', x) or x in SPECIAL or
    # should not be a num
    is_num(x)) and 
    # should be larger than 1 i.e. not "a" etc.
    len(x) > 1
  )

def word_is_valid(word):
  return (
    # word should not be none
    word and 
    # word should be valid in a english dictionary
    (EN_US_DICT.check(word) and EN_GB_DICT.check(word)) or
    # average word length for biology assuming that the english word_list
    # does not contain specialized biology words
    (len(word) > 6 and
    # weird words containing large sequences of numbers are also included through
    # the lengths argument...
    not re.match(r'(\d{2,}.+|\w+\d{2,})', word))
  )

def remove_noise(tokens):
  return [remove_special(token) for token in tokens if is_not_noisy(token)]

def remove_special(token):
  return re.sub("[\.\\\/\|,;\:\-\_\*\+\&\%\$\!\?\#]", "", token)

def wiki_tokenize(s):
  sentences = []
  for sentence in SENTENCE_DETECTOR.tokenize(s.strip()):
    if "See also" in sentence:
      return sentences
    if not any(delim in sentence for delim in ["http", "www", "://", "ISBN"]):
      sentences += word_tokenize(sentence)
  return sentences

def stemmatize(tokens): # work heavy!
  for token in tokens:
    if word_is_valid(token):
      yield PORTER.stem(WN_LEMMATIZER.lemmatize(token)).lower()

def lemmatize(tokens):
  for token in tokens:
    if word_is_valid(token):
      yield WN_LEMMATIZER.lemmatize(token)

def stem(tokens):
  for token in tokens:
    if word_is_valid(token):
      yield PORTER.stem(token).lower()

def pos_tag(text):
  blob = TextBlob(text, pos_tagger=TAGGER)
  return blob.tags


# Artifacts
def remove_stop_words(tokens):
  return filter(lambda x: not x in STOPS, tokens)

def train_stops(s):
  return re.match(r'^https?:\/\/.*[\r\n]*', s, flags=re.MULTILINE) or re.match('(^\W+|\W+$)', s)


