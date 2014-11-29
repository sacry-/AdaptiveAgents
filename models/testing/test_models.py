from __future__ import division

import random
from nltk.corpus import names
from nltk.classify import apply_features
from nltk import NaiveBayesClassifier


SMALL = 'abcdefghijklmnopqrstuwxyz'
UPPER = map(lambda x: x.lower(), SMALL)

def gender_features(word):
  return {"last" : word[-1], "snd_last" : word[-2]}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + 
    [(name, 'female') for name in names.words('female.txt')])

# mutable!
random.shuffle(labeled_names)

the_split = 500
features = [(gender_features(w), gender) for (w, gender) in labeled_names]
train_set = features[:the_split]
test_set = features[the_split:]
classifier = NaiveBayesClassifier.train(train_set)

i = 0
for (feature, gender) in test_set:
  guess = classifier.classify(feature)
  if guess != gender:
    print i, labeled_names[i + 500]
    i += 1

print i, len(test_set) - i