# Retornar o grau de cada vértice de um grafo 
def degrees_vertices(vertices, edges):
        edge_dict = {}
        graus = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1
        # print(edge_dict)

        for ver in vertices:
            graus[ver] = 0

        for i in edge_dict.items():
            # print(i[0][0], i[0][1], i[1])
            for j in graus.keys():
                if i[0][0] == j or i[0][1] == j:
                    graus[j] += 1
        return graus