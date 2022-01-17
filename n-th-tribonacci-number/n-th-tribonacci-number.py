class Solution:
    cache = {0:0, 1:1, 2:1}
    
    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.cache[n]

    def tribonacciTopDown(self, n: int) -> int:
        for i in range(3, n+1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2] + self.cache[i-3]
        
        return self.cache[n]