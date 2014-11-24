
# coding: utf-8

# In[1]:

get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')


# <h3>Fast and Effective Text Mining Using Linear-time Document Clustering</h3>
# <a href="http://comminfo.rutgers.edu/~muresan/IR/Docs/Articles/sigkddLarsen1999.pdf">PDF</a>
# 
# Goal:
#     Clustering of Documents
# 
# Basic Procedure:
# <h4>1. Feature Extraction</h4>
# <p>Feature Extraciton maps each document to a concise representation of its topic</p>
# <p>     FeatureVector(document) := the n most-weightend words of that document (default n = 25)</p>
# <p>        where weight(t,d) := tf(t,d) * idf(t)</p>
# <h4>2. Clustering</h4>

# In[2]:

from persistence.rediss import RPos, RFeature
from multiprocessing import Pool, cpu_count

cat = "biology"

rfeature = RFeature()
rpos = RPos()

DS = ['category:cycad_stubs', 'pyrenocine', 'ericoid_mycorrhiza', 'islander_(database)', 'list_of_metropolitan_areas_in_the_united_kingdom', 'juha_hernesniemi', 'book:biology', 'ngsmethdb', 'estrogen_and_neurodegenerative_diseases', 'molecular_genetics_and_metabolism', 'antibiotic_resistance', 'functional_ecology', 'mesenchymal_stem_cell', "on_nature's_trail", 'history_of_eugenics', 'mt-tq', 'underwater_camouflage', 'sublingual_caruncle', 'ventral_reticular_nucleus', 'list_of_arecaceae_genera', 'hypomyces', 'p1-derived_artificial_chromosome', 'iodine_in_biology', 'arca-net', 'list_of_troglobites', 'luolishaniidae', 'outline_of_life_extension', 'peripatopsidae', 'list_of_geneticists', 'genetic_ablation', 'mucor', 'thomas_hunt_morgan_medal', '3-hydroxypropionate_pathway', 'aerobiology', 'disease_resistance_in_fruit_and_vegetables', 'evolution_of_photosynthesis', 'retroposon', 'law_of_specific_nerve_energies', 'iteron', 'tentaculites_oswegoensis', 'karenia_(dinoflagellate)', 'philippine_native_plants_conservation_society', 'southwestern_blot', 'rete_ovarii', 'follicular_lumen', 'dna_sequencing_theory', 'parenchymella', 'gard_model', 'aortopulmonary_window', 'azoospermia_factor', "estonian_naturalists'_society", 'eos_(protein)', 'schistosoma_mekongi', 'fusidic_acid', 'beauvericin', 'ephedra_fragilis', 'biomolecular_complex', 'epsilometer_test', 'gunneraceae', 'available_name', 'neuroepidemiology', 'data_sharing', 'fluroxypyr', 'blue_zone', 'cursorial_hunting', "doctor's_visit", 'actinorhodin', 'list_of_sequenced_protist_genomes', 'cryptochrome', 'mir-544_microrna_precursor_family', 'barbara_a._schaal', 'fedomia', 'teleomorph,_anamorph_and_holomorph', 'falling_cat_problem', 'electrophoretic_mobility_shift_assay', 'information_hyperlinked_over_proteins', 'lumi_(software)', "tollmann's_hypothetical_bolide", 'huffia', 'rafflesia_pricei', 'preformationism', 'nuclear_lamina', 'list_of_countries_and_territories_with_fewer_than_100,000_people', 'herring_bodies', 'v\\u00e1clav_hampl', 'animalcule', 'iditol', 'catenochytridium', 'silverquant', 'lyso-', 'pgreen', 'ceragenin', 'isagenix_international']


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
        zip(ds, rpos.values_by_titles(cat, ds, ordered=True))
    )
    return 0


def safe(x):
    if not x:
        return 0
    return float(x)

# [Term] -> [Float]
def idf_multi(ts):
    return map(safe, rfeature.values_by_titles(cat, ts, ordered=True))

print idf_multi(["biolog"])

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

# print "fvecs N: %s" % feature_vector_multi(["biology", "biologist", "rnase_h"])
ds = ["biology", "biologist", "rnase_h"]
ds = DS

if REDIS_HAS_IDFS == False:
    print "Do you have the IDFs in Redis? Check the REDIS_HAS_IDFS flag.\nNothing done."
    exit(1)

tf_multi_d_load("dummy", ds) # force self.freqs[d] for d in ds to be loaded


# Title -> [ (Term, Float) ]
def get_words_frequencies(tpl):
    d, words = tpl
    return w_multi_t(words, d)

def sort_and_chomp(v):
    return sorted(v, key=lambda x:-x[1])[0:maxLen]

pool = Pool(cpu_count() - 1) # create cpu_pool, leave one cpu untoched for gui

# wordss :: [ [Word] ]
wordss = map( get_words , ds)

# [ [(Term, Float)] ]
vectors = map( get_words_frequencies , zip(ds, wordss))

# [ [(Term, Float)] ]
fvectors = map( sort_and_chomp , vectors)

# term frequency, inverse document frequency, weight, feature vector

# calculating this was almost instant!!!
for (d, fvec) in zip(ds, fvectors):
    print "%s has %s..." % (d, fvec[0:2])


# In[ ]:




# In[ ]:



