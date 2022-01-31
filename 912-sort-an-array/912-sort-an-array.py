class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
    
    def insertion_sort(self, nums: List[int]) -> List[int]:
        """
        Buble Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        """
        return nums
        
    def selection_sort(self, nums: List[int]) -> List[int]:
        """
        Selection Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        """
        return nums
    
    def buble_sort(self, nums: List[int]) -> List[int]:
        """
        Buble Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        """
        size = len(nums)
        for i in range(size):
            for j in range(size-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
        return nums
                
        
        