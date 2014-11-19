# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

import time
from wiki_api import categories_by_depth, fetch_articles_by_titles
from io_utils import load_json, save_json, flatten_hash, create_file_name
from category_knowledge import saved_titles
from rediss import Rediss

print "this module is old. it still uses elasticsearch!"
exit(1)

def download_wikipedia_titles(categories, depth):
  persisted_titles = persisted_titles = saved_titles(depth)
  for category in categories:
    file_name = create_file_name(category, depth)
    if file_name in persisted_titles:
      print "%s was already downloaded" % file_name
      continue
    print "fetching category titles for: %s" % category
    titles = categories_by_depth(category_string="Category:%s" % category, limit=depth)
    save_json("categories", file_name, {"name": category, "titles" : titles})

# Download
def print_download_status(titles_size, done, acc):
  articles_to_go = titles_size - done
  needed = ((acc / done) * articles_to_go) / 60
  print "%s articles and %s mins to go" % (articles_to_go, needed)

def fetch_articles_and_add_to_elastic_search(rss, titles, category, group_factor=100):
  group_factor, done = _group_factor, 0
  grouped_titles = [titles[i:i+group_factor] for i in range(0, len(titles), group_factor)]
  last, acc = 0, 0
  for sub_titles in grouped_titles:
    before = time.time()
    all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
    rss.add_articles_and_pos_tags(category, all_articles)
    end = time.time() - before
    acc += end
    done += group_factor
    print_download_status(len(titles), done, acc)

def download_article_and_add_to_elastic_search(categories, depth):
  rss = Rediss()
  for category in categories:
    file_name = create_file_name(category, depth)
    titles = list(flatten_hash(load_json("categories", file_name)))
    print "fetched %s titles from %s..." % (len(titles), file_name)
    fetch_articles_and_add_to_elastic_search(rss, titles, category.lower())
    print "done downloading for index=%s and doc_type=%s" % (index, doc_type)
  print "all done!"




