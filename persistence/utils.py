import re

def good_title(title):
  title = re.sub("\s+", '_', title)
  title = re.sub("_+", '_', title)
  return title.lower()