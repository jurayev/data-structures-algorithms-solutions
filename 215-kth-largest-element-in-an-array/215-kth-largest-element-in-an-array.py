class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quick Select 
        Time worst: O(N^2)
        Time best: O(N)
        
        [3,2,1,4,5,6]
        """
        return self.quick_select(nums, k)
        
    def quick_select(self, nums, k):
        pivot_num = random.choice(nums)
        min_nums = [num for num in nums if num < pivot_num]
        equal_nums = [num for num in nums if num == pivot_num]
        max_nums = [num for num in nums if num > pivot_num]

        m_size, e_size = len(max_nums), len(equal_nums)
        if k <= m_size:
            return self.quick_select(max_nums, k)
        if k > m_size + e_size:
            return self.quick_select(min_nums, k - m_size - e_size)
        return pivot_num
        
    def partition(self, nums, start, end):
        p_index = end
        i = start
        for j in range(start, end):
            if nums[j] < nums[p_index]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        nums[i], nums[p_index] = nums[p_index], nums[i]
        return i
        