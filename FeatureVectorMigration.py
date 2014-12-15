
from persistence.io_utils import load_json
from persistence.rediss import RPos, RIdf, RFeature
from multiprocessing import Pool, cpu_count
import time

ridf = RIdf()
rpos = RPos()
rfeature = RFeature()


cat_titles = load_json("categories", "all_cats_3000")

titles = sum(cat_titles.values(), [])

cat_of = {}
for cat_, ts in cat_titles.iteritems():
    for t in ts:
        cat_of[t] = cat_

#my_ts = titles[:2] + titles[-2:]
#print my_ts
#print map(lambda x:cat_of[x], my_ts)
#exit(0)
# term frequency and inverse document frequencies are already implemented in statistics

# In[3]:

REDIS_HAS_IDFS = True

class Frequency():
  def __init__(self, pos_tags):
    self.pos_tags = pos_tags # {"words" : {"tags" : counts}}

  def tf(self, t):
    return sum(self.pos_tags.get(t, {}).values())

  def words(self):
    return self.pos_tags.keys()

freqs = {}
maxLen = 25


# FREQUENCIES

# Term -> [ Title ] -> ()
def tf_multi_d_load(t, ds):
    global freqs # explicit global variable.....
    freqs = dict(
        (d, Frequency(ptags))
        for d, ptags in
        zip(ds, list(rpos.value_by_title(cat_of[d], d) for d in ds))
    )
    return 0


def safe(x):
    if not x:
        return 0
    return float(x)

# [Term] -> [Float]
def idf_multi(ts):
    return map(safe, ridf.values_by_titles("all", ts, ordered=True))


# [Term] -> Title -> [ Int ]
def tf_multi_t(ts, d):
    return map(lambda t: int(freqs.get(d,{t:0}).tf(t)), ts)


# [ Term ] -> Title -> [ (Term, Float) ]
def w_multi_t(ts, d):
    # [ Float ]
    idfs = idf_multi(ts) # ["biolog", "magon"] => [ 3.412 , 9.712 ]

    # [ Int ]
    tfs = tf_multi_t(ts, d) # [ "biolog", "magon" ] => [ 23, 2 ]

    weights = list((ts[i], _tf*_idf) for i, (_tf, _idf) in enumerate(zip(tfs, idfs)))

    return weights


# Title -> [ Word ]
def get_words(d):
    ws = freqs[d].words()
    diff = maxLen - len(ws)
    # make sure, the list words are atleast 25(maxLEn) words long
    if diff > 0:
        ds = ["dummy" for i in xrange(diff)]
        return ws + ds
    return ws


# [Title] ( -> Int) -> [ [(Term,Float)] ]
# def feature_vector_multi(ds, maxLen=25):

ds = titles

if REDIS_HAS_IDFS == False:
    print "Do you have the IDFs in Redis? Check the REDIS_HAS_IDFS flag.\nNothing done."
    exit(1)


t__ = time.clock()
def diff():
    return "%s" % ((time.clock() - t__)) 

print "[1] %s %s - loading freqs..." % (diff(), "all")

tf_multi_d_load("dummy", ds) # force self.freqs[d] for d in ds to be loaded

# Title -> [ (Term, Float) ]
def get_words_frequencies(tpl):
    d, words = tpl
    return w_multi_t(words, d)

def sort_and_chomp(v):
    return sorted(v, key=lambda x:-x[1])[0:maxLen]

pool = Pool(cpu_count() - 1) # create cpu_pool, leave one cpu untoched for gui


print "[2] %s %s - loading words..." % (diff(), "all")
# wordss :: [ [Word] ]
wordss = map( get_words , ds)

print "[3] %s %s - loading word frequecies..." % (diff(), "all")
# [ [(Term, Float)] ]
vectors = map( get_words_frequencies , zip(ds, wordss))

print "[4] %s %s - calculating feature vectors..." % (diff(), "all")
# [ [(Term, Float)] ]
fvectors = map( sort_and_chomp , vectors)

# term frequency, inverse document frequency, weight, feature vector

print "[4] %s %s - saving into %s" % (diff(), "all", rfeature)
mapping = dict(zip(ds, fvectors))
rfeature.puts("all", mapping)
print "[5] %s %s - Finished %s!" % (diff(), "all", rfeature)



# In[ ]:




# In[ ]:



