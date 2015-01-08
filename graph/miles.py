#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
import fileinput
import math
import re
import gzip 


REDS = ["FF0000", "B80000", "810000"]

def add_node(G, city):
  G.add_node(city)
  return G.get_node(city)

def assign_attributes_to_node(n, coordpop, city):
  # assign positions, scale to be something reasonable in points
  # assign node size, in sqrt of 1,000,000's of people 
  (coord,pop)=coordpop.split("]")
  (y,x)=coord.split(",")
  n.attr['pos']="%f,%f)"%(-(float(x)-7000)/10.0,(float(y)-2000)/10.0)
  d=math.sqrt(float(pop)/1000000.0)

  n.attr['height']="%s"%(d/1.5)
  n.attr['width']="%s"%(d/1.5)
  # assign node color
  n.attr['fillcolor']="#%s" % REDS[int(d*256) % 3]
  n.attr['label']= city.split(",")[0].strip()

  return n

def create_edge(G, city1, city2, distance):
  G.add_edge(city1, city2, distance)
  e = G.get_edge(city1, city2)
  e.attr['label'] = str(distance).split(".")[0]

def styled_graph():
  G=pgv.AGraph(name='miles_dat')
  G.node_attr['shape']='circle'
  G.node_attr['fixedsize']='true'
  G.node_attr['fontsize']='8'
  G.node_attr['style']='filled'
  # G.graph_attr['outputorder']='edgesfirst'
  G.graph_attr['size'] = '25!'
  G.graph_attr['label']="miles_dat"
  G.graph_attr['ratio']='1.0'
  G.edge_attr['style']='setlinewidth(0.5)'
  G.edge_attr['fontsize']='6'
  return G

def miles_graph():
  G = styled_graph()

  cities=[]
  for line in gzip.open("miles_dat.txt.gz",'rt'):
    if line.startswith("*"): # skip comments
      continue
    numfind=re.compile("^\d+") 

    if numfind.match(line):
      dist=line.split()
      for d in dist:
        if float(d) < 500:
          create_edge(G, city, cities[i], float(d))
        i=i+1
    else:
      i=1
      (city, coordpop)=line.split("[")
      cities.insert(0, city)
      n = add_node(G, city)
      n = assign_attributes_to_node(n, coordpop, city)

  return G

def new_graph():
  G=pgv.AGraph(name='graph8')
  for line in open('graph8.graph', 'r'):
    (c1, c2, w) = line.strip().split(",")

    create_edge(G, c1, c2, int(w))

  return G
  
if __name__ == '__main__':
  import warnings
  import pygraphviz as pgv

  warnings.simplefilter('ignore', RuntimeWarning)

  G = new_graph()
  G.write("miles.dot")
  # prog=[’neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]
  G.draw("miles.png",prog='circo')
  print("Finished!")









