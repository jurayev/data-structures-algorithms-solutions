class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]
    
    def maximumScore1(self, nums: List[int], mult: List[int]) -> int:
        """
     m   0 1 2  n
     0  [0,0,0]
     1  [0,0,0]
     2  [0,0,4]
        
        
        
        """
        
        @functools.lru_cache(maxsize=2000)
        def dp(left, i):
            if i >= len(mult):
                return 0

            right = len(nums) - 1 - (i - left)

            return max(mult[i] * nums[left] + dp(left+1, i+1), mult[i] * nums[right] + dp(left, i+1))
        return dp(0, 0)
    
    