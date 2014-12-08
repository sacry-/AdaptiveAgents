import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature
from copy import deepcopy

from trees import Tree, clustered_trees, merge_trees
from clustering import titles_to_indexed_dict, vector_to_cluster
from clustering import closest_distance, merge_cluster, reduce_clusters

'''
Vector = [(lemma, weight)]
'''

category = "biology"
pattern = "%s*" % category
rfeature = RFeature()

print "[1] fetch data.."
vectors = rfeature.take_by_pattern(pattern, 500) # {title : Vector}
clusters = vector_to_cluster(vectors) # no dummies, ..

titles = titles_to_indexed_dict(clusters.keys()) # { title : unique_id }
cluster_trees = clustered_trees(titles)

print "[2] start clustering.."
while len(clusters) > 1:
  c1, c2 = closest_distance(clusters)
  merged_cluster = merge_cluster(c1, c2)
  clusters = reduce_clusters(clusters, c1, c2, merged_cluster)
  cluster_trees = merge_trees(cluster_trees, merged_cluster)
print "[3] finished clustering..."


def save_result(cluster_hash):
  from utils import persistence_path
  from io_utils import save
  json_data = json.dumps(cluster_hash, indent=2, sort_keys=True).encode('utf8')
  save("%s/%s" % (persistence_path(), "cluster.json"), json_data)

save_result(clusters)


