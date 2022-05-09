class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        
        1 ... 10
        
        p = 1
        
                       
        1. pick arbitrary between left and right
        2. find the best pivot
        3. repeat recursively
        """
        @lru_cache(maxsize=None)
        def dp(left, right):
            best = float("inf")
            for pivot in range(left, right):
                left_best = dp(left, pivot-1)
                right_best = dp(pivot+1, right)
                best = min(best, max(left_best, right_best) + pivot)
            return best if best != float(inf) else 0
        
        return dp(1, n)