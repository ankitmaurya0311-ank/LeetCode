class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack :
            self.min_stack.append(value)
        else :
            current_value = self.min_stack[-1]
            self.min_stack.append(min(value,current_value))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
           
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()