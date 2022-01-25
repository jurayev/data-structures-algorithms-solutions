class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [0,1,2,3,4,2,2,3,3,4]
        i
                             j
        k = 4
        
        [1,2,2]
           i
             j
        [1,2,3]
         i
         j
        """
        unique_idx, dup_idx = 0, 0
        while dup_idx < len(nums):
            while dup_idx < len(nums) and nums[unique_idx] == nums[dup_idx]:
                dup_idx += 1
            
            if dup_idx >= len(nums):
                break
            
            nums[unique_idx+1] = nums[dup_idx]
            unique_idx += 1
            dup_idx += 1
   
        return unique_idx+1