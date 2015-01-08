
def cluster_sizes(clusters):
    return sorted(map(lambda cluster: len(cluster.vectors()), clusters))
