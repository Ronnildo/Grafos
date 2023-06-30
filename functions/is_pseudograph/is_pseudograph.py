# Função que verifica se um dado grafo é pseudografo
def is_pseudograph(edges):
        edge_dict = {}
        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1
        for i in edge_dict.items():
            if i[0][0] == i[0][1]:
                return True
        return False