#Verifica quais vértices não são alcançaveis pelo vértice de entrada
def vertices_unreachable_of_input(edges, vertice):

        edge_dict = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1
        # print(edge_dict)

        vertex_list = []

        for i in edge_dict.items():
            if i[0][0] in vertex_list or i[0][1] in vertex_list:
                pass
            if i[0][0] != vertice and i[1] == 1:
                vertex_list.append(i[0][0])
                vertex_list.append(i[0][1])

        return vertex_list