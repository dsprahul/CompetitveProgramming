class MinStack:

    def __init__(self):
        self.min = float("inf")    
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if val <= self.min:
            self.min_stack.append(val)
            self.min = val
        self.stack.append(val)
        

    def pop(self) -> None:
        print(self.min_stack)
        dropped = self.stack.pop()
        if dropped == self.min:
            self.min_stack.pop()
            if len(self.min_stack):
                self.min = self.min_stack[-1]
            else:
                self.min = float("inf")
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()