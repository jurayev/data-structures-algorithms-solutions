class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        
        [1,2,3,4]
        
        [4,3,2,1]
        """
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if self.condition(nums, mid) == 0:
                return mid
            if self.condition(nums, mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
    
    def condition(self, nums, mid):
        prev_num = nums[mid-1] if mid-1 >= 0 else float("-inf")
        next_num = nums[mid+1] if mid+1 < len(nums) else float("-inf")
        if prev_num < nums[mid] > next_num:
            return 0
        if nums[mid] < next_num:
            return 1
        return 2
        