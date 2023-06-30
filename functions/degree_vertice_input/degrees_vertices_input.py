def degree_vertice_input(edges, vertice):
        edge_dict = {}
        grau = {}
        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1

        grau[vertice] = 0

        for i in edge_dict.items():
            # print(i[0][0], i[0][1], i[1])
            for j in grau.keys():
                if i[0][0] == j or i[0][1] == j:
                    grau[j] += 1

        return grau