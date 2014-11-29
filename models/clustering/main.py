import os, sys
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from seed_selection import SeedSelect
import center_adjustment
import refinement
from rediss import RFeature

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


# Seed

k = 9

'''
  [Vector_0,..Vector_k]
'''
k_seeds = select_seed(k, vectors)


# Adjustment

'''
  {_id : set(title)} , 0 = unmatched, 1-9 = seeds
'''
seed_to_title= {}
for _id in range(0, k+1):
  seed_to_title[_id] = set([])

n_times = 10
for _ in range(0, n_times):

  for title, vector in vectors.iteritems(): 
    '''
      assigns vector to k_seeds,
      assigns title to seed_to_title for mapping k_seed indices to titles,
      returns k_seeds cluster id, can be 0 for unmatched or else 1-9 for real seeds,
    '''
    _id = assign(title, vector, k_seeds, seed_to_title)
    if _id:
      '''
        remove title from all other seeds except from _id
      '''
      remove(title, seed_to_title, _id)
      '''
        adjusts the centroid of the current id with vector
      '''
      adjust(vector, _id, k_seeds)


# Refinement

clusters = k_seeds
n_times = 10
for _ in range(0, n_times):
  '''
    how?
  '''
  splitted_centroids = split(clusters)
  '''
    joins the splitted clusters into new clusters,
    heuristics 1: join those splitted centroids with at least p common keywords
    heuristic 2: join those where the cosine of two centroids is > constant c
    heuristic 3: join those where the cosine of two centroids is > c times variance of the parents
    heuristic 4: greedy join closest pair of clusters (naive)
  '''
  clusters = join(splitted_centroids)










