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

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        val, increment = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += increment
        return val + increment

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            k = min(k, len(self.stack))
            self.stack[k-1][1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)