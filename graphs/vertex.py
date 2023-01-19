class Vertex:
    def __init__(self, name):
        self.name = name
        self.marked = False
        
    def mark(self):
        self.marked = True
        
    def unmark(self):
        self.marked = False
        
    def __repr__(self):
        return self.name