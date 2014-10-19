from io_utils import load_json, save_json, flatten_hash
from wiki_api import categories_by_depth, fetch_articles_by_titles
from elasticsearch import Elasticsearch
import elastic

es = Elasticsearch()

# Extract all Categories by Depth
depth = 2
# titles = categories_by_depth(category_string="Category:Biology", limit=depth)
# save_json({"name":"Biology", "titles" : titles}, "bio_titles_%s" % depth)

# Fetch all Articles by given titles (as List)
file_name = "bio_titles_%s" % depth
titles = list(flatten_hash(load_json(file_name)))
unpersisted_titles = elastic.all_unpersisted_titles(es, "biology", "title", titles)

i = 1
tmp = titles
grouped_titles = [unpersisted_titles[i:i+10] for i in range(0, len(unpersisted_titles), 10)]
for sub_titles in grouped_titles:
  if i % 100 == 0:
    tmp = elastic.all_unpersisted_titles(es, "biology", "title", tmp)
    size_title, size_tmp = len(titles), len(tmp)
    print "total titles: %s, to go: %s, persisted: %s" % (size_title, size_tmp, size_title - size_tmp)
  all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
  elastic.add_multiple_articles(es, "biology", "title", all_articles)
  i += 1