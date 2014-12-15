import time
import math
from rediss import RPos, RIdf
from io_utils import load_json

rpos = RPos()
ridf = RIdf()

n = 0
t__ = time.clock()
def diff():
  return "%s" % ((time.clock() - t__)) 


def count_occurrences(w, cat_titles_pos):
  def f(trpl):
    if trpl[2].has_key(w):
      return 1
    return 0
  return sum(map(f, cat_titles_pos))

def do_category():

  print "[1] %s - loading titles" % (diff())

  cat_titles = load_json("categories", "all_cats_3000")

  n_docs = sum(len(v) for k,v in cat_titles.iteritems())

  print "[2] %s - loading pos tags, n_docs = %s" % (diff(), n_docs)

  cat_titles_pos = list( (cat, t, rpos.value_by_title(cat,t)) for cat, ts in cat_titles.iteritems() for t in ts)

  print "[3] %s - extractings words" % diff()

  def calc_idf(w):
    n = count_occurrences(w, cat_titles_pos)
    try:
      return (w, math.log(n_docs / float(n)))
    except ZeroDivisionError:
      return (w, 0)
  
  words = []
  for c_t_p in cat_titles_pos:
    words += c_t_p[2].keys()
  words = set(words)

  print "[4] %s - calculating idfs, n_words = %s" % (diff(), len(words))

  words_idfs = dict(map(calc_idf, words))

  print "[5] %s - saving idfs" % diff()

  ridf.puts("all", words_idfs)

  print "[6] %s - method finisheed" % (diff())


do_category()



