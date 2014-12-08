import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature
from copy import deepcopy

from trees import Tree, clustered_trees, merge_trees
from clustering import titles_to_indexed_dict, vector_to_cluster
from clustering import closest_distance, reduce_clusters
from clustering import filter_dummies_dict

'''
Vector = [(lemma, weight)]
'''

category = "biology"
pattern = "%s*" % category
rfeature = RFeature()

print "[1] fetch data.."
vectors = filter_dummies_dict(dict(rfeature.take_by_pattern(pattern, 500))) # {title : Vector}

# clusters = vector_to_cluster(vectors) # no dummies, ..

indexed_titles = titles_to_indexed_dict(vectors.keys()) # { title : unique_id }
cluster_trees = clustered_trees(indexed_titles) # [Tree]

#for x in cluster_trees:
#    x.show()


print "[2] start clustering.."
while len(cluster_trees) > 1:
  c1, c2, merged_set = closest_distance(cluster_trees, vectors)
  clusters = reduce_clusters(cluster_trees, c1, c2, merged_set)
  # cluster_trees = merge_trees(cluster_trees, merged_set)
print "[3] finished clustering..."

t = cluster_trees[0]
t.show()
jsonstr = t.to_json()
with open("tree.josn", "w+") as f:
    f.write(jsonstr)
    f.close()



