# Copy over the implementation of StateMachine from Cohort
from abc import ABC, abstractmethod


class StateMachine(ABC):
    def start(self):
        self.state = self.start_state
        pass

    def step(self, inp):
        # compute next state and output
        next_state, output = self.get_next_values(self.state, inp)
        # update current state
        self.state = next_state
        return output

    def transduce(self, inp_list):
        output = []
        # restart the machine
        self.start()
        # loop through the inputs
        for i in range(0, len(inp_list)):
            # check if "game over"
            if (self.is_done()):
                break
            # else continue running the input
            current_input = inp_list[i]
            current_output = self.step(current_input)
            output.append(current_output)

        return output

    @abstractmethod
    def get_next_values(self, state, inp):
        pass

    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)


class CommentsSM():
    """
    3 states for get_next_values:
    1 - take in: Collect the string
    2 - Don't: Return None
    """
    start_state = 2

    def __init__(self):
        self._state = self.start_state

    def get_next_values(self, state, inp):
        if state == 1:
            if inp == '\n':
                self._state = 2
                return [None]
            else:
                return [inp]
        elif state == 2:
            if inp == '#':
                self._state = 1
                return ['#']
            else:
                return [None]

    def transduce(self, inp):
        outputList = []
        for i in inp:
            outputList += self.get_next_values(self._state, i)
        return outputList


inpstr = "def func(x): # comment\n    return 1"
m = CommentsSM()
out = m.transduce(inpstr)
print(out)
assert out == [
    None, None, None, None, None, None, None, None, None, None, None, None,
    None, "#", " ", "c", "o", "m", "m", "e", "n", "t", None, None, None, None,
    None, None, None, None, None, None, None, None, None
]
