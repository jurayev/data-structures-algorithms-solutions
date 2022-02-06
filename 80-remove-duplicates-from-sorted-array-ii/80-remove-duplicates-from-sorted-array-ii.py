class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [0,0,1,1,2,3,3,3,3]
                         e
                 s   s
        
        count = 3
        """
        
        start, end = 2, 2
        
        while end < len(nums):
            if nums[start-2] != nums[end]:
                nums[start] = nums[end]
                start += 1
            end += 1
            
        return start
                
                
                
                
            
            