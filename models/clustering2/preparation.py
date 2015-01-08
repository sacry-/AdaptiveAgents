

# filter_dummies_dict :: Dict(Title, Vector) -> Dict(Title, Vector)
def filter_dummies_dict(d):
  return dict((t, filter_dummies(v)) for t,v in d.iteritems() if filter_dummies(v))

def filter_dummies(vector):
  return filter(lambda t: t[0] != "dummy", vector)