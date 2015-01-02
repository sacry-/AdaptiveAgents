import pygraphviz as pgv

'''
# (1) <--> (2) <--> (3)
TEST_DICT = {'1': ['2'], '2': ['1', '3'], '3': ['2']}

def fromTreeToGraphDict(tree=None):
  if not tree:
    return TEST_DICT
  d = {}

  # process

  return d 


d = fromTreeToGraphDict()
G=pgv.AGraph(d)


'''
G=pgv.AGraph()

G.add_node('a')
G.add_edge('b','c')
G.add_edge('a', 'c')
G.add_edge('c', 'c')
print G
G.draw('file.ps',prog='neato')
G.write("file.dot")





