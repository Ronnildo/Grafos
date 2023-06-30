#!/usr/bin/env python3
import sys
import graph as gi
from lib.menu import menu_inicial
from lib.statement import ExecuteGraph

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

    print("\n")
    execute = ExecuteGraph(f"{data}.json")
    while True:
        menu_inicial()
        print("\n")
        try:
            op = int(input("Selecione a opção que deseja prosseguir: "))
            print("\n")
            execute.verify_op(op)
        except KeyboardInterrupt:
            print("Programa encerrado")
            sys.exit()
        except ValueError:
            print("Digite um valor interiro!")
