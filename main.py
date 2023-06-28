#!/usr/bin/env python3
import graph as gi
from lib.menu import menu_inicial
from lib.statement import Chamada

if __name__ == "__main__":
    
    print("-------------------------")
    print("*   Teoria dos Grafos   *")
    print("-------------------------")
    print("1º Vamos carregar o arquivo JSON\n")
    try:
        # input do arquivo
        data = input("Digite o nome do arquivo sem o .json: ")
        print("\n")
        if data.isnumeric():
            print("Entrada inválida\n")
            data = input("Digite o nome do arquivo sem o .json: ")
    except KeyboardInterrupt:
        print("\n")
        print("Entrada não informada")
        exit(1)

    # Chamada de função que faz a desserialização JSON
   # graph = gi.Graph(f"{data}.json")

    menu_inicial()
    print("\n")
    op = int(input("Selecione a opção que deseja prosseguir: "))
    print("\n")
    execute = Chamada(f"{data}.json")
    execute.verify_op(op)
    # print("\n")
    # multigrafh, pseudograph, completegraph, desconex = graph.graph_check()

    # print(f"É multigrafo: {multigrafh}")
    # print(f"É pseudografo: {pseudograph}")
    # print(f"É desconexo: {desconex}")
    # print(f"É grafo completo: {completegraph}")

    # graus = graph.graus_vertices()
    # print(f"Grau dos Vértices do id=1: {graus}")

    # a_grau = graph.degree_vertice_input("A")
    # print(f"Grau do Vértice A do id=1: {a_grau}")

    # vertice_a = graph.reachable_vertices_of_A(1, "A")
    # print(f"Vértices alcançavéis de A: {vertice_a}")
    
    # vertice_ina = graph.vertices_unreachable_of_A(1, "A")
    # print(f"Vértices inalcançavéis de A: {vertice_ina}")
    # print(graph.bfs_graph("A", "BV"))

    # print(graph.dfs("A", "H"))
