class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []
        

    def push(self, val: int) -> None:
        if len(self.vals) == 0:
            self.mins.append(0)
        elif val < self.vals[self.mins[-1]]:
            self.mins.append(len(self.vals))
        self.vals.append(val)
        

    def pop(self) -> None:
        if len(self.vals) == 0:
            return None
        
        last_min = self.mins[-1]
        if last_min == len(self.vals) - 1:
            self.mins.pop()
        
        self.vals.pop()
        

    def top(self) -> int:
        if len(self.vals) == 0:
            return None
        else:
            return self.vals[-1]
        

    def getMin(self) -> int:
        return self.vals[self.mins[-1]]
        
