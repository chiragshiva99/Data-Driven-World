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
            return self.__items.pop(
            )  #.pop() always removes the last element added into the stack
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


class EvaluatePostfix:

    operands = "0123456789"
    operators = "+-*/"

    def __init__(self):
        self.expression = []
        self.stack = Stack()

    # what is this function for?
    # what are the arguments and their type?
    # item (string, but must be converted either
    # into a number - int, or mathematical sign)
    # what are the return value(s) if any?
    # None
    def input(self, item):
        ###BEGIN SOLUTION
        # store the input by inserting it at the front of the list
        self.expression.insert(0, item)  #insert a new item at dict[0]
        ###END SOLUTION
        pass

    def evaluate(self):
        # take out the item one by one from expression list (from the back)
        # push it to the stack (reversed)
        # process the item (operands or operator)
        # compute the result

        # the stack contains always at MOST two integers at any point in time
        # when expressions are all processed, the stack contains ONE item only
        # which is the result
        while len(self.expression) != 0:
            # example
            # 11, 12, +, 6, * --> actual input
            # *, 6, +, 12, 11 --> in expression list
            item = self.expression.pop()  # take out the back of the list
            # check whether it is an operator
            if item.isdigit():
                self.stack.push(int(item))  # push it to the stack
            elif len(
                    item
            ) == 1 and item in EvaluatePostfix.operators:  # for the + - * and /
                # take out last two operands from the stack
                # this assumes we have 2 numbers in the stack
                # whenever we encounter the operator
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                # compute the result
                # item is a string,
                # op1, op2 are integers
                result = self.process_operator(op1, op2, item)
                self.stack.push(result)

        return self.stack.pop()
        ###BEGIN SOLUTION
        ###END SOLUTION

    # custom helper function
    def process_operator(self, op1, op2, op):
        ###BEGIN SOLUTION
        if op == "+":
            return op2 + op1
        elif op == "-":
            return op2 - op1
        elif op == "*":
            return op2 * op1
        elif op == "/":
            return op2 / op1
        else:
            return 0.0


pe = EvaluatePostfix()
pe.input("2")
pe.input("3")
pe.input("+")
pe.input("6")
pe.input("*")
print(pe.evaluate())