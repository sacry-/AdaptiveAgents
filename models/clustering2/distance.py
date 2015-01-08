

class Cluster():

  def __init__(self, elems):
    self.elems = elems

  def vectors(self):
    return self.elems.values()

  def key(self):
    raise "Cluster.key not implemented"

# Set(Word) -> Set(Word) -> (Double, Set(Word))
def calculate_distance(v1, v2):
  try:
    rset = v1.intersection(v2)
    #print "%s %s %s" % (len(v1), len(v2), len(rset))
    return (1 / len(rset), rset)
  except ZeroDivisionError:
    return (INF, set([]))

# distance :: Cluster -> Cluster -> Dict(Title, Vector) -> Diff -> Double
memo = {}
def distance(c1, c2, vectors, diff):
  global memo
  raise "key calculation missing!"
  key = calculate_key(c1, c2)
  if not key in memo:
    v1 = get_words(c1, vectors)
    v2 = get_words(c2, vectors)
    memo[key] = calculate_distance(v1, v2)
  return memo[key]

def get_words(cluster):
  for v in cluster:
    for word, _ in v.values():
      yield word

# Cluster -> Cluster -> String
def calculate_key(c1, c2):
  return "%s#%s" % (c1, c2)



