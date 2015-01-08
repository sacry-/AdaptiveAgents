import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature

import preparation
import distance
import centroidation


'''
type Cluster = {title: Vector}
'''


rfeature = RFeature()

# {title : Vector}
feature_3000 = dict(rfeature.key_value_by_pattern("*"))
master_cluster = preparation.filter_dummies_dict(feature_3000)

# { title : unique_id }
indexed_titles = titles_to_indexed_dict(vectors.keys())



