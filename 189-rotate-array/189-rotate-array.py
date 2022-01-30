class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        [1,2,3,4,5,6,7]
        
        [7,6,5,4,3,2,1]
        
        [5,6,7,1,2,3,4]
                   j
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
                
        
    def rotate1(self, nums: List[int], k: int) -> None:
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
        