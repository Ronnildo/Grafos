# Algoritmo busca em profundidade em um grafo
from collections import defaultdict


def dfs_function(edges, initial, final, visited):
        dici_edges = defaultdict(list)
        for i in edges:
            dici_edges[i[0]].append(i[1])

        visited.add(initial)
        
        for de in dici_edges[initial]:
            if de not in visited:
                dfs_function(edges, de, final, visited)
            if de == final:
                break
def dfs(edges, initial, final):
    visited = set()
    dfs_function(edges, initial, final, visited)
    return visited