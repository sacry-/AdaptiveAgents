import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature
from copy import deepcopy

from trees import Tree, clustered_trees, merge_trees
from clustering import titles_to_indexed_dict, vector_to_cluster
from clustering import closest_distance, reduce_clusters

'''
Vector = [(lemma, weight)]
'''

category = "physics"
pattern = "%s*" % category
rfeature = RFeature()

print "[1] fetch data.."
vectors = rfeature.take_by_pattern(pattern, 1000) # {title : Vector}
clusters = vector_to_cluster(vectors) # no dummies, ..

titles = titles_to_indexed_dict(clusters.keys()) # { title : unique_id }
cluster_trees = clustered_trees(titles)

print "[2] start clustering.."
while len(clusters) > 1:
  c1, c2, merged_set = closest_distance(clusters)
  clusters = reduce_clusters(clusters, c1, c2, merged_set)
  cluster_trees = merge_trees(cluster_trees, merged_set)
print "[3] finished clustering..."

print list(clusters.iteritems()).pop()

