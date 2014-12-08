# coding: utf-8
from __future__ import division
from trees import clustered_trees, merge_trees
from treelib import Tree

INF = float("inf")

def fst(tpl):
    return tpl[0]
    
# filter_dummies_dict :: Dict(Title, Vector) -> Dict(Title, Vector)
def filter_dummies_dict(d):
    return dict((t, filter_dummies(v)) for t,v in d.iteritems())

def filter_dummies(vector):
  return filter(lambda t: t[0] != "dummy", vector)

def vector_to_cluster(vectors):

  clusters = dict((title, filter_dummies(vector)) for title, vector in vectors)
  return clusters

def titles_to_indexed_dict(titles):
  return dict((e, idx) for idx, e in enumerate(titles))

# Set(Word) -> Set(Word) -> (Double, Set(Word))
def calculate_distance(v1, v2):
  try:
    rset = s1.intersection(s2)
    return (1 / len(rset), rset)
  except:
    return (INF, set([]))

# distance :: Tree -> Tree -> Dict(Title, Vector) -> Double
memo = {}
def distance(c1, c2, vectors):
  global memo
  key = calculate_key(c1, c2)
  v1 = get_words(c1, vectors)
  v2 = get_words(c2, vectors)
  if not key in memo:
    memo[key] = calculate_distance(v1, v2)
  return memo[key]

# Tree -> Tree -> String
def calculate_key(c1, c2):
    return "%s#%s" % (c1.root, c2.root)

# Tree -> Dict(Title, Vector) -> Set(Word)
def get_words(c1, vectors):
    #print "Get_words:"
    #c1.show()
    words = set([])
    for node in c1.leaves(c1.root):
        for word in vectors[c1[node].tag]:
            words.add(word)
    return words

# clostest_distance :: [Tree] -> Dict(Title, Vector) -> (Tree, Tree, Double)
def closest_distance(cluster_trees, vectors):
  pairs = []
  m = INF
  min_pair = (None, None, None)
  for c1 in cluster_trees:
    for c2 in cluster_trees:
      if c1 != c2:
        dist, rset = distance(c1, c2, vectors)
        if dist <= m:
          m = dist 
          min_pair = (c1, c2, rset)
  return min_pair

# reduce_clusters :: [Tree] -> Tree -> Tree -> Set(Word) -> [Tree]
tick = 1 # start from 1 to avoid collision in ids
def reduce_clusters(cluster_trees, c1, c2, intersect_words):
  global tick
  # n1, n2 = c1[0], c2[0]
  # clusters["new_cluster_%s" % tick] = merged_cluster
  # clusters.pop(n1)
  # clusters.pop(n2)
  cluster_trees.remove(c1)
  cluster_trees.remove(c2)
  newtree, name = merge_trees(c1,c2, tick)
  cluster_trees.append(newtree)
  c1_name = c1.get_node(c1.root).tag
  c2_name = c2.get_node(c2.root).tag
  print "cluster-size: %s - [%s] %s <- %s + %s" % (len(cluster_trees),len(intersect_words), name, c1_name, c2_name)
  tick = tick + 1
  return cluster_trees



