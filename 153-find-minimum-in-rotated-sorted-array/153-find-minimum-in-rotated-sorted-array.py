class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
        
    def findMin1(self, nums: List[int]) -> int:
        """
        [4,5,6,7,0,1,2]
        
        [7,1,2,3,4]
        
        [7,1,2,2,3]
        """
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            
            if self.condition(nums, left, mid):
                if self.condition(nums, mid, right): # mid is between sorted edges
                    right = mid
                else:
                    left = mid + 1
            else:
                if self.condition(nums, mid, right): # mid is between sorted edges
                    right = mid
                else:
                    left = mid + 1
                
        return nums[left]
    
    def condition(self, nums, left, right):
        return nums[left] <= nums[right]
            
            