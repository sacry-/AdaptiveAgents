import os, sys
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from seed_selection import SeedSelect
import center_adjustment
import refinement
from rediss import RFeature
from copy import deepcopy

''' types

  Vector = [(lemma, weight)]

'''

# Data

category = "biology"
rfeature = RFeature()

''' 
  {title : Vector}
'''
vectors = dict(rfeature.key_value_by_pattern("%s*" % category))
clusters = deepcopy(vectors)
tree = 

while len(clusters.values()) > 1:
  c1, c2 = closest_distance(clusters)










