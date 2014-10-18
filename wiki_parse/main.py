from io_utils import load_json, save_json, flatten_hash
from wiki_api import categories_by_depth, fetch_articles_by_titles
from elasticsearch import Elasticsearch
import elastic

es = Elasticsearch()

# Extract all Categories by Depth
# titles = categories_by_depth(category_string="Category:Biology", limit=1)
# save_json({"name":"Biology", "titles" : titles}, "bio_titles2")

# Fetch all Articles by given titles (as List)
# Number stands for depth
file_name = "bio_titles_%s" % 1
titles = list(flatten_hash(load_json(file_name)))
unpersisted_titles = elastic.all_unpersisted_titles(es, "biology", "title", titles)
print "total titles: %s, not_perstisted: %s" % (len(titles), len(unpersisted_titles))

grouped_titles = [unpersisted_titles[i:i+10] for i in range(0, len(unpersisted_titles), 10)]
for sub_titles in grouped_titles:
  all_articles = fetch_articles_by_titles(title_list=sub_titles, limit=len(sub_titles))
  elastic.add_multiple_articles(es, "biology", "title", all_articles)