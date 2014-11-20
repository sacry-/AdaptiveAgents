import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature

rf = RFeature()

def take_while(f, collection):
  for elem in collection:
    if not f(elem):
      return
    yield elem

h = sorted(rf.key_value_by_pattern("biology-idf:*"), key=lambda t: -t[1])
over_nine = list(filter(lambda x: x[1] < 3, h))

# 9.72142596194803
print over_nine
print "%s-%s=%s" % (len(h), len(over_nine), len(h) - len(over_nine))

#for elem in take_while2(lambda x: x[1] > 9.5, over_nine):
#  print elem