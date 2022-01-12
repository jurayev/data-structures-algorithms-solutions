class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        {1, 2, 3, 4} -> 10 // 2 = 5

        0 1 2 3 4 5
        {}    t f f f f f
        {1}   t t f f f f
        {1,2} t t t t f f

        {3, 3, 4, 6}
        """
        if sum(nums) % 2:
            return False
        partition_sum = sum(nums) // 2

        n = len(nums)
        dp = [[False for _ in range(partition_sum+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, partition_sum+1):
                num = nums[i-1]
                if num <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num] 
                dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]