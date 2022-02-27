class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        
        
        1[3,1,5,8]1
        
        1[3]1  -> 3 [2] -> 2
          j
        1[3,2]1  -> 6, 6
          ^
        1[3,3,2]1 -> 15
            ^
        l i r
        1. subproblems: consider the each baloon as the last one, the remaining L,R
        2. recurrence:
                    1. burst(j, left, right) = max(burst([j+1, j+2, j+3, left, right))
                    2. 
                    burst(l, j) + burst(j, r) + nums[l] * nums[j] * nums[r]
        base cases:
            
        answer -> burst(0, n-1)
        
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for left in range(n-2, 0,-1):     
            for right in range(left, n-1):
                for j in range(left, right+1):
                    points = dp[left][j-1] + dp[j+1][right] + nums[left-1] * nums[right+1] * nums[j]
                    dp[left][right] = max(dp[left][right], points)
        # for row in dp:
        #     print(dp)
        return dp[1][n-2]
        
        @lru_cache(None)
        def burst(left, right):
            if left >= right:
                return 0
            left_num = nums[left] if left >= 0 else 1
            right_num = nums[right] if right < len(nums) else 1
            
            max_points = 0
            for j in range(left+1, right):
                points = burst(left, j) + burst(j, right) + left_num * right_num * nums[j]
                max_points = max(max_points, points)
            return max_points
        #return burst(-1, len(nums))