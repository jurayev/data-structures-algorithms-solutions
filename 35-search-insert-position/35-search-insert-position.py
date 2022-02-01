class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        [1,3,5,6] -> 0
         m
        
        """
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        return start