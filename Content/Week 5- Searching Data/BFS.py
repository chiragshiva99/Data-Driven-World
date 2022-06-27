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


class Queue:
    ###BEGIN SOLUTION
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    ###END SOLUTION
    pass


class SearchBFS(Search2D):

    # this is BFS algorithm
    # @args: start --> String, id of vertex to start from
    def search_from(self, start):
        ###BEGIN SOLUTION
        # performing BFS algorithm, from start Vertex
        # 1. check if start vertex exist in the Graph
        start_vertex = self.graph.get_vertex(start)
        if start_vertex is None:
            return None

        # clear everything
        self.clear_vertices()

        # prepare the start_vertex
        start_vertex.d = 0

        # 2. Instantiate a Queue to be used for BFS
        vertices_to_explore_queue = Queue()
        vertices_to_explore_queue.enqueue(start_vertex)

        # 3. Keep adding neighbours of currently explored vertex to the Queue
        # until no more vertices can be explored (queue is empty)
        while not vertices_to_explore_queue.is_empty():
            # print([v.id for v in vertices_to_explore_queue.items])
            current_vertex_explored = vertices_to_explore_queue.dequeue()
            # update the color of this current vertex, "black" represents "explored"
            current_vertex_explored.colour = "black"

            # get all its neighbours
            # get_neighbours returns the vertex instances in RANDOM order
            # relying on keys() default method in python dict

            for current_vertex_neighbour in current_vertex_explored.get_neighbours(
            ):
                # add it the queue if it is not explored before AND has no "parent"
                if current_vertex_neighbour.colour == "white" and current_vertex_neighbour.parent is None:
                    # update the parent
                    current_vertex_neighbour.parent = current_vertex_explored
                    # update the distance to this neighbour so far
                    # this assumes that the weight for the edge is one
                    current_vertex_neighbour.d = current_vertex_explored.d + 1  # can be changed to edge weight between current v to neighbour v
                    # print("current vertex is ", current_vertex_explored.id, " and vertex ", current_vertex_neighbour.id , " is not yet explored.")
                    # print("distance from parent: ", current_vertex_neighbour.d, " parent's current distance: ", current_vertex_explored.d)
                    # add it the queue
                    vertices_to_explore_queue.enqueue(current_vertex_neighbour)

        ###END SOLUTION

    def get_shortest_path(self, start, dest):
        result = []
        self.get_path(start, dest, result)
        if result == []:
            return None  # this clause is only true when start, OR dest vertex does NOT exist in G
        else:
            return result
            # result can be "No Path", which means start AND dest vertex exist in G but they are not connected

    # We need to call search_from once, then after it returns,
    # the .colours, .d, and .parent of each VertexSearch instance
    # in self.graph will be "set"
    # If we want to get "path", we need to start at the dest Vertex
    # then, repeatedly "backtrack" the parent
    # @args: start, dest is the id of Start, end vertex
    # result: a list containing paths -> ids of Vertex from Start to End
    def get_path(self, start, dest, result):
        ###BEGIN SOLUTION
        # check if start, dest exist in graph
        start_vertex = self.graph.get_vertex(start)
        if start_vertex is None:
            return None

        end_vertex = self.graph.get_vertex(dest)
        if end_vertex is None:
            return None

        # if you reach here, both vertices exist
        # just because both vertices exist, doesn't mean they're connected
        # run BFS to find out, this method runs BFS until there's no Vertex unexplored in G
        # it doesn't always stop at dest
        # this means that this method can be used to compute path from Start to end_i,
        # where end_i is any vertex in G.

        # do not call BFS again to save time, when it's been called before
        if start_vertex.d != 0:
            self.search_from(start)

        print(start_vertex.id, end_vertex.id)
        # this check is done AFTER BFS is run because we can't assume that
        # the question does not run BFS at all if start == dest
        if (start == dest):  # if the inputs are the same Vertex
            result.append(start)
        elif end_vertex.parent is None:
            # start_vertex to end_vertex is NOT connected
            result.append("No Path")
        else:
            # recursive call
            # BFS is done, update the end-vertex to be the "parent of the original end vertex"
            self.get_path(start, end_vertex.parent.id, result)
            result.append(dest)

        # example:
        # A -> B -> C -> D
        # result = []

        # 1st call of get_path(A, D, result):
        #     do BFS starting from A
        #     end_vertex = D, parent is C
        #     go to else-clause and recurse
        #     result = [... , D]
        # 2nd call of get_path(A, C, result):
        #     end_vertex = C, parent is B
        #     go to else-clause and recurse
        #     result = [... , C, ...]
        # 3rd call of get_path(A, B, result):
        #     end_vertex = B, parent is A
        #     go to else-clause and recurse
        #     result = [..., B, ...]
        # 4th call of get_path(A, A, result):
        #     end-vertex = A, parent is None
        #     go to if-clause, no recurse
        #     result = [A, ...]

        ###END SOLUTION
        pass


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
gs4 = SearchBFS(g4)

gs4.search_from("A")
assert gs4.graph.get_vertex("A").d == 0
assert gs4.graph.get_vertex("A").colour == "black"
assert gs4.graph.get_vertex("A").parent == None
assert gs4.graph.get_vertex("B").d == 1
assert gs4.graph.get_vertex("B").colour == "black"
assert gs4.graph.get_vertex("B").parent == gs4.graph.get_vertex("A")

print(gs4.graph.get_vertex("C").d)
assert gs4.graph.get_vertex("C").d == 1
assert gs4.graph.get_vertex("C").colour == "black"
assert gs4.graph.get_vertex("C").parent == gs4.graph.get_vertex("A")
assert gs4.graph.get_vertex("D").d == 2
assert gs4.graph.get_vertex("D").colour == "black"
gs4.graph.get_vertex("D").parent
#assert gs4.graph.get_vertex("D").parent == gs4.graph.get_vertex("B")
ans = gs4.get_shortest_path("A", "D")
assert ans == ["A", "B", "D"]
ans = gs4.get_shortest_path("E", "D")
# print(ans)
assert ans == ["E", "F", "C", "D"]