from preparation import Cluster
from cluster_utils import *

INF = float("inf")

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
def calculate_distance(v1, v2):
  try:
    rset = v1.intersection(v2)
    #print "%s %s %s" % (len(v1), len(v2), len(rset))
    return (1 / len(rset), rset)
  except ZeroDivisionError:
    return (INF, set([]))



