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

    def __eq__(self, other):
        print("equal method is called")
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        print("hash method is called ", self.id)
        return hash(self.id)

    def __str__(self):
        return "Vertex {self.id} is connected to: ".format(
            self=self) + ", ".join([x.id for x in self.get_neighbours()])


# Copy VertexSearch class from Cohort

import sys


class VertexSearch(Vertex):
    def __init__(self, id=""):
        super().__init__(id)
        self.colour = "white"
        self.d = sys.maxsize
        self._f = sys.maxsize
        self._parent = None

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value


#Copy Graph over from Cohort


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


#Copy over GraphSearch from Homework


class GraphSearch(Graph):
    def _create_vertex(self, id):
        return VertexSearch(id)


#Copy Queue over from Wk4 Homework


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.__items == []:
            return None
        else:
            return self.__items.pop(0)

    def peek(self):
        if len(self.__items) >= 1:
            return self.__items[0]

    # @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)


import sys


class Search2D:
    def __init__(self, g):
        self.graph = g

    def clear_vertices(self):
        for vid, vertex in self.graph.vertices.items():
            vertex.colour = "white"
            vertex.d = sys.maxsize
            vertex.f = sys.maxsize
            vertex.parent = None

    def __iter__(self):
        return iter([v for v in self.graph])

    def __len__(self):
        return len([v for v in self.graph.vertices])


g2 = GraphSearch()
g2.add_vertex("Z")
assert (type(g2.vertices["Z"]) == type(VertexSearch()))
