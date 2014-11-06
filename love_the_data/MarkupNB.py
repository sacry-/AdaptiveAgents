'''
from elastic import Elastic
from nltk import word_tokenize, FreqDist
import itertools
from nltk.corpus import stopwords

es = Elastic()
stops = stopwords.words('english')
special_stops = [u'(', u')', u',', u':', u'.', u';', u'``', u"''", u"'", u'[', u']', u'?', u'/', u'#', u'*', u'&', u'-', u'@', u'--', u'%', u'\u2014', u'+', u'=', u'\u2013', u'$', u'..', u'//', u'\\', u'>', u'==', u'\xd7', u'!', u'**', u'~', u'^', u'\u2194', u'\u2193', u'\u2212', u':*', u'=-', u'\\\\', u':=', u'\\|', u'\u2014\u03bf', u'\u0394\u03c8', u'\u2192', u'\u2260', u'\u0394', u'`', u'|-', u'|', u'+\\', u'~~', u'.^', u'\\^', u'\u03b2', u'<', u'.-', u'\u03a6', u'=\\', u"'+", u'++', u"'~", u'*+', u"'\\", u'||', u"'/", u"'-", u'*-', u'.\\', u',.', u'*^', u'`^', u'\u2208', u'|\\', u'/*', u'*/', u'^*', u"'*", u'\xb1', u'-^', u'\xbc', u'\u232a', u',\\', u'\u2026', u'\u212b']
stops.extend( special_stops )

def lexical_diversity(ls):
    return len(set(ls)) / float(len(ls))

def remove_stops(tokens):
    return filter(lambda x: x not in stops, tokens)

# ElementHash from ElasticSearch -> Hash with calculated attributes
def process(elem):
    title = elem['_source']['title']
    s = elem['_source']['content']
    ls = word_tokenize(s)
    pure = remove_stops(ls)
    h = {"title": title, "tokens":pure}
    h['lex_div'] = lexical_diversity(ls)
    h['freq'] = FreqDist(h['tokens'])
    return h


# Example usage of elastic search scrolling

import re

commons = []
i = 0

def f(s):
    return re.match(r'^https?:\/\/.*[\r\n]*', s, flags=re.MULTILINE) or re.match('^\W{1,2}$',s)

# creates a list of all contained words and prints the progress. this was used to calculate the stopwords
for bulk in es.generator_scroll("biology","title"):
    for elem in bulk:
        tokens = word_tokenize(elem['_source']['content'])
        commons.extend(filter(f,tokens))
        i += 1
        if i % 100 == 0:
            print i / float(16672)
'''