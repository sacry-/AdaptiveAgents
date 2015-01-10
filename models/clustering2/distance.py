from preparation import Cluster
from cluster_utils import *

INF = float("inf")
from math import fsum

# [Vector] -> {title : Vector} -> [Clusters]
def assign_nodes_to_centroids(centroids, master):
  clusters = dict((vector_to_key(c), Cluster({})) for c in centroids)
  for title, vector in master.iteritems():
    centroid = find_closest(vector, centroids)
    centroid_key = vector_to_key(centroid)
    clusters[centroid_key] = clusters[centroid_key].add_elem( (title, vector) )
    # print "%s += %s" % (centroid_key, title)
  return clusters.values()

def vector_to_word_set(vec):
  return set(map(fst,vec))

# Vector -> Double
def vector_to_key(vector):
  return sum(map(snd,vector))

def find_closest(vector, centroids):
  v_words = vector_to_word_set(vector)
  f = lambda cent: calculate_distance(v_words, vector_to_word_set(cent))
  return min(centroids, key=f)

# Set(Word) -> Set(Word) -> (Double, Set(Word))
# used in clustering
def calculate_distance(v1, v2):
  try:
    rset = v1.intersection(v2)
    #print "%s %s %s" % (len(v1), len(v2), len(rset))
    return (float(1) / float(len(rset)), rset)
  except ZeroDivisionError:
    return (INF, set([]))


# [Weight] -> Weight
def collapse_weights(wts):
    return fold(lambda x,y:x*y,wts,1)

# Dict(Word, Weight) -> Dict(Word, Weight) -> (Double, Set(Word))
def calculate_weighted_distance(v1, v2):
  try:
    keys = set(v1.keys())
    keys = keys.intersection(set(v2.keys()))
    zip_dict = {}
    for k in keys:
      zip_dict[k] = collapse_weights([d[k] for d in [v1,v2]])
    weight = float(fsum(zip_dict.values()))
    # print "%s %s %s" % (len(v1), len(v2), len(rset))
    return (float(1) / weight, keys)
  except ZeroDivisionError:
    return (INF, set([]))

def get_weighted_words(cluster):
  words_ = dict()
  for v in cluster.vectors():
    for w,wt in v:
      if words_.has_key(w):
        words_[w] += wt
      else:
        words_[w] = wt
  return words_

# used in visualization
def cluster_distance(c1, c2):
  ww1 = get_weighted_words(c1)
  ww2 = get_weighted_words(c2)
  dist, inters = calculate_weighted_distance(ww1,ww2)
  # print len(inters)
  return dist
  
def fold(f, l, a):
  """
  f: the function to apply
  l: the list to fold
  a: the accumulator, who is also the 'zero' on the first call
  """ 
  return a if(len(l) == 0) else fold(f, l[1:], f(a, l[0]))


