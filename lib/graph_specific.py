import graph_model as gm
def graph_specific_return(data, parms):
        json_file = gm.JsonToDict(data)
        graph = json_file.json_to_graph()["graphs"]
        id = graph[parms]["id"]
        vertices = graph[parms]["vertices"]
        edges = graph[parms]["edges"]
        return id, vertices, edges