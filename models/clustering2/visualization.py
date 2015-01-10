#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import os

from clustering import clustering_algorithm
import centroidation
import distance
from distance import INF

def base_graph(_name):
  G=pgv.AGraph(name=_name)
  G.node_attr['shape']='ellipse'
  G.node_attr['fixedsize']='true'
  G.node_attr['fontsize']='6'
  G.node_attr['style']='filled'
  G.graph_attr['size'] = '25!'
  G.graph_attr['ratio']='1.0'
  G.edge_attr['style']='setlinewidth(0.5)'
  G.edge_attr['fontsize']='5'
  return G

def to_disc(G):
  graphname = "%s.dot" % G.name
  filename = "%s.png" % G.name
  G.write(graphname)
  # prog=[’neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]
  G.draw(filename,prog='circo')
  os.system("./bak.sh")
  print("Finished. Output in %s and %s." % (graphname, filename))

# [Cluster] -> {Title: (Cluster, Centroid)}
def prepare_visualization(clusters):
  return dict( (c.name(), (c, centroidation.cluster_centroid_vector(c)) ) for c in clusters )

def dist_to_string(d):
    if d == INF:
        return u"∞"
    else:
        return str(d*100).split('.')[0]

if __name__ == '__main__':
  import warnings
  import pygraphviz as pgv

  warnings.simplefilter('ignore', RuntimeWarning)

  name = "wikigraph"
  G = base_graph(name)
  clusters = clustering_algorithm(n=10, iterations = 10, verbose=False)
  ds = prepare_visualization(clusters)
    
  distances = []
  for title1,(c1, cent1) in ds.iteritems():
    for title2, (c2, cent2) in ds.iteritems():
      # add_edge
      dist = distance.cluster_distance(c1, c2)
      G.add_edge(title1, title2 ,dist)
      G.get_edge(title1, title2).attr['label'] = dist_to_string(dist)
      distances.append( (dist, title1, title2) ) 

  # show a few sample distances
  import random
  random.shuffle(distances)
  for d, t1, t2 in distances[:8]:
    print ("%s :: %s <-> %s" % (d, t1, t2))

  to_disc(G)
  






