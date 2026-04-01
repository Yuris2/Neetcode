class MinStack:
# initialize the stack and minStack
# minimum will always be at top of minStack
# append val to stack
# redefine val to be the current minimum
# find the current min between the val and top of minStack
# make sure the minimum function is calling a non-empty minStack
# the min result is pushed to the minStack

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
   
    def getMin(self) -> int:
        return self.minStack[-1]
