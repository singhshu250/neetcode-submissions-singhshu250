class MinStack:

    # Two Stack

    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minStack:
    #         self.minStack.append(val)
    #     else:
    #         self.minStack.append(min(self.minStack[-1], val))
        

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()

        

    # def top(self) -> int:
    #     return self.stack[-1]
        

    # def getMin(self) -> int:
    #     return self.minStack[-1]

    #--------------------------------------------------------------
    # One Stack

    def __init__(self):
        self.stack = []
        self.m = 0
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.m=val
        else:
            self.stack.append(val-self.m)
            self.m = min(self.m,val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0 :
            self.m = self.m - val

        

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.m
        else:
            return self.m
        

    def getMin(self) -> int:
        return self.m
        
