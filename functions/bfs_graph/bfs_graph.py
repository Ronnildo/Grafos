from collections import defaultdict

# Algoritmo busca em largura em um grafo

def bfs_graph(edges, vertices, initial, final):
    # Lista para verificar os grafos adicionados
    dici_edges = defaultdict(list)

    for i in edges:
        dici_edges[i[0]].append(i[1])

    visited = {}
    for i in vertices:
        visited[i] = False

    # Lista para adicionar os vértices visitados
    queue = []

    queue.append(initial)
    visited[initial] = True

    while queue:
        initial = queue.pop(0)
        print(initial, end=", ")

        for i in dici_edges[initial]:
            # print(i)
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
            if visited[i] == True and i == final:
                return queue
