# coding: utf-8
from __future__ import division

import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from rediss import RFeature
from rediss import RContent

rc = RContent()

abs_all, size_all = 0, 0
for category in ["biology", "chemistry", "physics"]:
  size = len(list(rc.keys("%s-*" % category)))
  size_all += size
  print "size of %s: %s" % (category, size)

  abs_size_of_docs = map(lambda article: len(article.split(" ")), rc.values_by_pattern("%s-*" % category))
  category_abs = sum(abs_size_of_docs)
  abs_all += category_abs
  print "average size of doc: %s" % (category_abs / size)

print "average size of all: %s" % (abs_all / size_all)