class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        2^4 -> 16
        
        n = 4 -> 4*4  -> 16
        n = 2 -> 2*2 -> 4
        n = 1 -> 1*1*2 -> 2
        n = 0 -> 1
        
        keep dividing n // 2
        if n is even -> power of two
        if n is odd -> power of two * x
        
        Time O(logN)
        Space O(logN)
        """
        if n < 0:
            x = 1 / x
            n = -n
        return self.fast_pow(x, n)
    
    def fast_pow(self, x, n):
        if n == 0:
            return 1.0
        
        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x