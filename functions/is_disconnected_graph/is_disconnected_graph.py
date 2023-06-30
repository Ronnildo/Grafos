# Função que verifica se um grafo é desconcexo 
def is_disconnected_graph(vertices, edges):
        '''para cada par s e t de seus vértices, existe um caminho com origem s e término t'''
        """ VERIFICAR SE CADA POSIÇÃO NA LISTA DE VÉRTICES ESTÁ CONTIDO NA LISTA DE ARESTAS"""

        # Para um grafo ser conexo é necessário que no minimo
        # a quantidade de arestas seja 2 vezes o número de vértices
        calc = len(vertices) * 2
        if len(edges) * 2 < calc:
            return True
        
        return False