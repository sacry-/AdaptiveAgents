# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from rediss import Rediss
from io_utils import save_json
from statistics import Frequencies


rss = Rediss()
tags = rss.get_pos_tag("biology", "biology")
frequencies = Frequencies(rss, "biology")
for key in tags.keys()[:5]:
  print key, frequencies.idf(key)