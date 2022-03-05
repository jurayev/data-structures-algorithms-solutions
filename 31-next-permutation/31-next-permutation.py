class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        [9, 5, 4, 7, 5, 1]
               ^
           
        [2 1 2]   
        """
        
        swap_index = -1
        for i in reversed(range(1, len(nums))):
            if nums[i-1] < nums[i]:
                swap_index = i-1
                break
        if swap_index == -1:
            self.reverse(0, len(nums)-1, nums)
            return
        for i in reversed(range(0, len(nums))):
            if nums[i] > nums[swap_index]:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                break
        self.reverse(swap_index+1, len(nums)-1, nums)
        
    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
                          

            