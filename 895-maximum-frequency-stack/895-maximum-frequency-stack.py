class FreqStack:
    """
    copy = [5:1, 7:1, 5:2, 7:2, 4:1, 5:3]
    
    []
    pop() -> 5
    pop() -> 7
    pop() -> 5
    pop() -> 4
    pop() -> 7
    pop() -> 5
    
    Ideas:
        1. Counter dict with all counts for values
        2. max heap with (counter, value) pairs
        3. keep stack in the correct order, allowing simple O(1) pops
            - using global counters for values, search insert position using binsearch
            - Time Complexities:
                    TC push() -> O(N) , optimize with BST O(log N)
                    TC pop() -> O(1), BST remove O(log N)
                    SC O(M), M unique numbers
        [5:1, 7:1, 4:1, 3:1, 5:2, 7:2, 4:2, 5:3, 0:1]
        
        
    """
    def __init__(self):
        self.counters = Counter()
        self.stack = []

    def push(self, val: int) -> None:
        self.counters[val] += 1
        insort_right(self.stack, (self.counters[val], val), key=lambda x: x[0])
        
    def pop(self) -> int:
        if not self.stack:
            return -1
        counter, val = self.stack.pop()
        self.counters[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()