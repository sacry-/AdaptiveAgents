#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

from clustering import clustering_algorithm
import centroidation
import distance

def base_graph(_name):
  G=pgv.AGraph(name=_name)
  G.node_attr['shape']='circle'
  G.node_attr['fixedsize']='true'
  G.node_attr['fontsize']='8'
  G.node_attr['style']='filled'
  G.graph_attr['size'] = '25!'
  G.graph_attr['ratio']='1.0'
  G.edge_attr['style']='setlinewidth(0.5)'
  G.edge_attr['fontsize']='6'
  return G

def to_disc(G):
  G.write("%s.dot" % G.name)
  # prog=[’neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]
  G.draw("%s.png" % G.name,prog='circo')
  print("Finished!")

# [Cluster] -> {Title: (Cluster, Centroid)}
def prepare_visualization(clusters):
  return dict( (c.name(), (c, centroidation.cluster_centroid_vector(c)) ) for c in clusters )

if __name__ == '__main__':
  import warnings
  import pygraphviz as pgv

  warnings.simplefilter('ignore', RuntimeWarning)

  name = "clustering_graph"
  G = base_graph(name)

  clusters = clustering_algorithm(25, iter_count = 15, iter_print=True)
  ds = prepare_visualization(clusters)

  for title1,(c1, cent1) in ds.iteritems():
    for title2, (c2, cent2) in ds.iteritems():
      # add_edge
      dist = distance.cluster_distance(c1, c2)
      print ("%s :: %s <-> %s" % (dist, title1, title2))



  # to_disc(G)
  






