# coding: utf-8
from __future__ import division

INF = float("inf")

def vector_to_cluster(vectors):

  def filter_dummies(vector):
    return filter(lambda t: t[0] != "dummy", vector)

  clusters = dict((title, filter_dummies(vector)) for title, vector in vectors)
  return clusters


def titles_to_indexed_dict(titles):
  return dict((e, idx) for idx, e in enumerate(titles))

def calculate_distance(v1, v2):
  try:
    s1 = set(zip(*v1)[0])
    s2 = set(zip(*v2)[0])
    rset = s1.intersection(s2)
    return (1 / len(rset), rset)
  except:
    return (INF, set([]))

memo = {}
def distance(c1, c2):
  global memo
  t1, v1 = c1
  t2, v2 = c2
  key = "%s%s" % (t1, t2)
  if not key in memo:
    memo[key] = calculate_distance(v1, v2)
  return memo[key]

def closest_distance(cluster_hash):
  pairs = []
  m = INF
  min_pair = (None, None, None)
  for c1 in cluster_hash.iteritems():
    for c2 in cluster_hash.iteritems():
      if c1 != c2:
        dist, rset = distance(c1, c2)
        if dist <= m:
          m = dist 
          min_pair = (c1, c2, rset)
  return min_pair

tick = 0
def reduce_clusters(clusters, c1, c2, merged_cluster):
  global tick
  n1, n2 = c1[0], c2[0]
  clusters["new_cluster_%s" % tick] = merged_cluster
  clusters.pop(n1)
  clusters.pop(n2)
  print "cluster-size: %s - pair(%s, %s)" % (len(clusters), n1, n2)
  tick = tick + 1
  return clusters



