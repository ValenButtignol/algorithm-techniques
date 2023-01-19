
# Assume we use Directed Weighted Graph for simplicity.
def recursive_dfs(graph):
    graph.unmark_all()
    path = []
    r_dfs(graph, graph.get_first_vertex(), path)
    return path

def r_dfs(graph, vertex, path=[]):
    vertex.mark()
    path.append(vertex)
    for adyacent in graph.get_adyacents(vertex):
        if not adyacent.marked:
            r_dfs(graph, adyacent, path)
    return  # Isn't necesary to return the path, we override it on each recursive call.


def iterative_dfs(graph):
    graph.unmark_all()
    stack = []
    path = []
    first = graph.get_first_vertex()
    stack.append(first)
    first.mark()
    while stack:
        current = stack.pop()
        current.mark()
        path.append(current)    #Process
        for adyacent in graph.get_adyacents(current):
            if not adyacent.marked:
                stack.append(adyacent)
        
    return path