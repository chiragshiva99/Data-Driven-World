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


class Graph:
    def __init__(self):
        self.vertices = {}

    def _create_vertex(self, id):
        return Vertex(id)

    def add_vertex(self, id):
        v = self._create_vertex(id)
        self.vertices[v.id] = v

    def get_vertex(self, id):
        return self.vertices.get(id, None)

    def add_edge(self, start_v, end_v, weight=0):
        if start_v not in self.vertices.keys():
            self.add_vertex(start_v)
        start_vertex = self.vertices[start_v]
        if end_v not in self.vertices.keys():
            self.add_vertex(end_v)
        end_vertex = self.vertices[end_v]
        start_vertex.add_neighbour(end_vertex, weight)

    def get_neighbours(self, id):
        v = self.get_vertex(id)
        if v is not None:
            neighbours = v.get_neighbours()
            neighbours_id = []
            for neighbouring_vertex in neighbours:
                neighbours_id.append(neighbouring_vertex.id)
            return neighbours_id
        return None

    def __contains__(self, v_id):
        return v_id in self.vertices.keys()

    def __iter__(self):
        for k, v in self.vertices.items():
            yield v

    @property
    def num_vertices(self):
        return len(self.vertices)


g = Graph()
assert g.vertices == {} and g.num_vertices == 0
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
assert g.num_vertices == 6
assert "A" in g
assert "B" in g
assert "C" in g
assert "D" in g
assert "E" in g
assert "F" in g
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "C")
g.add_edge("E", "F")
g.add_edge("F", "C")
assert sorted(g.get_neighbours("A")) == ["B", "C"]
assert sorted(g.get_neighbours("B")) == ["C", "D"]
assert sorted(g.get_neighbours("C")) == ["D"]
assert [v.id for v in g] == ["A", "B", "C", "D", "E", "F"]