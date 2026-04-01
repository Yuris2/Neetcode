class MinStack:

    def __init__(self):
        self.stack = []
        #Certain index showcases the min val at a stack
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #Comparing the value in the minStack
        if self.minStack:
            #Is the current value smaller than the smallest index
            val = min(val, self.minStack[-1])
        
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
