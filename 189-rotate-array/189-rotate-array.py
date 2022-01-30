class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        [1,2,3,4,5,6,7]
        
        """
        k %= len(nums)
        j = 0
        nums_copy = nums[:]
        for i in range(len(nums)):
            if -k+i < 0:
                nums[i] = nums_copy[-k+i]
            else:
                nums[i] = nums_copy[j]
                j += 1
        
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        j = 0 if k % 2 else 1
        nums[-k:], nums[:-k+j] = nums[:-k+j], nums[-k:]
        