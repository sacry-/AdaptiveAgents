from io_utils import load_json, save_json, flatten_hash
from wiki_api import categories_by_depth, fetch_articles_by_titles

# Extract all Categories by Depth
# titles = categories_by_depth(category_string="Category:Biology", limit=1)
# save_json({"name":"Biology", "titles" : titles}, "bio_titles2")

# Fetch all Articles by given titles (as List)
# Number stands for depth
file_name = "bio_titles_%s" % 1
title_list = flatten_hash(load_json(file_name))
fetch_articles_by_titles(title_list)