# Função que verifica se o grafo é um multigrafo
def is_multigraph(edges):
        # Criar um dicionário para armazenar as arestas
        edge_dict = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1

        for i in edge_dict.values():
            if i > 1:
                return True
        return False