class MovingAverage:
    """
    [1,10,3,5]
    
    size = 3
    n = 4
    [0,1,11,14,19]
    """
    def __init__(self, size: int):
        self.size = size
        self.prefixes = [0]

    def next(self, val: int) -> float:
        n = len(self.prefixes)
        self.prefixes.append(val)
        self.prefixes[-1] += self.prefixes[-2]
        if n <= self.size:
            return self.prefixes[-1] / n
        return (self.prefixes[-1] - self.prefixes[n-self.size]) / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)