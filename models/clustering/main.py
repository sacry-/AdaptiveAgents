import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature
from copy import deepcopy
import time

from trees import Tree, clustered_trees, merge_trees
from clustering import titles_to_indexed_dict, vector_to_cluster
from clustering import closest_distance, reduce_clusters
from clustering import filter_dummies_dict

'''
Vector = [(lemma, weight)]
'''


def diff():
  return "%3.1f" % ((time.time() - diff.t__))

diff.t__ = time.time()

category = "biology"
filter_ = "biolog"
pattern = "%s*%s*" % (category, filter_) # using only docs with biolog in title
rfeature = RFeature()

print "[1] [%s] fetch data.." % diff()
vectors = filter_dummies_dict(dict(rfeature.take_by_pattern(pattern, 300))) # {title : Vector}
# clusters = vector_to_cluster(vectors) # no dummies, ..

indexed_titles = titles_to_indexed_dict(vectors.keys()) # { title : unique_id }
cluster_trees = clustered_trees(indexed_titles) # [Tree]

print "[2] [%s] start clustering.." % diff()
while len(cluster_trees) > 1:
  c1, c2, merged_set, distance = closest_distance(cluster_trees, vectors, diff)
  clusters = reduce_clusters(cluster_trees, c1, c2, merged_set, distance, vectors, diff)
print "[4] [%s] finished clustering..." % diff()

t = cluster_trees[0]
# t.show() # uncomment to show tree
jsonstr = t.to_json()
fname = "tree"
t.save2file(fname+".txt")
with open(fname+".json", "w+") as f:
    f.write(jsonstr)
    f.close()
print "[5] [%s] Saved tree into %s.txt and %s.json. Read it with from_jsom(...)" % (diff(), fname,fname)


