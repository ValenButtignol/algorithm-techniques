class UnirectedUnweightedGraph:
    def __init__(self):
        self.nodes = {}

    def add_vertex(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)
        
    def get_vertices(self):
        return list(self.nodes.keys())

    def get_adyacents(self, node):
        return self.nodes[node]

    def show_connections(self):
        for node in self.nodes:
            connections = " ".join([str(n) for n in self.nodes[node]])
            print(f"{node} --> {connections}")

