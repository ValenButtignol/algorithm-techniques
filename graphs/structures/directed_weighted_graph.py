class DirectedWeightedGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []


    def add_vertex(self, vertex):
        from structures.vertex import Vertex

        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False


    def add_edge(self, vertex1, vertex2, cost=0):
        from structures.edge import Edge

        if vertex1.name in self.vertices and vertex2.name in self.vertices:
            self.edges.append(Edge(vertex1, vertex2, cost))
            return True
        else:
            return False
        
        
    def get_vertices(self):
        return list(self.vertices.values())
    

    def get_first_vertex(self):
        return self.get_vertices()[0]
    

    def unmark_all(self):
        for vertex in self.get_vertices():
            vertex.unmark()
    

    def get_adyacents(self, vertex):
        from structures.vertex import Vertex
        if not isinstance(vertex, Vertex) or vertex.name not in self.vertices:
            return None
        
        edges = []
        for edge in self.edges:
            if edge.vertex1 == vertex:
                edges.append(edge.vertex2)
                
        return edges


    def show_connections(self):
        for edge in self.edges:
            print(edge)