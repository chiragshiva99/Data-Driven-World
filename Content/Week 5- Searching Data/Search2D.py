class Vertex:
    def __init__(self, id=""):
        self.id = id  # String
        self.neighbours = {}  # Dictionary e.g: {Vi_instance: 1, Vj_instance:3}

    # @args:
    #   nbr_vertex: vertex instance
    #   weight: Int
    def add_neighbour(self, nbr_vertex, weight=0):
        ###BEGIN SOLUTION
        # adding items to the dictionary neighbours
        # nbr_vertex's __hash__ method is called
        # in dictionary: elements are UNORDERED
        # there should be a way for Python to know if the KEY exists in the dict or not
        # if it exists: replace the value with the new value
        # else: create a new dict entry
        # if Python naively LOOP through all elements in the dict and compare the existing key with given key : O(n*e) where e is the length of the key
        # d = {"apple is great": 3, "banana is yellow": 4, "cherry is red":9, ...}
        # d["apple is great "] = 6
        # hash() is used to quickly compare between two values FAST

        self.neighbours[
            nbr_vertex] = weight  # check if hash(nbr_vertex) exists as key in the dictionary

        ###END SOLUTION
        pass

    def get_neighbours(self):
        ###BEGIN SOLUTION
        return list(self.neighbours.keys())
        ###END SOLUTION
        pass

    # @args:
    #   neighbour: Vertex instance
    # @return:
    #   weight: Int
    def get_weight(self, neighbour):
        ###BEGIN SOLUTION
        return self.neighbours.get(neighbour,
                                   None)  #get neighbours weight or none
        ###END SOLUTION
        pass

    # @args:
    #   other: Vertex instance
    def __eq__(self, other):
        print("equal method is called")
        ###BEGIN SOLUTION
        return self.id == other.id
        ###END SOLUTION
        pass

    # @args:
    #   other: Vertex instance
    def __lt__(self, other):
        ###BEGIN SOLUTION
        return self.id < other.id
        ###END SOLUTION
        pass

    # this overrides the default __hash__ of Python object that uses the "memory location" of the instance as the hashable item
    def __hash__(self):
        print("hash method is called ", self.id)
        ###BEGIN SOLUTION
        return hash(self.id)  # hashable items: immutable items
        ###END SOLUTION
        pass

    def __str__(self):
        ###BEGIN SOLUTION
        return "Vertex {self.id} is connected to: ".format(
            self=self) + ", ".join([x.id for x in self.get_neighbours()])
        ###END SOLUTION
        pass


class Graph:
    def __init__(self):
        self.vertices = {
        }  # Dictionary, key = String of Vertex id, value is the Vertex instance
        # to get the neighbours of a vertex in this graph: self.vertices[vid].neighbours

    # id: String
    # the leading underscore means it is used INTERNALLY in Graph class only
    # DO NOT DO THIS: instance._create_vertex
    def _create_vertex(self, id):
        ###BEGIN SOLUTION
        # create a new Vertex object and return it
        return Vertex(id)
        ###END SOLUTION
        pass

    def add_vertex(self, id):
        ###BEGIN SOLUTION
        # create a new Vertex object using _create_vertex
        self.vertices[id] = self._create_vertex(id)  #CALLING DICTIONARY
        # v = self._create_vertex(id)
        # # add it to this instance's vertices attribute
        # self.vertices[v.id] = v # composition
        ###END SOLUTION
        pass

    # return the instance of the requested id
    def get_vertex(self, id):
        ###BEGIN SOLUTION
        return self.vertices.get(id, None)
        ###END SOLUTION
        pass

    # creates an edge from one Vertex to another Vertex.
    # The arguments are the `id`s of the two vertices and are both Strings.
    # is there a guarantee that start_v and end_v exists in the Graph??
    # Nope
    # if the vertex with the id start_v or end_v doesnt exist, create it
    def add_edge(self, start_v, end_v, weight=0):
        ###BEGIN SOLUTION
        # check if start_v is in the graph's vertices dictionary
        if start_v not in self.vertices.keys():
            self.add_vertex(start_v)

        # obtain the instance of Vertex with id start_v
        start_vertex = self.vertices[start_v]

        # check if end_v is in the graph's vertices dictionary
        if end_v not in self.vertices.keys():
            self.add_vertex(end_v)

        # obtain the instance of Vertex with id end_v
        end_vertex = self.vertices[end_v]

        # utilising the add_neighbour method of the Vertex instance
        # the info about the "neighbour" exist in the Vertex instance with id start_v
        start_vertex.add_neighbour(end_vertex, weight)
        ###END SOLUTION
        pass

    # @args: id is the String of vertex in question
    # returns: ids of all neighbouring vertices
    def get_neighbours(self, id):
        ###BEGIN SOLUTION
        v = self.get_vertex(id)
        if v is not None:  # if v exists in the graph, get all its neighbours
            neighbours = v.get_neighbours(
            )  # utilising the get_neighbours method in Vertex class instance
            neighbours_id = []
            for neighbouring_vertex in neighbours:
                # neighbouring_vertex is a vertex instance, so extract its id
                neighbours_id.append(neighbouring_vertex.id)
            return neighbours_id
        return None
        ###END SOLUTION

    # returns True or False if given val (String representing Vertex id) is in the Graph
    def __contains__(self, v_id):
        ###BEGIN SOLUTION
        return (v_id in self.vertices.keys())  #MODIFIED
        #     return True
        # else:
        #     return False
        ###END SOLUTION
        pass

    def __iter__(self):
        for key, value in self.vertices.items():
            yield value

    # write a code to create a computed property called num_vertices
    ###BEGIN SOLUTION
    @property
    def num_vertices(self):
        return len(self.vertices)

    ###END SOLUTION


import sys


# VertexSearch INHERITS Vertex
# VertexSearch has all Vertex attributes and methods
class VertexSearch(Vertex):

    # override init method
    def __init__(self, id=""):
        ###BEGIN SOLUTION
        super().__init__(
            id
        )  # invoke the superclass (parent class) Vertex's INIT function so we have Vertex's attributes too in VertexSearch instance
        self.colour = "white"
        self.d = sys.maxsize  # biggest number in Python int
        self._f = sys.maxsize
        self._parent = None
        ##END SOLUTION
        pass

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


class GraphSearch(Graph):
    # overriding the _create_vertex method
    def _create_vertex(self, id):
        return VertexSearch(id)


import sys


class Search2D:
    def __init__(self, g):
        self.graph = g

    def clear_vertices(self):
        ###BEGIN SOLUTION
        # loop through the graph's vertices (dictionary)
        for vid, vertex in self.graph.vertices.items():
            # reset all the vertex color, d, f, and parent
            vertex.colour = "white"
            vertex.d = sys.maxsize
            vertex.f = sys.maxsize
            vertex.parent = None
        ###END SOLUTION
        pass

    def __iter__(self):
        return iter([v for v in self.graph])

    def __len__(self):
        return len([v for v in self.graph.vertices])


g4 = GraphSearch()
g4.add_vertex("A")
g4.add_vertex("B")
g4.add_vertex("C")
g4.add_vertex("D")
g4.add_vertex("E")
g4.add_vertex("F")
g4.add_edge("A", "B")
g4.add_edge("A", "C")
g4.add_edge("B", "C")
g4.add_edge("B", "D")
g4.add_edge("C", "D")
g4.add_edge("D", "C")
g4.add_edge("E", "F")
g4.add_edge("F", "C")
gs4 = Search2D(g4)
gs4.clear_vertices()

assert len(gs4) == 6
assert [v.id for v in gs4] == ["A", "B", "C", "D", "E", "F"]
assert [v.colour for v in gs4] == ["white" for v in range(len(gs4))]
assert [v.d for v in gs4] == [sys.maxsize for v in range(len(gs4))]
assert [v.f for v in gs4] == [sys.maxsize for v in range(len(gs4))]
assert [v.parent for v in gs4] == [None for v in range(len(gs4))]