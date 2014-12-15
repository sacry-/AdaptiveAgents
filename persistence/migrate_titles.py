from io_utils import flatten_hash, load_json, save_json
from utils import good_title
from rediss import RFeature
import re


rfeature = RFeature()
pattern = re.compile("(Category\:|List of|File\:).*")
categories = ["biology", "physics", "chemistry"]

r = {}
for cat in categories:
    r[cat] = []
    l = set(good_title(title) for title in flatten_hash(load_json("categories", "%s_titles_1" % cat)) if not pattern.search(title))
    for title, fvector in rfeature.key_value_by_titles(cat, l):
        s = sum(map(lambda x: x[1], fvector)) 
        if s > 500:
            r[cat].append(title)
    

save_json("categories", "all_cats_3000", r)
#print len(r)