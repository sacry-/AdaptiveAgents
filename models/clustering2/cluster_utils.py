

def fst(tpl):
  return tpl[0]

def snd(tpl):
  return tpl[1]
  
def cluster_sizes(clusters):
  return sorted(map(lambda cluster: len(cluster.vectors()), clusters))

def concatMap(f, ls):
    return sum(map(f,ls), [])

def prints(ls):
  for x in ls:
    print x
