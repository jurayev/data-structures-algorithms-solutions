class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [0,1,0,3,2,3]
        
         ^ ^     ^ ^ 
         
         Brute Force O(2^n)
         
         DP O(N^2)
         
           [0,1,0,3,2,3]
          1 1 1 1 1 1 1
        0 1 1 2 2 2 2 2
        1 1 1 2 2 2 3 3
        0 1 1 2 2 3 3 4
        3 1 1 2 2 3 3 4
        2 1 1 2 2 3 3 4
        3 1 1 2 2 3 3 4
         State: [i, j] -> Cell(i, j) -> prefix of seq till i and prefix of seq till j
         Value function: max len of the subsequence 
         Transition:    1. if nums[i] < nums[j]: dp[i][j] = dp[i-1][j-1] + 1
                        2. dp[i][j] = max(dp[i-1][j], dp[i][j-1]) -> skip or increase
                        
         Order of calculation: 0 ... i - 1, 0.... j-1
         Answer: dp[i-1][j-1]
         Reconstuction: store of the reference
            [4,10, 4, 3, 8, 9]    
            [1, 2, 1, 1, 2, 3]
                            i
                         j

            [0,1,0,3,2,3]
            [1,2,1,2,1,1]
                   i
                 j

        """
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        