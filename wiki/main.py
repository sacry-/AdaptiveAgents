# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from wiki_download import download_wikipedia_titles
from wiki_download import download_article_and_add_to_elastic_search
from category_knowledge import USED_CATEGORIES


download_wikipedia_titles(categories=USED_CATEGORIES, depth=2)
download_article_and_add_to_elastic_search(categories=USED_CATEGORIES, depth=2)