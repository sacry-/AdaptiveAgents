# coding: utf-8
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from elastic import Elastic
from io_utils import save_json
from statistics import statistic_hash

titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
          "brian_dale", "dependence_receptor", "despeciation", "biologist", "biology"]
es = Elastic()
articles = list(es.get_multiple_articles("biology", "title", titles))

h = statistic_hash(articles[0])
save_json(h, "sample_statistics")

