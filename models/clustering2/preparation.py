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

  
  def name(self):
    n = 4
    relevant_lemmas = self.relevant_lemmas(n)
    articles = self.some_articles(n)
    return "%s\n\n%s" % (articles, relevant_lemmas)
  
  def some_articles(self,n):
    xs = self.elems.keys()
    return '\n'.join(xs[:n]) if len(xs) > n else "DuMMy"
  
  def relevant_lemmas(self, n):
    def toString(tpl):
      word, weight = tpl
      return "%s(%s)" % (word, weight)
    xs = map(toString,sorted(sum(self.vectors(), []), key=snd))
    return '\n'.join(xs[:n]) if len(xs) > n else "(none)"
    

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
    rat = levenshtein_ratio(w,lex)
    if rat > best_rat:
      best_rat = rat
      best_lex = lex
  return best_lex


def get_non_junk_words(data, bounds=2):
  non_junk_words = filter(lambda x: snd(x) > bounds, list(data))
  return non_junk_words

def lexicon_with_min_and_max_bound(non_junk_words, decr_bound, incr_bound, verbose=True):
  average_word = sum(map(snd, non_junk_words)) / len(non_junk_words)
  min_bound, max_bound = average_word + decr_bound, average_word + incr_bound
  filtered = filter(lambda x: min_bound < snd(x) < max_bound, non_junk_words)
  if verbose:
    print "average word size: %s, mind_bound: %s, max_bound: %s" % (average_word, min_bound, max_bound)
    print "lexicon with min and max bound size: %s" % len(filtered)
  return filtered

def get_lexicon(n, data, verbose=True):
  non_junk_words = get_non_junk_words(data)
  filtered = lexicon_with_min_and_max_bound(non_junk_words, -2.5, -1.5, verbose=verbose)
  lexicon = map(fst, sorted(filtered, key=snd, reverse=True)[:n])
  if verbose:
    print "%s" % ", ".join(lexicon)
  return lexicon

def initial_clusters(master, n, data, verbose=True):
  from itertools import repeat
  lexicon = get_lexicon(n, data, verbose=verbose)
  clusters = dict((lex, Cluster({})) for lex in lexicon)
  for title, vector in master.iteritems():
    word = find_closest(vector, lexicon)
    # print "%s -> %s" % (title, word)
    clusters[word] = clusters[word].add_elem( (title,vector) )
  print "Clusters initiated."
  return clusters.values() # [{title : Vector}] == [Cluster]


if __name__ == "__main__":
  import os, sys, json
  p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
  sys.path.insert(0, p)
  from rediss import RIdf
  data = RIdf().key_value_by_pattern("*")
  initial_clusters({}, 50, data)


