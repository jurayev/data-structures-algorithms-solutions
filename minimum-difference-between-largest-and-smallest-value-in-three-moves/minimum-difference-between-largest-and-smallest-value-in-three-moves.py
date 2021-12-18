class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        
        Approach:
            Sort the values, if given exacly 3 moves, 
                remove 3 min elements or 
                remove 3 max elements, 
                remove 2 min elements, 1 max element
                remove 1 min elements, 2 max element
            
        Examples:
        
        0,2,3,4,4,5,6,
        
        
        [2,3,4,5]
        
        [20,75,81,82,95,]
                 ,82,95,
                  3  -1
               81,82,
               2  -2
            20,81,
            1  -3
         20,75,
         0  -4
        
        """
        if len(nums) < 5:
            return 0
        
        sorted_nums = sorted(nums)
        best = float(inf)
        for i in range(0,4):
            diff = sorted_nums[i-4] - sorted_nums[i]
            best = min(best, diff)
        
        return best
        