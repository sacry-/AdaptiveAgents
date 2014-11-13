
# coding: utf-8

# runfile to see some distances. more distances are to come.

# In[3]:

from persistence.elastic import Elastic
from persistence.io_utils import save_json
from love_the_data.statistics import Statistics
es = Elastic()


# In[5]:

titles = ["biology", "biologist", "biological_ornament", "birth", "cell_population_data",
            "brian_dale", "dependence_receptor", "despeciation"]
articles = list(es.get_multiple_articles("biology", "title", titles))
stats = map(lambda a: Statistics(a).as_dict(), articles)


# In[13]:

# for biology
# average lemma complexity biology: 0.660727943852
# average word size biology: 6.37006237006

def lc_avg(h):
    return h['stats']['lemmas']['dev_lemma_complexity']
def lc_dev(h):
    return h['stats']['lemmas']['avg_lemma_complexity']
def ws_avg(h):
    return h['stats']['lemmas']['avg_word_size']
def ws_dev(h):
    return h['stats']['lemmas']['dev_word_size']

# stddev added
print "complexities average: %1.2f +- %1.2f" % (lc_avg(stats[0]), lc_dev(stats[0]))
print "word sizes average:   %1.2f +- %1.2f" % (ws_avg(stats[0]), ws_dev(stats[0]))


# Defining complexity of the article


# In[14]:

# and Distance based the four avrage adn stddev of wordsize and complexities
# each document corresponds to a 4-dimensional vector
def vector(h):
    return [lc_avg(h), lc_dev(h), ws_avg(h), ws_dev(h)]

import math

# distance 1
def euclidic(va,vb):
    s = 0
    for i in range(0, len(va)):
        s += pow(vb[i] - va[i], 2)
    return math.sqrt(s)

_va = vector(stats[0])
print _va
_vb = vector(stats[1])
print _vb
euclidic(_va, _vb)


# In[15]:

l = len(stats)
for i in range(0,l):
    for j in range(i,l):
        t1 = titles[i]
        t2 = titles[j]
        va = vector(stats[i])
        vb = vector(stats[j])
        dist = euclidic(va, vb)
        print "%3.3f for %s <-> %s" % (dist, t1,t2)


# In[ ]:



