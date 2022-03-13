class StockSpanner:
    """
    Warm-up: Easy stack question
    
    TC O(2n)
    SC O(n)  - keeping intermediate result in the stack
    
    Approach: mono stack (decreasing), precalculate prev results
    
    Examples:
    [100,80,60,70,60,75,85]  -> [1, 1, 1, 2, 1, 4, 6]
    [50, 40, 30, 20, 10]     -> [1, 1, 1, 1, 1] 
    [10, 20, 30, 40, 50]     -> [1, 2, 3, 4, 5] 
    
    [100,80,60,60,70,60,75,85,85]  -> [1, 1, 1, 2, 3, 1, 5, 7, 8]
     
    [100,80,60,70,60,75,85]
    [100:1 , 80:1, 60:1, 70:2, 60:1, 75:4, 85:6]
                                                
    """
    def __init__(self):
        self.mono_stack = []

    def next(self, price: int) -> int:
        total_days = 1
        while self.mono_stack and self.mono_stack[-1][0] <= price:
            _, prev_days = self.mono_stack.pop()
            total_days += prev_days
        
        self.mono_stack.append((price, total_days))
        return total_days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)