titles = ["deletion_mapping", "orthotheca", "genetically_modified_sperm", "category:intelligence"]

def idx(title):
    return titles.index(title)

## =============================================

# treelib, simple and effective tree library
from treelib import Tree, Node
# Examples: http://hsiamin.com/treelib/examples.html#basic-usage
# Documentation: http://hsiamin.com/treelib/pyapi.html

t = Tree()
t.create_node("deletion_mapping",15)
t.create_node("orthotheca",14, parent=15)
t.create_node("genetically_modified_sperm",13, parent=14)
t.create_node("category:intelligence",12, parent=14)
print "Example Tree:"
t.show()

json = t.to_json()
print "\nAs JSON:"
print json


from ast import literal_eval
# JSON-String -> Titles -> Tree
def from_json(json_str, titles):
    json = ""
    
    try:
        json = literal_eval(json_str)
    except:
        json = json_str
        
    # leaf node
    if type(json) == str:
        title = json
        t = Tree()
        t.create_node(title,idx(title))
        return t
    
    # root node
    if type(json) == dict:
        node = json.keys()[0]  # get node name
        children = map(lambda x:from_json(x,titles),json[node]['children'])  # parse children
        t = Tree()
        identifier = idx(node)
        t.create_node(node,identifier) # create node
        for sub_tree in children:
            t.paste(identifier, sub_tree) # add children
        return t
        
print "\nAnd parsed back into a tree."
t2 = from_json(json, titles)
t2.show()
