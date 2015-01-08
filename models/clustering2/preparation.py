from Levenshtein import ratio
from cluster_utils import *

class Cluster():
  # Cluster({title, Vector})
  def __init__(self, elems):
    self.elems = elems

  # e :: (Title, Vector)
  def add_elem(self, e):
    return Cluster(dict(self.elems.items() + [e]))

  def vectors(self):
    return self.elems.values()

# filter_dummies_dict :: Dict(Title, Vector) -> Dict(Title, Vector)
def filter_dummies_dict(d):
  return dict((t, filter_dummies(v)) for t,v in d.iteritems() if filter_dummies(v))

def filter_dummies(vector):
  return filter(lambda t: t[0] != "dummy", vector)

def find_closest(vector, lexicon):
  w = fst(vector[0]) # first word in vector
  best_rat = -1
  best_lex = ""
  for lex in lexicon:
    rat = ratio(str(w),str(lex))
    if rat > best_rat:
      best_rat = rat
      best_lex = lex
  return best_lex

def get_lexicon(n):
  import os, sys, json
  p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
  sys.path.insert(0, p)

  from rediss import RIdf
  rif = RIdf()
  heuristic = lambda x: x[1] > 2
  non_junk_words = filter(heuristic, list(rif.key_value_by_pattern("*")))
  return map(fst, sorted(non_junk_words, key=snd)[:n])

def initial_clusters(master, n):
  from itertools import repeat
  lexicon = get_lexicon(n)
  clusters = dict((lex, Cluster({})) for lex in lexicon)
  for title, vector in master.iteritems():
    word = find_closest(vector, lexicon)
    # print "%s -> %s" % (title, word)
    clusters[word] = clusters[word].add_elem( (title,vector) )
  print "clusters initiated!"
  return clusters.values() # [{title : Vector}] == [Cluster]


if __name__ == "__main__":
  initial_clusters({}, 50)


