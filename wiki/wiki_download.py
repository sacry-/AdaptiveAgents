import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)
import time

from wiki_api import categories_by_depth, fetch_articles_by_titles
from io_utils import load_json, save_json, flatten_hash, create_file_name
from category_knowledge import saved_titles
from elastic import Elastic


def download_wikipedia_titles(categories, depth):
  persisted_titles = persisted_titles = saved_titles(depth)
  for category in categories:
    file_name = create_file_name(category, depth)

    if file_name in persisted_titles:
      print "%s was already downloaded" % file_name
      continue

    print "fetching category titles for: %s" % category
    titles = categories_by_depth(category_string="Category:%s" % category, limit=depth)
    save_json({"name": category, "titles" : titles}, file_name)

# Download
def print_download_status(titles_size, done, acc):
  articles_to_go = titles_size - done
  needed = ((acc / done) * articles_to_go) / 60
  print "%s articles and %s mins to go" % (articles_to_go, needed)

def fetch_articles_and_add_to_elastic_search(es, titles, _index, _doc_type):
  group_factor, done = 10, 0
  grouped_titles = [titles[i:i+group_factor] for i in range(0, len(titles), group_factor)]
  last, acc = 0, 0
  for sub_titles in grouped_titles:
    before = time.time()
    all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
    es.add_multiple_articles(_index, _doc_type, all_articles)
    end = time.time() - before
    acc += end
    done += group_factor
    print_download_status(len(titles), done, acc)

def download_article_and_add_to_elastic_search(categories, depth):
  elastic = Elastic("localhost", 9200)
  for category in categories:
    file_name = create_file_name(category, depth)
    titles = list(flatten_hash(load_json(file_name)))
    print "fetched %s titles from %s..." % (len(titles), file_name)
    index, doc_type = category.lower(), "title"
    elastic.dummy(index)
    titles = elastic.all_unpersisted_titles(index, doc_type, titles)
    print "articles to go: %s" % len(titles)
    fetch_articles_and_add_to_elastic_search(elastic, titles, index, doc_type)
    print "done downloading for index=%s and doc_type=%s" % (index, doc_type)
  print "all done!"




