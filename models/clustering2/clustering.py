import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature

import pprint
import preparation
import distance
import centroidation
from cluster_utils import *

'''
type Cluster( {title: Vector} )
'''

def clustering_algorithm(n=50, iter_count=10, iter_print=False):
  rfeature = RFeature()
  # {title : Vector}
  feature_3000 = dict(rfeature.key_value_by_pattern("*"))
  master = preparation.filter_dummies_dict(feature_3000)
  # clusters :: [Cluster]
  clusters = preparation.initial_clusters(master, n)

  for i in range(0, iter_count):
    if iter_print:
      # print "Cluster sizes: %s" % cluster_sizes(clusters)
      print "%s th iteration:" % (i + 1)
    centroids = map(centroidation.cluster_centroid_vector, clusters)
    clusters = distance.assign_nodes_to_centroids(centroids, master)

  print "Cluster sizes: %s" % cluster_sizes(clusters)
  return clusters





