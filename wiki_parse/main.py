from io_utils import load_json, save_json, flatten_hash
from wiki_api import categories_by_depth, fetch_articles_by_titles
from elasticsearch import Elasticsearch
import elastic


depth = 2
file_name = "bio_titles_%s" % depth

if False:
  titles = categories_by_depth(category_string="Category:Biology", limit=depth)
  save_json({"name":"Biology", "titles" : titles}, file_name)

es = Elasticsearch()
if True:
  titles = list(flatten_hash(load_json(file_name)))
  elastic.fetch_articles_and_add_to_elastic_search(es, titles, _index="biology", _doc_type="title")

#print elastic.title_exists(es, _index="biology", _doc_type="title", title="biologist")