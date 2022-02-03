class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quick Select 
        Time worst: O(N^2)
        Time best: O(N)
        
        [3,2,1,4,5,6]
        """
        return self.quick_select(nums, 0, len(nums)-1, len(nums)-k)
        
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        pivot_idx = self.partition(nums, start, end)
        if k > pivot_idx:
            return self.quick_select(nums, pivot_idx+1, end, k)
        if k < pivot_idx:
            return self.quick_select(nums, start, pivot_idx-1, k)
        
        return nums[pivot_idx]
        
    def partition(self, nums, start, end):
        p_index = end
        i = start
        for j in range(start, end):
            if nums[j] < nums[p_index]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        nums[i], nums[p_index] = nums[p_index], nums[i]
        return i
        