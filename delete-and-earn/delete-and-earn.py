class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Approach:
            Using buckets, sum up all the same values.
            Implement DP solution like for House Robber problem
        [2,2,3,3,3,4,1]
         0 1 2 3 4 5 6 7 8
         0 0 4 9 4 0 0 0 0
         0 1 4 10 8 10 8 9 8
         
          [2,3,4]
          0 1 2 3 4
          0 0 2 3 4
          0 0 2 3 6
          
        Time Complexity O(N), N is 10000
        Space Complexity O(N)
        """
        buckets = [0] * 10001
        
        for num in nums:
            buckets[num] += num
            
        for i in range(2, len(buckets)):
            buckets[i] = max(buckets[i-1], buckets[i-2] + buckets[i])
        
        return max(buckets[-1], buckets[-2])
        