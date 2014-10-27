from nltk import clean_html, word_tokenize, data

from dewiki.parser import Parser # https://github.com/daddyd/dewiki.git
from wiki_api import fetch_articles_by_titles
from io_utils import read, save
import re
import time

def remove_special(s):
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

# single_step_test("biology_2.txt", "biology_nested.txt", remove_special)
def single_step_test(fn_read, fn_write, f):
  save(fn_write, f(read(fn_read)))

def test():
  #article = fetch_articles_by_titles(["biology"], 1)
  #save("biology.txt", article[0]["content"])
  base = "test_data/"
  t = read("%sbiology.txt" % base)
  t1 = remove_special(t)
  save("%sbiology_1.txt" % base, t1)
  t2 = remove_markup(t1)
  save("%sbiology_2.txt" % base, t2)
  t3 = remove_html(t2)
  save("%sbiology_3.txt" % base, t3)
  t4 = sentence_tokenize(t3)
  save("%sbiology_4.txt" % base, str(t4))

t = time.clock()
for _ in range(0, 1):
  test()
t1 = time.clock()
print "%s" % (t1 - t)

