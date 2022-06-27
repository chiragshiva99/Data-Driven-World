# Copy over the implementations of Queue from PS4 HW2
class Queue:
    pass
    ###BEGIN SOLUTION
    def __init__(self):
        self.items = []
  
    @property
    def is_empty(self):
        return len(self.items) == 0
  
    @property
    def size(self):
        return len(self.items)
  
    def enqueue(self, item):
        self.items.insert(0, item)
  
    def dequeue(self):
        return self.items.pop()
  
    def peek(self):
        return self.items[-1]
    ###END SOLUTION


# Copy over the implementation of StateSpaceSearch from Cohort
from abc import ABC, abstractmethod

class StateMachine(ABC):
    # start_state is in the child class
    def start(self):
        self.state = self.start_state

    # step() is not a pure function
    # because it modifies variables outside of this function
    # and relies on this variable outside for computation
    # rather than just "inp" (its input)
    # that variable is self.state
    # this causes step to  return DIFFERENT output possibly, with the same inp
    def step(self, inp): 
        # get new state, and output from the transition logic 
        new_state, output = self.get_next_values(self.state, inp)
        # set current state as next state (update state)
        self.state = new_state
        return output
        
    # run steps through the series of input from the start
    def transduce(self, inp_list):
        output = []
        self.start() # dont forget to start
        for i in range(0, len(inp_list)):
            # check if state machine lands on final state
            if (self.is_done()):
                break
            else:
                # continue if it is not game over yet
                current_input = inp_list[i]
                current_output = self.step(current_input)
                output.append(current_output)
        return output

    @abstractmethod
    def get_next_values(self, state, inp):
        pass

    # should be overriden when necessary
    # thats why this is not made an abstract method
    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)

    

class StateSpaceSearch(StateMachine):
    @property
    @abstractmethod
    def statemap(self):
        pass

    @property
    @abstractmethod
    def legal_inputs(self):
        pass


# Copy over the implementation of MapSM from Cohort
class MapSM(StateSpaceSearch):
    
    def __init__(self, start):
        self.start_state = start
        
    @property
    def statemap(self):
        statemap = {"S": ["A", "B"],
                    "A": ["S", "C", "D"],
                    "B": ["S", "D", "E"],
                    "C": ["A", "F"],
                    "D": ["A", "B", "F", "H"],
                    "E": ["B", "H"],
                    "F": ["C", "D", "G"],
                    "H": ["D", "E", "G"],
                    "G": ["F", "H"]}
        return statemap

    @property
    def legal_inputs(self):
        ###BEGIN SOLUTION
        maxsofar = -1
        for state, neighbours in self.statemap.items():
            count = len(neighbours)
            if count > maxsofar:
                maxsofar = count
        return set(range(maxsofar))
        ###END SOLUTION
        pass
  
    def get_next_values(self, state, inp):
        ###BEGIN SOLUTION
        neighbours = self.statemap.get(state, None)
        if neighbours != None and inp < len(neighbours):
            next_state = neighbours[inp]
            return next_state, next_state
        else:
            return state, state 
        ###END SOLUTION

# Copy over the implementations of Step and SearchNode from Cohort
class Step:
    def __init__(self, action, state):
        self.action = action
        self.state = state
    
    def __eq__(self, other):
        return self.action == other.action and self.state == other.state
  
    def __str__(self):
        return f"action: {self.action:}, state: {self.state:}"

class SearchNode:
    pass
    ###BEGIN SOLUTION
    def __init__(self, action, state, parent):
        self.action = action
        self.state = state
        self.parent = parent
  
    def path(self):
        if self.parent == None:
            return [Step(self.action, self.state)]
        else:
            return self.parent.path() + [Step(self.action, self.state)]
  
    def in_path(self, state):
        if self.state == state:
            return True
        elif self.parent == None:
            return False
        else:
            return self.parent.in_path(state)
  
    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return self.state == other.state and self.parent == other.parent and \
                   self.action == other.action
    ###END SOLUTION


# @args:
# sm_to_search: MapSM instance 
# initial_state: string 
# goal_test: function used to test whether we are in the goal state
# @return:
# a list of Step instances, from Start state to Goal state

def sm_search(sm_to_search, initial_state=None, goal_test=None):
    # check if initial_state is provided
    # if it is, use it
    # otherwise, get the start state of sm_to_search
    
    init_state = initial_state
    if initial_state == None:
        # replace None to take the start state of sm_to_search
        ###BEGIN SOLUTION
        init_state = sm_to_search.start_state
        ###END SOLUTION

  
    # check if goal_test is provided
    # if it is, use it
    # otherwise, use the done method as the goal function
    # taken from sm_to_search
    goal_func = goal_test
    if goal_test == None:
        goal_func = sm_to_search.done # the done function in StateMachine

    # do BFS
    # create a Queue instance to store the node to explore
    # replace the None below
    bfs_queue = Queue()
  
    # if the initial state is the goal state, 
    # then we are done and exit
    if goal_func(init_state): # at first, we are comparing "S" == "H" ->> false 
        return [Step(None, init_state)]
  
    # otherwise, add the current node into the agenda 
    # start BFS from the root 
    # we create a SearchNode instance, with 
    # state as init_state
    # initially, we have SearchNode(None,"S",None)
    bfs_queue.enqueue(SearchNode(None, init_state, None))
    
    # explore as long as the Queue is not empty
    while not bfs_queue.is_empty:
        
        # replace None to take out the parent from the Queue
        ###BEGIN SOLUTION
        # initially, we have parent -> SearchNode(None,"S",None)
        current_node = bfs_queue.dequeue()
        ###END SOLUTION
        
        # create a list to keep track which child state have been explored
        neighbours_list = []
        
        # get all the legal input values
        actions = sm_to_search.legal_inputs
        
        #iterate over all legal inputs
        for a in actions:
            # get the next possible state using the current action
            # call get_next_values to get the next state
            ###BEGIN SOLUTION
            # get next values returns a tuple (next state, output)
            # so just get the FIRST one
            # next_state is a string 
            next_state = sm_to_search.get_next_values(current_node.state, a)[0]
            ###END SOLUTION
            
            # create a new search node from the new_s
            ###BEGIN SOLUTION
            next_state_searchnode = SearchNode(a, next_state, current_node)
            ###END SOLUTION
            
            # if the next state is the goal state, then we exit and return the path
            if goal_func(next_state):
                return next_state_searchnode.path()
            
            # do not explore anymore states that have already been explored, or ABOUT to be explored (and is already in the queue)
            # if the next state is already in the list of new child state, ignore it
            elif next_state in neighbours_list:
                pass
            
            # if the new state is in the path of the current node, ignore it
            elif current_node.in_path(next_state):
                pass
            
            # otherwise, add the new state into the list
            # and the new node into the Queue
            else:
                # step 1. add the new state into the new_child_state
                ###BEGIN SOLUTION
                neighbours_list.append(next_state)
                ###END SOLUTION
                
                # step 2. add the new node into the Queue
                ###BEGIN SOLUTION
                bfs_queue.enqueue(next_state_searchnode)
                ###END SOLUTION
                pass
    return None


mapSM = MapSM("S")
ans = sm_search(mapSM , "S" , lambda s: s=="H" )
print(ans)
steps = [(step.action, step.state) for step in ans]
assert steps == [(None, "S"), (0, "A"), (2, "D"), (3, "H")]
for step in ans:
    print(step)