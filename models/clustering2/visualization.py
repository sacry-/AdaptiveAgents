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

def base_graph(_name,n,iterations):
  G=pgv.AGraph(name=_name)
  
  # http://www.graphviz.org/doc/info/attrs.html
  # http://www.graphviz.org/content/faq

  G.graph_attr['label']="%s - n=%s, it=%s" % (_name, n, iterations)
  G.graph_attr['size'] = str(n*3)
  G.graph_attr['splines'] = "none"
  # G.graph_attr['outputorder']='nodesfirst'

  G.node_attr['shape']='ellipse'
  G.node_attr['style']='filled'
  
  G.edge_attr['style']='setlinewidth(0.2)'
  G.edge_attr['font']='Arial'
  
  return G

def to_disc(G):
  graphname = "%s.dot" % G.name
  filename = "%s.png" % G.name
  G.write(graphname)
  # prog=[’neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]
  G.draw(filename,prog='fdp')
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
  # drawing complexity seems to increase quadratic/cubic with N
  # ~1min for n = 32
  n=35
  iterations=25
  G = base_graph(name,n,iterations)
  clusters = clustering_algorithm(n=n, iterations=iterations, verbose=True)
  ds = prepare_visualization(clusters)
    
  distances = []
  for title1,(c1, cent1) in ds.iteritems():
    for title2, (c2, cent2) in ds.iteritems():
      # add_edge
      dist = distance.cluster_distance(c1, c2)
      d = dist_to_string(dist)
      if dist < 0.5:
        G.add_edge(title1, title2, weight=-dist) # weight is negated distance
        if dist < 0.1:
          G.get_edge(title1, title2).attr['label'] = d
        distances.append( (dist, title1, title2) )

  if True:
    print ("few sample distances")
    import random
    random.shuffle(distances)
    for d, t1, t2 in distances[:8]:
      print (d)

  to_disc(G)
  





