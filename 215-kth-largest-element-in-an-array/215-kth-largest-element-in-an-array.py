class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quickselect
        
        [3,2,1,5,6,4], k = 4

        k = 3
        smaller = [3,2,1,4]
        bigger = [5,6]
        
        [3,2,1,4]
        k = 1
        s = [1,2]
        b = [3,4]
        
        [3,3,4]
        k = 4     k = 1
        s = [2,1]
        e = [3,3]
        b = [4]
        
        [2,1]  k = 1
        s = []
        e = [1]
        b = [2]
        
        [2] = k = 1
        s = []
        e = [2]
        b = []
        
        Time O(N^2)     with fixed pivot
        Time O(N log N) with random pivot
        Time O(N)       the average/best cases
        
        Space O(N log N)
        """
        return self.quick_select(nums, k)
    
    def quick_select(self, nums, k):
        # split into 3 array by pivot
        pivot_num = random.choice(nums)
        smaller_nums = [num for num in nums if num < pivot_num]
        equal_nums = [num for num in nums if num == pivot_num]
        bigger_nums = [num for num in nums if num > pivot_num]

        big_size, eq_size = len(bigger_nums), len(equal_nums)
        if k <= big_size:                                     # check if in bigger
            return self.quick_select(bigger_nums, k)
        if k > big_size + eq_size:                            # check if in smaller
            return self.quick_select(smaller_nums, k - big_size - eq_size)
        return pivot_num                                      # element has to be in equal
        