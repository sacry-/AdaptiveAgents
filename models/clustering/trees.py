from treelib import Tree, Node
# Examples: http://hsiamin.com/treelib/examples.html#basic-usage
# Documentation: http://hsiamin.com/treelib/pyapi.html
from ast import literal_eval

def merge_trees(t1, t2, tick):
  t = Tree()
  identifier = -tick # using negative numbers as identifiers, positive numbers are ids for the leaf nodes
  name = "new_cluster_%s" % tick
  t.create_node(name, identifier)
  t.paste(identifier, t1)
  t.paste(identifier, t2)
  return t, name

def create_tree(indexed_titles, root, children=None):
  t = Tree()
  identifier = indexed_titles[root]
  t.create_node(root, identifier)
  if children:
    for sub_tree in children:
      t.paste(identifier, sub_tree)
  return t

def clustered_trees(indexed_titles):
  cluster_trees = []
  for title in indexed_titles.keys():
    cluster_trees.append(create_tree(indexed_titles, title))
  return cluster_trees

def from_json(json_str, titles):
  try:
    json = literal_eval(json_str)
  except:
    json = json_str
  t = None
  if type(json) == str:
    t = create_tree(titles, json)
  if type(json) == dict:
    title = json.keys()[0]
    children = [from_json(child, titles) for child in json[title]['children']]
    t = create_tree(titles, title, children)
  return t


def tree_test():
  test_titles = [
    "deletion_mapping", 
    "orthotheca", 
    "genetically_modified_sperm", 
    "category:intelligence"
  ]
  titles = dict((e, idx) for idx, e in enumerate(test_titles))

  # Tree testing
  t = Tree()
  t.create_node("deletion_mapping",15)
  t.create_node("orthotheca",14, parent=15)
  t.create_node("genetically_modified_sperm",13, parent=14)
  t.create_node("category:intelligence",12, parent=14)
  t.show()

  json = t.to_json()
  print "\nAs JSON:"
  print json

  print "\nAnd parsed back into a tree."
  t2 = from_json(json, titles)
  t2.show()

# tree_test()
