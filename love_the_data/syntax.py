from nltk import word_tokenize, data


def tag(sentence):
  return str(word_tokenize(sentence))

def sentence_tokenize(s):
  sent_detector = data.load('tokenizers/punkt/english.pickle')
  sentences = []
  for sentence in sent_detector.tokenize(s.strip()):
    if sentence.find("See also") != -1:
      return "\n--------\n".join(sentences)
    sentences.append(tag(sentence))
  return "\n--------\n".join(sentences)