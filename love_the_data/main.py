# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from rediss import RPos
from io_utils import save_json
from statistics import Frequencies

rpos = RPos()

def is_not_category(x):
    return "category:" == x[0:9]

meta_titles = filter(is_not_category, map(lambda x: rpos.real_title(x), rpos.keys("%s*" % "biology")))

print meta_titles
print len(meta_titles)

# TODO: do migration for feature vector calculcation


