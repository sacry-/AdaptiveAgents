import os, sys, json
p = "%s/../../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature

from Levenshtein import ratio
from itertools import groupby
from math import sqrt
from math import log
from math import fsum
from distance import Cluster

VLEN = 25
MIN_SUM_OF_WEIGHTS = 500
LIMIT_LOG = MIN_SUM_OF_WEIGHTS*log(MIN_SUM_OF_WEIGHTS)
LIMIT_SQRT = MIN_SUM_OF_WEIGHTS*sqrt(MIN_SUM_OF_WEIGHTS)

def concatMap(f, ls):
    return sum(map(f,ls),[])

def prints(ls):
  for x in ls:
    print x

def fst(tpl):
  return tpl[0]

def snd(tpl):
  return tpl[1]

# given a Vector of arbitrary length, truncate or extends it to 25 elements
def fix_length(ls):
  diff = len(ls) - VLEN
  if diff < 0:
    return ls + [("dummy",0) for i in xrange(diff)]
  return ls[:VLEN]

# relevance takes two weighted words and returns the higher weighted word with the modified weight
# the resulting weight is higher, the closer the words are to each other
# relevance :: ((Word, Weight),(Word, Weight)) -> (Word, Weight)
def relevance(tpl, debug=False):
    a, b = tpl
    w1, wt1 = a
    w2, wt2 = b
    weight = ratio(str(w1),str(w2))*log(1+wt1+wt2) # sqrt(wt1*wt2)
    res = (w1, weight) if wt1 > wt2 else (w2, weight)
    if debug and weight > 5:
        print "::::::::\n%s -> %s\n%s -> %s\nbecame %s" % (w1,wt1,w2,wt2,res)
    return res

# collapse a 625 length vector to a 25 length representative vector
# collapse :: [(Word, Weight)] -> [(Word, Weight)]
def collapse(ls, debug=False):
  sls = sorted(ls, key=fst)
  
  def f(ls):
    ls = map(snd,ls)
    return fsum(ls)
  
  groups = list((k, f(g))for k, g in groupby(sls, key=fst))
  sgroups = sorted(groups, key=snd, reverse=True)
  dist_v = fix_length(sgroups)
  
  if debug:
    print "Merged:"
    prints(dist_v[:5])
  return dist_v


def compare_all(v,  debug=False):
    # build pairs to compare each word from v1 with every word from v2
    ps = [(a,b) for a in v for b in v] # len(ps) ~= 22.500
    
    relevances = map(lambda x:relevance(x,debug=False), ps)
    #print "First:"
    #prints(v1[:5])
    #print "Second:"
    #prints(v2[:5])
    distance_vector = collapse(relevances, debug=False)
    return distance_vector

# Vector -> Vector
def reduce_duplicates(weighted_words):
    new_vector = {}
    for w, wt in weighted_words:
        if new_vector.has_key(w):
            new_vector[w] += wt
        else:
            new_vector[w] = wt
    return list(new_vector.iteritems())
    # raise "sum weights of identical words, or not?"

# Cluster -> Vector
def cluster_centroid_vector(cluster):
    all_weighted_words = reduce_duplicates(sum(cluster.vectors(), []))
    limit = LIMIT_SQRT
    vector_of_compared = []
    accu = 0
    sorted_all_weighted_words = sorted(all_weighted_words, key=snd, reverse=True)
    for w, wt in sorted_all_weighted_words:
        accu += wt
        if accu > limit:
            break
        vector_of_compared.append( (w,wt) )
    return compare_all(vector_of_compared)


if __name__ == '__main__':
    rfeature = RFeature()
    features = dict(rfeature.key_value_by_pattern("*rn"))
    cluster = Cluster(features)
    centroid = cluster_centroid_vector(cluster)
    tests = sorted(concatMap(lambda v:v[:5], cluster.vectors()), key=snd)
    def inCentroid(x):
        return fst(x) in map(fst,centroid)

    print "Sample:"
    prints(tests)
    print "Sample in Centroid:"
    prints(filter(inCentroid, tests))
    print "Centroid:"
    prints(centroid)
