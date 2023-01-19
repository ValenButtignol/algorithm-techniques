class Edge:
    def __init__(self, vertex1, vertex2, cost):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.cost = cost
        
    def set_cost(self, new_cost):
        self.cost = new_cost
    
    def __repr__(self):
        return f"{self.vertex1} ---> {self.vertex2} ({self.cost})"