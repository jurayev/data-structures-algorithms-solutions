class StockSpanner:
    """
    TC O(1) - Amortized, O(n) - Worst
    SC O(n) - keeping intermediate result in the stack

    Approach: mono stack (decreasing), precalculate prev results

    Examples:
    [100,80,60,70,60,75,85]

    [100:1 , 80:1, 60:1, 60:1, 70:1, 60:1, 75:1, 85:1]
                                                  ^
    [100:1, 85:8]
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
