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
                    burst(l, j-1) + burst(j+1, r) + nums[l] * nums[j] * nums[r]
        base cases:
            
        answer -> burst(0, n-1)
        """
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
        return burst(-1, len(nums))