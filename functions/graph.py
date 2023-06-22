from collections import defaultdict, deque
import functions.graph_model as gm


class Graph:

    def __init__(self, json):
        self.__input = json
        self.__graph = {}
        self.adj_mtx = []

    def graph_check(self):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        mult, pseud, complet, desconex = {}, {}, {}, {}

        for i in range(len(self.__graph)):
            mult[i+1] = self.is_multigraph(self.__graph[i]["edges"])
            pseud[i+1] = self.is_pseudograph(self.__graph[i]["edges"])
            complet[i+1] = self.is_complete_graph(
                self.__graph[i]["vertices"], self.__graph[i]["edges"])
            desconex[i+1] = self.is_disconnected_graph(
                self.__graph[i]["vertices"], self.__graph[i]["edges"])
        return mult, pseud, complet, desconex

    def is_multigraph(self, edges):
        # Criar um dicionário para armazenar as arestas
        edge_dict = {}

        # print(self.__graph)

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

    def is_pseudograph(self, edges):

        edge_dict = {}
        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1
        # print(edge_dict)
        for i in edge_dict.items():
            # [0][0]== [0][1]
            # ("D"  ,   "D")
            if i[0][0] == i[0][1]:
                # print(f"{i[0][0]} - {i[0][1]}")
                return True
        return False

    def is_disconnected_graph(self, vertices, edges):
        '''para cada par s e t de seus vértices, existe um caminho com origem s e término t'''
        """ VERIFICAR SE CADA POSIÇÃO NA LISTA DE VÉRTICES ESTÁ CONTIDO NA LISTA DE ARESTAS"""

        # Para um grafo ser conexo é necessário que no minimo
        # a quantidade de arestas seja 2 vezes o número de vértices
        calc = len(vertices) * 2
        if len(edges) * 2 < calc:
            return True
        
        return False

    # verificar se o grafo é completo
    def is_complete_graph(self, vertices, edges):

        calc_edge = (len(vertices) ** 2) - len(vertices)
        # print(calc_edge)
        if self.is_multigraph(edges):
            return False
        elif self.is_pseudograph(edges):
            return False
        else:
            if calc_edge == (len(edges)) * 2:
                # print(f"1°: {edges}")
                return True
            elif calc_edge == ((len(edges) - 1) * 2):
                return True
            elif len(edges) % 2 == 0:
                # print(f"2: {len(a) * 2}")
                # print(f"2°: {edges}")
                par = calc_edge == len(edges) * 2
                return par
            elif calc_edge == (len(edges) - 1) * 2:
                # print(f"3°: {calc_edge}")
                return True
        return False

    def graus_vertices(self):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[0]["vertices"]
        edges = self.__graph[0]["edges"]

        edge_dict = {}
        graus = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1
        # print(edge_dict)

        for ver in degrees:
            graus[ver] = 0

        for i in edge_dict.items():
            # print(i[0][0], i[0][1], i[1])
            for j in graus.keys():
                if i[0][0] == j or i[0][1] == j:
                    graus[j] += 1
        return graus

    def degree_vertice_input(self, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[0]["vertices"]
        edges = self.__graph[0]["edges"]

        edge_dict = {}
        grau = {}
        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            if edge_tuple in edge_dict:
                edge_dict[edge_tuple] += 1
            else:
                edge_dict[edge_tuple] = 1

        grau[degree] = 0

        for i in edge_dict.items():
            # print(i[0][0], i[0][1], i[1])
            for j in grau.keys():
                if i[0][0] == j or i[0][1] == j:
                    grau[j] += 1

        return grau

    def reachable_vertices_of_A(self, idgraph, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[idgraph]["vertices"]
        edges = self.__graph[idgraph]["edges"]

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

            elif i[0][0] != degree and i[1] == 1:
                if i[0][0] in vertex_list:
                    vertex_list.append(i[0][1])

            else:
                vertex_list.append(i[0][1])
        return vertex_list

    def vertices_unreachable_of_A(self, idgraph, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[idgraph]["vertices"]
        edges = self.__graph[idgraph]["edges"]

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
            if i[0][0] != degree and i[1] == 1:
                vertex_list.append(i[0][0])
                vertex_list.append(i[0][1])

        return vertex_list

    def bfs_graph(self, initial, final):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[10]["vertices"]
        edges = self.__graph[10]["edges"]
        # Lista para verificar os grafos adicionados
        dici_edges = defaultdict(list)
        for i in edges:
            dici_edges[i[0]].append(i[1])
        #print("Edges_dici: ", dici_edges)
        
        visited = {}
        for i in degrees:
            visited[i] = False
        #print("Visited: ", visited)
        
        # Lista para adicionar os vértices visitados
        queue = []

        queue.append(initial)
        visited[initial] = True
        
        while queue:
            initial = queue.pop(0)
            print(initial, end=", ")

            for i in dici_edges[initial]:
                #print(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                if visited[i] == True and i == final:
                    return queue
    def dfs_function(self, initial, final, visited):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[10]["vertices"]
        edges = self.__graph[10]["edges"]


        dici_edges = defaultdict(list)
        for i in edges:
            dici_edges[i[0]].append(i[1])

        visited.add(initial)
        print(initial, end=" ")
        
        for teste in dici_edges[initial]:
            if teste not in visited:
               
                self.dfs_function(teste, final, visited)
            if teste == final:
                break
    def dfs(self, initial, final):
        visited = set()
        self.dfs_function(initial, final, visited)
        return visited  