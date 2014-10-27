from io_utils import load_json, save_json, flatten_hash
from wiki_api import categories_by_depth, fetch_articles_by_titles
from category_knowledge import basic_categories, saved_titles
from elasticsearch import Elasticsearch
import elastic


def download_wikipedia_titles(depth):
  persisted_titles = persisted_titles = saved_titles(depth)
  for field in basic_categories():
    file_name = ("%s_titles_%s" % (field, depth)).lower()

    if file_name in persisted_titles:
      continue

    print "Fetching Categorie Titles for: %s" % field

    if True:
      titles = categories_by_depth(category_string="Category:%s" % field, limit=depth)
      save_json({"name": field, "titles" : titles}, "categories/%s" % file_name)

def download_article_and_add_to_elastic_search(titles=[]):
  es = Elasticsearch()
  if not titles:
    titles = list(flatten_hash(load_json("categories/%s" % file_name)))
  elastic.fetch_articles_and_add_to_elastic_search(es, titles, _index=field.lower(), _doc_type="title")


# download_wikipedia_titles(depth=2)
download_article_and_add_to_elastic_search(["biology"])








