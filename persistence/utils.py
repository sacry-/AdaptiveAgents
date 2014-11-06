import re
from socket import gethostname
from os import getenv


def good_title(title):
  title = re.sub("\s+", '_', title)
  title = re.sub("_+", '_', title)
  return title.lower()

def persistence_path():
  if gethostname() == "swaneetXu-VPCEH2Q1E":
    return getenv('WIN',"/dual/Users/Swaneet")+"/github/AdaptiveAgents/persistence/"
  return "/Users/sacry/dev/uni/s5/la/AdaptiveAgents/persistence/"