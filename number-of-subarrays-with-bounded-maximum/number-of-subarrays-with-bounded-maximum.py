class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        count = 6
        prev  = 6
        [2,1,4,3], left = 2, right = 3
        
        [[2,2,3,1]], left = 2, right = 3
                i
        j
        
        handle min vals : if new is from range use dist from start to end + 1
                          if new is smaller, use last count
                          if new is great, break and move pointer
        
        
        """
        count = 0
        prev = 0
        i,j = 0, -1
        
        while i < len(nums):
            num = nums[i]
            if left <= num <= right:
                count += i - j
                prev = i - j
            elif num < left:
                count += prev
            else:
                j = i
                prev = 0
            
            i += 1
        return count