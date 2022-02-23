class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
         1 2 3 2
        
        [1,1,1,1,1]
         2 2 2 2 
        
        
        -1 + 1 + 1 + 1 + 1 = 3
        +1 - 1 + 1 + 1 + 1 = 3
        +1 + 1 - 1 + 1 + 1 = 3
        
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 - 1 - 1 = 2
        
        +1 + 1 + 1 + 1 - 1 = 3
        +1 + 1 + 1 + 1 + 1 = 4
        
        @lru_cache(maxsize=None)
        sum_ways(i, target-nums[i])
        sum_ways(i, target+nums[i])
        sum_ways(i+1, target-nums[i+1])
        sum_ways(i+1, target+nums[i+1])
        sum_ways(n-1, target-nums[n-1])
        sum_ways(n-1, target+nums[n-1])
        
        O(N^2)
        
        [1,1,1] -> 3
        sum_ways(-1, 3)
        
        sum_ways(0, 2)
                        sum_ways(1, 1)
                                    sum_ways(2, 0)
                                            sum_ways(3, -1)
                                            sum_ways(3, 1)
                                    sum_ways(2, 2)
                        sum_ways(1, 3)
        sum_ways(0, 4)
        
        
        """
        @lru_cache(maxsize=None)
        def sum_ways(i, target):
            if i >= len(nums):
                return target == 0

            return sum_ways(i+1, target-nums[i]) + sum_ways(i+1, target+nums[i])
        if not nums:
            return 0
        return sum_ways(0, target)