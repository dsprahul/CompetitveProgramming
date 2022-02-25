class MyQueue:

    def __init__(self):
        self.stack = []
        self.holder = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack):
            self.holder.append(self.stack.pop())
            
        popped = self.holder.pop()
        
        while len(self.holder):
            self.stack.append(self.holder.pop())
            
        return popped

    def peek(self) -> int:
        while len(self.stack):
            self.holder.append(self.stack.pop())
            
        peeked = self.holder[-1]
        
        while len(self.holder):
            self.stack.append(self.holder.pop())
            
        return peeked

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()