class Item:
    def __init__(self, val, increment=0):
        self.val = val
        self.increment = increment
        
class CustomStack:
    """
    ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
    [[3],          [1],      [2],   [],   [2],   [3],   [4],    [5,100],    [2,100],   [],   [],   [],  []]
    Output
    [null,         null,     null,   2,   null, null,   null,       null,       null, 103,   202, 201,  -1]
    size -> 3
    [(1, 0),(2, 100),(3, 100)]
    
    [(1, 200),] -> 202 -> 103
    2 -> 200
    2 -> 100
    """
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []

    def push(self, val: int) -> None:
        """Time O(1)"""
        if len(self.stack) < self.size:
            self.stack.append(Item(val))

    def pop(self) -> int:
        """Time O(1)"""
        if not self.stack:
            return -1
        item = self.stack.pop()
        if self.stack:
            self.stack[-1].increment += item.increment
        return item.val + item.increment

    def increment(self, k: int, val: int) -> None:
        """Time O(1)"""
        if self.stack:
            k = min(k, len(self.stack))
            self.stack[k-1].increment += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)