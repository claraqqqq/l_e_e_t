# Min Stack
# Design a stack that supports push, pop, top, 
# and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
# @param x, an integer

    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x):
        stock_len = len(self.stack)
        if stock_len == 0:
            self.min_stack.append(x)
        else:
            min_val = self.min_stack[-1]
            if x <= min_val:
                self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        if len(self.stack) > 0:
            tmp = self.stack.pop()
        if tmp == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]