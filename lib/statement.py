from graph import Graph
from lib.menu import menu_inicial, submenu

class Chamada:
    def __init__(self, json):
        self.__json = json 
    def verify_op(self, entrada):
        graph = Graph(self.__json)
        try:
            while True:
                # Is_Multigraph
                if entrada == 1: 
                    submenu(entrada)
                    op = int(input("Opção: "))
                    print("\n")
                    if op == 1:
                        id = int(input("Id do grafo a ser verificado: "))
                        i, v, e = graph.graph_specific_return(id)
                        
                        if graph.is_multigraph(e):
                            print(f"O grafo de ID={i} é Multigrafo")
                            print("\n")
                        else:
                            print(f"O grafo de ID={i} não é Multigrafo")
                            print("\n")
                        #print(f"O grafo de ID={i} é {graph.is_multigraph(e)}")
                    if op == 2:
                        todo = graph.graph_all_return()
                        mult = {}
                        for i in range(len(todo)):
                            mult[i+1] = graph.is_multigraph(todo[i]["edges"])
                        res = ("Todos os Grafos: True se é Multigrafo e Falso caso não seja:\n" f"{mult}")
                        print(res)
                        print("\n")
                        exit()
                    else:
                        print("Opção inválida")         
                if entrada == 2: 
                    submenu(entrada)
                    op = int(input("Opção: "))
                    print("\n")
                    if op == 1:
                        id = int(input("Id do grafo a ser verificado: "))
                        i, v, e = graph.graph_specific_return(id)
                        
                        if graph.is_pseudograph(e):
                            print(f"O grafo de ID={i-1} é Pseudografo")
                            print("\n")
                        else:
                            print(f"O grafo de ID={i-1} não é Pseudografo")
                            print("\n")
                        #print(f"O grafo de ID={i} é {graph.is_multigraph(e)}")
                    if op == 2:
                        todo = graph.graph_all_return()
                        mult = {}
                        for i in range(len(todo)):
                            mult[i+1] = graph.is_pseudograph(todo[i]["edges"])
                        res = ("Todos os Grafos: True se é Pseudografo e Falso caso não seja:\n" f"{mult}")
                        print(res)
                        print("\n")
                        exit()
                    else:
                        print("Opção inválida")
                if entrada == 3: 
                    submenu(entrada)
                    op = int(input("Opção: "))
                    print("\n")
                    if op == 1:
                        id = int(input("Id do grafo a ser verificado: "))
                        i, v, e = graph.graph_specific_return(id)
                        
                        if graph.is_disconnected_graph(v, e):
                            print(f"O grafo de ID={i} é Desconexo")
                            print("\n")
                        else:
                            print(f"O grafo de ID={i} não é Conexo")
                            print("\n")
                        #print(f"O grafo de ID={i} é {graph.is_multigraph(e)}")
                    if op == 2:
                        todo = graph.graph_all_return()
                        mult = {}
                        for i in range(len(todo)):
                            mult[i+1] = graph.is_disconnected_graph(todo[i]["vertices"], todo[i]["edges"])
                        res = ("Todos os Grafos: True se é Desconexo e Falso caso não seja:\n" f"{mult}")
                        
                        print(res)
                        print("\n")
                        exit()
                    else:
                        print("Opção inválida")
                if entrada == 4: 
                    submenu(entrada)
                    op = int(input("Opção: "))
                    print("\n")
                    if op == 1:
                        id = int(input("Id do grafo a ser verificado: "))
                        i, v, e = graph.graph_specific_return(id)

                        if graph.is_complete_graph(v, e):
                            print(f"O grafo de ID={i} é Completo")
                            print("\n")
                        else:
                            print(f"O grafo de ID={i} não é Completo")
                            print("\n")
                        #print(f"O grafo de ID={i} é {graph.is_multigraph(e)}")
                    if op == 2:
                        todo = graph.graph_all_return()
                        mult = {}
                        for i in range(len(todo)):
                            mult[i+1] = graph.is_complete_graph(todo[i]["vertices"],todo[i]["edges"])
                        res = ("Todos os Grafos: True se é Completo e Falso caso não seja:\n" f"{mult}")
                        print(res)
                        print("\n")
                        exit()
                    else:
                        print("Opção inválida")
                if entrada == 5: 
                    print("Verificar os graus de um grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    i, v, e = graph.graph_specific_return(id)

                    print(graph.degrees_vertices(v, e))
                    print("\n")
                if entrada == 6:
                    print("Verificar os grau de um vertice específico do grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    vertice = input("Vertice a ser verificado: ")

                    print(graph.degree_vertice_input(id, vertice))
                    print("\n")
                if entrada == 7: 
                    
                    print("Verificar os vertice alcançaveis de um grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    vertice = input("Vertice a ser verificado: ")

                    print(graph.reachable_vertices_of_input(id, vertice))
                    print("\n")

                if entrada == 8: 
                    print("Verificar os vertice inalcançaveis de um grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    vertice = input("Vertice a ser verificado: ")

                    print(graph.vertices_unreachable_of_input(id, vertice))
                    print("\n")
                if entrada == 9:
                    print("Algoritmo BFS em um grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    verticeInitial = input("vertice de partida: ")
                    verticeFinal = input("vertice de chegada: ")

                    print(graph.bfs_graph(id, verticeInitial, verticeFinal))
                    print("\n")
                if entrada == 10: 
                    print("Algoritmo DFS um grafo")
                    
                    id = int(input("Id do grafo a ser verificado: "))
                    verticeInitial = input("vertice de partida: ")
                    verticeFinal = input("vertice de chegada: ")

                    print(graph.dfs(id, verticeInitial, verticeFinal))
                    print("\n")
                if entrada == 11:
                    print("Até mais!")
                    return False
        except KeyboardInterrupt:
            print("Programa encerrado de forma incorreta")
        except InterruptedError:
            print("Entrada Inválida")
            
        #menu_inicial()