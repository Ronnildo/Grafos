from functions.is_multigraph.is_multigraph import is_multigraph
from functions.is_pseudograph.is_pseudograph import is_pseudograph


# Verifica se o grafo é completo
def is_complete_graph(vertices, edges):

    calc_edge = (len(vertices) ** 2) - len(vertices)
    # print(calc_edge)
    if is_multigraph(edges):
        return False
    elif is_pseudograph(edges):
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