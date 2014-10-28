from io_utils import load_json, save_json, flatten_hash, create_file_name
from wiki_api import categories_by_depth, fetch_articles_by_titles
from category_knowledge import USED_CATEGORIES, saved_titles
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
    elastic.fetch_articles_and_add_to_elastic_search(titles, index, doc_type)
    print "done downloading for index=%s and doc_type=%s" % (index, doc_type)
  print "all done!"


download_wikipedia_titles(categories=USED_CATEGORIES, depth=2)
download_article_and_add_to_elastic_search(categories=USED_CATEGORIES, depth=2)





