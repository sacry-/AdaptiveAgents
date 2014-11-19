# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from wiki_download import download_wikipedia_titles
from wiki_download import download_article_and_add_to_redis
from category_knowledge import USED_CATEGORIES

print "this module is old. it still uses elasticsearch!"
exit(1)

download_wikipedia_titles(categories=USED_CATEGORIES, depth=2)
download_article_and_add_to_redis(categories=USED_CATEGORIES, depth=2)
