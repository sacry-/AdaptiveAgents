# coding: utf-8
from nltk import clean_html
from bs4 import BeautifulSoup
from dewiki.parser import Parser # https://github.com/daddyd/dewiki.git
import re
import time


def remove_curly_braces(s):
  buf = []
  c = 0
  for char in s:
    if char == '{':
      c += 1
      continue
    elif char == '}':
      c -=1
      continue
    elif c == 0:
      buf.append(char)
  return "".join(buf)

def remove_markup(s):
  return Parser().parse_string(s)

def remove_html(s):
  return BeautifulSoup(s).get_text()

def clean_parse(s):
  return remove_html(remove_markup(remove_curly_braces(s)))

