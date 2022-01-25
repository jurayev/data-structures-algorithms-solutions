class Item:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

class MinStack:
    """
    min() Time -> O(N) -> O(1)
    Overall Space -> O(N)
    [(1,1), (2,1), (0, 0)] 
      v m
    push -> 1
    min -> 1
    top -> 1
    
    push -> 2
    min -> 1
    top -> 2
    
    push -> 0
    min -> 0
    top -> 0
    """

    def __init__(self):
        self.stack = [Item(0, float("inf"))]

    def push(self, val: int) -> None:
        item = Item(val, min(val, self.stack[-1].min_value))
        self.stack.append(item)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()