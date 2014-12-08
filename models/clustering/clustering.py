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
    rset = v1.intersection(v2)
    #print "%s %s %s" % (len(v1), len(v2), len(rset))
    return (1 / len(rset), rset)
  except ZeroDivisionError:
    return (INF, set([]))

# distance :: Tree -> Tree -> Dict(Title, Vector) -> Diff -> Double
memo = {}
def distance(c1, c2, vectors, diff):
  global memo
  key = calculate_key(c1, c2)
  v1 = get_words(c1, vectors)
  v2 = get_words(c2, vectors)
  if not key in memo:
    memo[key] = calculate_distance(v1, v2)
  return memo[key]

# Tree -> Tree -> String
def calculate_key(c1, c2):
    return "%s#%s" % (tree_key(c1), tree_key(c2))

def tree_key(c1):
    return "%s" % (c1.root)

# Tree -> Dict(Title, Vector) -> Set(Word)
def get_words(c1, vectors):
    words = set([])
    for node in c1.leaves(c1.root):
        for tpl in vectors[c1[node].tag]:
            words.add(tpl[0])
    return words

# clostest_distance :: [Tree] -> Dict(Title, Vector) -> Diff -> (Tree, Tree, Double, Set(Word))
def closest_distance(cluster_trees, vectors, diff):
  pairs = []
  m = INF
  min_pair = (None, None, None)
  count = 0
  count2 = 0
  pairs = list((c1, c2, vectors) for c1 in cluster_trees for c2 in cluster_trees if c1 != c2)
  # each iteration is fast, but the number of iterations is the problem
  
  pairs_with_dist = p.map(par_distance, pairs)                    # <- bottleneck!
  c1, c2, dist, rset = min(pairs_with_dist, key=lambda x:x[2])
  # print "[3] [%s] distances: %s iterations. %s %s" % (diff(), len(pairs), c1, c2)
  return (c1, c2, rset, dist)

def par_distance(tpl):
  c1, c2, vectors = tpl
  v1 = get_words(c1, vectors)
  v2 = get_words(c2, vectors)
  dist, rset = calculate_distance(v1, v2)
  return c1, c2, dist, rset

from multiprocessing import Pool, cpu_count # import has to be done AFTER the par_mapped function par_distance

p = Pool(cpu_count()-1)
print "Cores: %s " % cpu_count()

# reduce_clusters :: [Tree] -> Tree -> Tree -> Set(Word) -> Double -> Vectors -> Diff -> [Tree]
tick = 1 # start from 1 to avoid collision in ids
def reduce_clusters(cluster_trees, c1, c2, intersect_words, dist, vectors, diff):
  global tick
  k1 = tree_key(c1)
  k2 = tree_key(c2)
  cluster_trees = list(t for t in cluster_trees if tree_key(t) != k1 and tree_key(t) != k2)
  newtree, name = merge_trees(c1, c2, tick)
  cluster_trees.append(newtree)
  c1_name = c1.get_node(c1.root).tag
  c2_name = c2.get_node(c2.root).tag
  print "[3] [%s] cluster-size: %s - [%s, %1.3f] %s <- %s + %s" % (diff(), len(cluster_trees),len(intersect_words), dist, name, c1_name, c2_name)
  tick = tick + 1
  return cluster_trees



