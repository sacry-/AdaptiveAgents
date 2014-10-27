from nltk import clean_html, word_tokenize, data

from dewiki.parser import Parser # https://github.com/daddyd/dewiki.git
from io_utils import read, save
import re
import time

def remove_curly_braces(s):
  buf = []
  c = 0
  for char in s:
    if char == '{':
      c += 1
      continue
    elif char == '}':
      c -=1
      continue
    elif c == 0:
      buf.append(char)
  return "".join(buf)

def remove_markup(s):
  return Parser().parse_string(s)

def remove_html(s):
  return clean_html(s)

def clean_parse(s):
  return remove_html(remove_markup(remove_curly_braces(s)))


# Syntax...
def tag(sentence):
  return str(word_tokenize(sentence))

def sentence_tokenize(s):
  sent_detector = data.load('tokenizers/punkt/english.pickle')
  sentences = []
  for sentence in sent_detector.tokenize(s.strip()):
    if sentence.find("See also") != -1:
      return "\n--------\n".join(sentences)
    sentences.append(tag(sentence))
  return "\n--------\n".join(sentences)
