import sys
from functions.bfs_graph.bfs_graph import bfs_graph
from functions.degree_vertice_input.degrees_vertices_input import degree_vertice_input
from functions.dfs_graph.dfs_graph import dfs
from functions.reachable_vertices_of_input.check_reachable_graph import reachable_vertices_of_input
from functions.vertices_unreachable_of_input.check_unreachable_graph import vertices_unreachable_of_input
from graph import Graph
from lib.graph_specific import graph_specific_return
from lib.menu import menu_inicial, submenu
from functions.is_multigraph.is_multigraph import is_multigraph
from functions.is_pseudograph.is_pseudograph import is_pseudograph
from functions.is_disconnected_graph.is_disconnected_graph import is_disconnected_graph
from functions.is_complete_graph.is_complete_graph import is_complete_graph


class ExecuteGraph:
    def __init__(self, json):
        self.__json = json

    def verify_op(self, entrada):
        graph = Graph(self.__json)
        try:

            # Is_Multigraph
            if entrada == 1:
                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                if is_multigraph(e):
                    print(f"O grafo de ID={i-1} é Multigrafo")
                    print("\n")

                else:
                    print(f"O grafo de ID={i-1} não é Multigrafo")
                    print("\n")
                return True
            if entrada == 2:
                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                if is_pseudograph(e):
                    print(f"O grafo de ID={i-1} é Pseudografo")
                    print("\n")
                else:
                    print(f"O grafo de ID={i-1} não é Pseudografo")
                    print("\n")

            if entrada == 3:
                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                if is_disconnected_graph(v, e):
                    print(f"O grafo de ID={i-1} é Desconexo")
                    print("\n")
                else:
                    print(f"O grafo de ID={i-1} não é Conexo")
                    print("\n")

            if entrada == 4:
                id = int(input("Id do grafo a ser verificado: "))
                i, v, e =graph_specific_return(self.__json, id)

                if is_complete_graph(v, e):
                    print(f"O grafo de ID={i-1} é Completo")
                    print("\n")
                else:
                    print(f"O grafo de ID={i-1} não é Completo")
                    print("\n")

            if entrada == 5:
                print("Verificar os graus de um grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                print(graph.degrees_vertices(v, e))
                print("\n")
            if entrada == 6:
                print("Verificar os grau de um vertice específico do grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                vertice = input("Vertice a ser verificado: ")

                print(degree_vertice_input(e, vertice))
                print("\n")
            if entrada == 7:

                print("Verificar os vertice alcançaveis de um grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)
                vertice = input("Vertice a ser verificado: ")

                print(reachable_vertices_of_input(e, vertice))
                print("\n")

            if entrada == 8:
                print("Verificar os vertice inalcançaveis de um grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e =graph_specific_return(self.__json, id)

                vertice = input("Vertice a ser verificado: ")

                print(vertices_unreachable_of_input(e, vertice))
                print("\n")
                return
            if entrada == 9:
                print("Algoritmo BFS em um grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                verticeInitial = input("vertice de partida: ")
                verticeFinal = input("vertice de chegada: ")

                print(bfs_graph(e, v, verticeInitial, verticeFinal))
                print("\n")
                return
            if entrada == 10:
                print("Algoritmo DFS um grafo")

                id = int(input("Id do grafo a ser verificado: "))
                i, v, e = graph_specific_return(self.__json, id)

                verticeInitial = input("vertice de partida: ")
                verticeFinal = input("vertice de chegada: ")

                print(dfs(e, verticeInitial, verticeFinal))
                print("\n")
            if entrada == 11:
                print("Até mais!")
                return False
        except KeyboardInterrupt:
            print("Programa encerrado de forma incorreta")
        except InterruptedError:
            print("Entrada Inválida")
        