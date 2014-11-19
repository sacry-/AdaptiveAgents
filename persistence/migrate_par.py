import time
from rediss import RPos, RFeature
from multiprocessing import Pool

import os, sys
p = "%s/../love_the_data" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from statistics import Frequencies


# USAGE:
# Open three terminals
# [1]: python migrate_par.py -cat "physics"
# [2]: python migrate_par.py -cat "chemistry"
# [3]: python migrate_par.py -cat "biology"
# each process will occupy a core. close other memory hungy applications, if you don't have more than 4 cores...

rpos = RPos()
rfeature = RFeature()

n = 0
t__ = time.clock()
def diff():
    return "%s" % ((time.clock() - t__)) 


def do_category(category):
    print "[1] %s %s - Calculating idfs for category %s" % (diff(), category, category)
    
    frequencies = Frequencies(rpos, category)
    numArticles = len(frequencies.titles)
    print "[1] %s %s - idfs for %s articles calculated" % (diff(), category, numArticles)
    print "[1] %s %s - Inserting idfs into %s" % (diff(), category, rfeature)
    
    curr = pre = len(list(rfeature.keys(category + "*")))
    i = 1
    j = 0
    pipe = rfeature.rs.pipeline(transaction=False)
    for f in frequencies.freqs.values():
        j += 1
        for t in f.words():
            i += 1
            if i % 5000 == 0:
                pipe.execute() # Section Pipeline: https://pypi.python.org/pypi/redis/
                pipe = rfeature.rs.pipeline(transaction=False)
                curr = len(list(rfeature.keys(category + "*")))
                print "[2] %s %s - processed %s/%s articles, i = %s" % (diff(), category, j, numArticles, i)
                print "[2] %s %s - added %s terms into RFeature, %s total" % (diff(), category, curr - pre, curr)
                pre = curr
            _idf = frequencies.idf(t)
            key = rfeature.key_name(category, t)
            pipe.set(key, _idf)
    print "[2] %s %s - Finished all %s terms in %s" % (diff(), category, len(list(rfeature.keys(category + "*"))))
    return "fin"

import argparse
parser = argparse.ArgumentParser(description="Migrate a category")
parser.add_argument('-cat', action='store', metavar="CATEGORY", help="Specify the name of the category to process.")
args = parser.parse_args()

if not args.cat:
    print "Please specify category. eg. \"biology\""

print "[0] %s - Started migrate script for inverse document frequencies" % diff()

do_category(args.cat)

print "[0] Finished migration: %s terms over %s categories" % (diff(), n)
