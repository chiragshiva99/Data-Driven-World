class Stack:
    def __init__(self):
        self.__items = []  # name mangling

    def push(self, item):
        ###BEGIN SOLUTION
        self.__items.append(item)
        ###END SOLUTION
        pass

    def pop(self):
        ###BEGIN SOLUTION
        if len(self.__items) >= 1:
            return self.__items.pop()
        ###END SOLUTION
        pass

    def peek(self):
        ###BEGIN SOLUTION
        if len(self.__items) >= 1:
            return self.__items[-1]
        ###END SOLUTION
        pass

    @property
    def is_empty(self):
        ###BEGIN SOLUTION
        return len(self.__items) == 0
        ###END SOLUTION
        pass

    @property
    def items(self):
        return self.__items

    @property
    def size(self):
        ###BEGIN SOLUTION
        return len(self.__items)
        ###END SOLUTION
        pass


class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    ###BEGIN SOLUTION
    def enqueue(self, item):
        self.right_stack.push(item)

    def dequeue(self):
        # if left_stack is empty, need to pop the right stack, and push it to the left
        # Pop from the left_stack
        if self.left_stack.is_empty:
            # fill the left stack
            while not self.right_stack.is_empty:
                item = self.right_stack.pop()
                self.left_stack.push(item)

        return self.left_stack.pop()

    def peek(self):
        # if left_stack is empty, then the first item in the queue is
        # the BASE of the right_stack
        # else, peek from the left_stack
        if self.left_stack.is_empty:
            if not self.right_stack.is_empty:
                return self.right_stack.items[0]  # the base of the stack
                # which is the first item added to the right stack (first in)
        else:
            return self.left_stack.peek()

    @property
    def is_empty(self):
        return self.left_stack.is_empty and self.right_stack.is_empty

    @property
    def size(self):
        return self.left_stack.size + self.right_stack.size

    ###END SOLUTION


q1 = Queue()
q1.enqueue(2)
assert not q1.is_empty
assert q1.size == 1
x = q1.dequeue()
print("x", x)
assert x == 2
assert q1.is_empty
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
assert q1.size == 3
assert q1.peek() == 1
assert q1.dequeue() == 1
assert q1.dequeue() == 2
assert q1.dequeue() == 3
assert q1.peek() == None