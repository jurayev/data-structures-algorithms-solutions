class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1,2,1,6,5,6,4]
           l
           r
           m       
        
        [1,2,3,4,5,6]
        
        
        [4,5,3,2,1,0]
                    l
                    r
                    m
        [1,2,3,1]
           m
           
         [6,5 ,4,3 ,2,3,2]
          ^
        """
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            mid = (left+right) // 2

            left_el = nums[mid-1] if mid-1 >= 0 else float(-inf)
            right_el = nums[mid+1] if mid+1 < n else float(-inf)
            mid_el = nums[mid]

            if left_el < mid_el > right_el:
                return mid
            elif left_el < mid_el:
                left = mid+1
            else:
                right = mid-1

        return left

                