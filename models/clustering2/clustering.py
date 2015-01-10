import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)


from rediss import RIdf
from rediss import RFeature

import preparation
import distance
import centroidation
from cluster_utils import *


def clustering_algorithm(n=50, iterations=15):
  print "n = %s and iterations = %s" % (n, iterations)
  # {title : Vector}
  feature_3000 = dict(RFeature().key_value_by_pattern("*"))
  master = preparation.filter_dummies_dict(feature_3000)

  # clusters :: [Cluster]
  data = RIdf().key_value_by_pattern("*")
  clusters = preparation.initial_clusters(master, n, data)

  for i in range(0, iterations):
    print "%s iteration" % (i + 1)
    print "Cluster sizes: %s" % cluster_sizes(clusters)
    centroids = map(centroidation.cluster_centroid_vector, clusters)
    clusters = distance.assign_nodes_to_centroids(centroids, master)

  print "Cluster sizes: %s" % cluster_sizes(clusters)
  return clusters

if __name__ == "__main__":
  clustering_algorithm(35, 50)


'''
Cluster sizes after 50th iteration:
[7, 9, 10, 12, 14, 15, 15, 16, 18, 18, 19, 20, 22, 23, 23, 23, 26, 
26, 32, 32, 33, 33, 35, 36, 36, 36, 36, 39, 41, 43, 46, 49, 53, 56, 
60, 60, 61, 65, 66, 79, 88, 112, 115, 118, 139, 177, 198, 225, 227, 227]
'''


