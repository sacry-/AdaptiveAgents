from nltk import clean_html
from dewiki.parser import Parser # https://github.com/daddyd/dewiki.git
from wiki_api import fetch_articles_by_titles
from io_utils import read, save

# String -> String
def remove_markup(s):
  return Parser().parse_string(s)

def remove_html(s):
  return clean_html(s)

def test():
  article = fetch_articles_by_titles(["biology"], 1)
  save("biology.txt", article[0]["content"])
  t = read("biology.txt")
  t1 = remove_markup(t)
  save("biology_1.txt", t1)
  t2 = remove_html(t1)
  save("biology_2.txt", t2)
  print "Done!"

test()