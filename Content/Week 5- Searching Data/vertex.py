class Vertex:
    def __init__(self, id=""):
        self.id = id
        self.neighbours = {}

    def add_neighbour(self, nbr_vertex, weight=0):
        self.neighbours[nbr_vertex] = weight

    def get_neighbours(self):
        return list(self.neighbours.keys())

    def get_weight(self, neighbour):
        return self.neighbours.get(neighbour, None)
        pass

    def __eq__(self, other):
        print("equal method is called")
        return self.id == other.id
        pass

    def __lt__(self, other):
        print("__it__ method is called")
        return self.id < other.id

    def __hash__(self):
        print("hash method is called ", self.id)
        return hash(self.id)

    def __str__(self):
        return "Vertex {self.id} is connected to: ".format(
            self=self) + ", ".join([x.id for x in self.get_neighbours()])


v1 = Vertex("1")
assert v1.id == "1" and len(v1.neighbours) == 0
v2 = Vertex("2")
v1.add_neighbour(v2)
assert v1.get_neighbours()[0].id == "2" and v1.neighbours[v1.get_neighbours()
                                                          [0]] == 0
v3 = Vertex("3")
v1.add_neighbour(v3, 3)
assert v1.get_weight(v3) == 3
v4 = Vertex("4")
assert v1.get_weight(v4) == None
assert v1 < v2
assert v1 != v2
assert str(v1) == "Vertex 1 is connected to: 2, 3"
