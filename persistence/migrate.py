import time
from rediss import RPos, RFeature
from multiprocessing import Pool

import os, sys
p = "%s/../love_the_data" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from statistics import Frequencies


# brew/apt-get? install redis
# sudo pip install redis-py
# sudo pip install redisdl
# DONE! :-)

rpos = RPos()
rfeature = RFeature()

n = 0
categories = ["biology", "physics", "chemistry"]
t__ = time.clock()
def diff():
    return "%s" % ((time.clock() - t__)) 


def do_category(category):
    print "[1] %s %s - Calculating idfs for category %s" % (diff(), category, category)
    
    frequencies = Frequencies(rpos, category)
    
    print "[1] %s %s - idfs for %s articles calculated" % (diff(), category, len(frequencies.titles))
    print "[1] %s %s - Inserting idfs into %s" % (diff(), category, rfeature)
    
    curr = pre = len(list(rfeature.keys(category + "*")))
    i = 1
    pipe = rfeature.rs.pipeline(transaction=False)
    for f in frequencies.freqs.values():
        for t in f.words():
            i += 1
            if i % 5000 == 0:
                pipe.execute() # Section Pipeline: https://pypi.python.org/pypi/redis/
                pipe = rfeature.rs.pipeline(transaction=False)
                curr = len(list(rfeature.keys(category + "*")))
                print "[2] %s %s - i = %s" % (diff(),category,  i)
                print "[2] %s %s - added %s terms into RFeature, %s total" % (diff(), category, curr - pre, curr)
                pre = curr
            _idf = frequencies.idf(t)
            key = rfeature.key_name(category, t)
            pipe.set(key, _idf)
    print "[2] %s %s - Finished all %s terms in %s" % (diff(), category, len(list(rfeature.keys(category + "*"))))
    return "fin"



print "[0] %s - Started migrate script for inverse document frequencies" % diff()

futures = map(do_category, categories)

print "[0] Finished migration: %s terms over %s categories" % (diff(), n)
