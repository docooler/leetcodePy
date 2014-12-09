class MinStack:
    def __init__(self):
        self.stack=[]
        self.min = None
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min is None or self.min > x:
            self.min = x
        return x
        

    # @return nothing
    def pop(self):
        x=self.stack.pop()
        if x is self.min:
            self.min = self.__getMin__()
        return x
            
    def __getMin__(self):
        if len(self.stack) == 0:
            return None
        min = self.stack[0]
        for x in self.stack:
            if x < min:
                min = x
        return min

    # @return an integer
    def top(self):
        if len(self.stack) == 0 :
            return None
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.min
        
