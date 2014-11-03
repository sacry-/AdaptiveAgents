from nltk import word_tokenize, data


def tokenize(s):
  return word_tokenize(s)

def sentence_tokenize(s):
  sent_detector = data.load('tokenizers/punkt/english.pickle')
  sentences = []
  for sentence in sent_detector.tokenize(s.strip()):
    if sentence.find("See also") != -1:
      return sentences
    sentences.append(tokenize(sentence))
  return sentences