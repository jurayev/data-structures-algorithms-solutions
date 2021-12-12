class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        Approach:
            For every possible subarray keep track of the min and max element, subracting max_val - min_val
        
        Complexity:
            TC: O(n^2)
            SC: O(1)
        
        Examples:
            [4,-2,-3,4,1]  => 59
                       ^
                       ^
             [4,-2]  6
             [4,-3]  7
             [4,-3]  7
             [4,-3]  7

             [-2,-3] 1
             [4,-3]  7
             [4,-3]  7

             [4,-3]  7
             [4,-3]  7

             [4,1]   3
        
        
        """
        # max_num = float(-inf)   4
        # min_num = float(inf)    1
        result = 0
        n = len(nums)
        for i in range(n):
            max_num = nums[i]
            min_num = nums[i]
            for j in range(i, n):
                max_num = max(max_num, nums[j])
                min_num = min(min_num, nums[j])
                result += max_num - min_num
                
        return result