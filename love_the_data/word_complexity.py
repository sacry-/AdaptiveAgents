# coding: utf-8

# Calculate the word complexities using the letter frequencies.

# In[3]:
import os, sys
p = "%s/../persistence" % os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, p)

from ast import literal_eval
from utils import persistence_path
from io_utils import load_json, save_json

# read in the biology_words
h = load_json("love_the_data","biology_words")

# read in the english-letter-frequencies.
# they were checked to add up to 1. Its not included in this .py script
lf = load_json("love_the_data","english-letter-frequencies")["letters"]
lfd = dict(lf) # dictionary variant of lf


# In[4]:
# for the word complexity to work, we may not allow numbers in our words. This regex allows letters, -, _ and space characters.
import re
letter_words = filter(lambda x: re.match("^[a-zA-Z\-_\s]*$", x), h['biology_words'])
# first 15:
#['llactic',
# 'woodi',
# 'spiderl',
# 'pentachlorophenyl',
# 'fumagillol',
# 'spideri',
# 'lophiiform',
# 'woodr',
# 'seland',
# 'crebriflora',
# 'miniblind',
# 'fibrillosa',
# 'yanagisawa',
# 'wendelboi',
# 'chatter']


# Word Complexity

# defining a measure of the word complexity of a word (no source. I invented out of blue)

# Thought 1: a word is more complex when more rare letters occur
# Thought 2: a word with n+1 letters is slightly more complex than one with only n letters

# The complexity of a word comp(w) ranged from 0 to 1 and is given by the formula:
# comp("") = 0
# comp(w[0 to n]) = 
#    let pre = comp(w[0 to n-1]) in
#    pre + (1 - pre) * (1 - lf(lower(w[n]))) ^ 40
# non-letters shall be ignored by keeping the factor unchanged
# the exponentiation by 40 was nesessary to gradually
# shift the range of results from (0.999 .. 1) to (0 .. 1)

def word_complexity(w):
    l = len(w)
    if l == 0:
        return 0
    pre = word_complexity(w[0:l-1])
    weight = (1 - lfd.get(w[l-1].lower(), 1))
    return pre + (1 - pre)*pow(weight, 40)


# In[7]:

# tryig it
test_words = [
    "et", "ao", "zq", "hallo", "welt", "eltw", "rowdy", "desoxyribonucleinacid",
    "turing-machine", "The Way Of My Life ", "The Way Of My Life", "love", "xpvzuywq", "axpvzuywq"]
for (w,wc) in sorted(map(lambda x:(x,word_complexity(x)), test_words), key=lambda x:x[1]):
    print "%f for %s" % (wc, w)
# Output:
# 0.025248 for et
# 0.075862 for ao
# 0.449348 for hallo
# 0.571025 for eltw
# 0.571025 for welt
# 0.744745 for love
# 0.808019 for rowdy
# 0.895376 for turing-machine
# 0.980044 for The Way Of My Life 
# 0.980044 for The Way Of My Life
# 0.998242 for desoxyribonucleinacid
# 0.998476 for zq
# 0.999996 for xpvzuywq
# 0.999996 for axpvzuywq

# works fine :)

# In[8]:

# now lets sort by word complexity
ls = sorted(map(lambda x:(x,word_complexity(x)), letter_words), key=lambda x:x[1]) # lowest first
len(ls) # => 155679

# Views of the list:

ls[:15] # least complex
#[('e', 0.004746253983231669),
# ('t', 0.020599911203095237),
# ('et', 0.025248392775724996),
# ('te', 0.025248392775724996),
# ('tee', 0.029874811474174683),
# ('a', 0.03499117319511314),
# ('ea', 0.03957135018318955),
# ('o', 0.04235248026929027),
# ('tet', 0.04532818932961943),
# ('oe', 0.04689771862434408),
# ('i', 0.04905504318684991),
# ('eeo', 0.051421384123750476),
# ('n', 0.05278352658776362),
# ('ie', 0.05356846947595839),
# ('at', 0.05487026933749692)]


# In[10]:

ls[-15:] # most complex
# (.. not shown here. too long words. one them was the next one here ..)

# gtgtgcactgtgtttgctgacgcaacccccactggttggggcattgccaccacctgtcagctcctttccgggactttcgctttccccctccctattgccacggcgg
# with rating 0.9999999999999057
# Google Search: http://en.wikipedia.org/wiki/WHP_Posttrascriptional_Response_Element

# hehe. biology has some bogus words
# lets grab into the front, end and middle

# In[11]:
ls[75000:75015] # middle
#[('mmegerl', 0.8328260730040393),
# ('highnitrogen', 0.8328284997806163),
# ('lacconectu', 0.8328307328265295),
# ('acetaminophen', 0.8328343336142195),
# ('gradientdirect', 0.8328355734900159),
# ('mummi', 0.8328358675216336),
# ('singlechannel', 0.8328359429199734),
# ('moonvan', 0.8328371719513881),
# ('saintvinc', 0.8328372054208724),
# ('dupuisi', 0.8328379492879117),
# ('solfataricu', 0.8328389919267163),
# ('tippointhead', 0.8328662032782365),
# ('yildirim', 0.832869492260722),
# ('nanocomposit', 0.8328717870991036),
# ('rosalamellatu', 0.8328723955783457)]

# In[12]:

ls[125000:125015] # rather complex
#[('soilfungalpl', 0.9483722857849198),
# ('conkerberri', 0.94837325573125),
# ('exce', 0.9483744026734234),
# ('exec', 0.9483744026734234),
# ('crosscrosslink', 0.9483745442823822),
# ('physicalbas', 0.9483762358373495),
# ('alkaliphila', 0.9483778386455517),
# ('photobacterium', 0.9483785476058285),
# ('lumbalium', 0.9483791128982552),
# ('streambank', 0.9483856432994592),
# ('embryolatimeria', 0.9483896646671892),
# ('kstrophanthosid', 0.9483907044344106),
# ('swulinski', 0.9483934092939951),
# ('subtomogram', 0.9483937964022883),
# ('reichsbank', 0.9483958500818059)]

# In[13]:

ls[1500:1515] # rather simple
#[('rariti', 0.2765528124958161),
# ('detent', 0.2765725565963135),
# ('sensor', 0.27672396652690373),
# ('hearst', 0.27681346371967963),
# ('ternatin', 0.27682804846653786),
# ('internat', 0.27682804846653786),
# ('total', 0.276907063192853),
# ('enniatin', 0.27709083264433604),
# ('intestin', 0.2771971732569174),
# ('hetieri', 0.27721833516120953),
# ('tanaensi', 0.2772852884221805),
# ('ensatina', 0.27728528842218053),
# ('alia', 0.2776381220170026),
# ('hotteana', 0.2778326260266659),
# ('tosteson', 0.27784949959990496)]


# In[16]:

# now saving it!
save_json("love_the_data", "biology-words-complexity", dict(ls))




