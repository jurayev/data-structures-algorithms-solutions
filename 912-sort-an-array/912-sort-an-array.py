class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quick_sort(nums, 0, len(nums)-1)
        # return nums
        #return self.merge_sort(nums)
        #return self.quick_sort(nums)
        #return self.heap_sort(nums)
        #return self.insertion_sort(nums)
        #return self.bubble_sort(nums)
        #return self.selection_sort(nums)
        return sorted(nums)
    
    def quick_sort(self, nums, start, end):
        """
        Merge Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        TLE
        """
        if start >= end:
            return 
        
        pivot_idx = self.partition(nums, start, end)
        self.quick_sort(nums, start, pivot_idx-1)
        self.quick_sort(nums, pivot_idx+1, end)
        
    def partition(self, nums, start, end):
        # [9, 18, 32, 40, 61, 50]
        #          i  
        #                      j
        #                      p
        pivot_el = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < pivot_el:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[end] = nums[end], nums[i]
        return i
        
    def merge_sort(self, nums):
        """
        Merge Sort Impelementation
        
        Time O(N log N)
        Space O(N Log N)
        """
        if len(nums) <= 1:
            return nums
        mid_idx = len(nums) // 2
        left_nums = self.merge_sort(nums[:mid_idx])
        right_nums = self.merge_sort(nums[mid_idx:])
        return self.merge(left_nums, right_nums)

    def merge(self, left_nums, right_nums):
        """
        Time O(M+N)
        Space O(M+N)
        """
        merged_nums = []
        l_size = len(left_nums)
        r_size = len(right_nums)
        left_idx = 0
        right_idx = 0
        while left_idx < len(left_nums) or right_idx < len(right_nums):
            left_num = left_nums[left_idx] if left_idx < l_size else float("inf")
            right_num = right_nums[right_idx] if right_idx < r_size else float("inf")
            if left_num < right_num:
                merged_nums.append(left_num)
                left_idx += 1
            else:
                merged_nums.append(right_num)
                right_idx += 1

        return merged_nums

    def heap_sort(self, nums):
        """
        Heap Sort Impelementation
        
        Time O(N log N)
        Space O(N)
        """
        from heapq import heapify, heappop
        min_heap = nums[:]
        heapify(min_heap)
        
        index = 0
        while min_heap:
            min_element = heappop(min_heap)
            nums[index] = min_element
            index += 1
        return nums
    
    def insertion_sort(self, nums: List[int]) -> List[int]:
        """
        Insertion Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        TLE
        """
        n = len(nums)
        for i in range(0, n):
            for j in range(i, 0, -1):
                if nums[j-1] <= nums[j]:
                    break
                nums[j-1], nums[j] = nums[j], nums[j-1] 
        return nums
        
    def selection_sort(self, nums: List[int]) -> List[int]:
        """
        Selection Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        TLE
        """
        n = len(nums)
        for i in range(0, n):
            min_el_idx = i
            for j in range(i+1, n):
                min_el_idx = j if nums[j] < nums[min_el_idx] else min_el_idx
            nums[i], nums[min_el_idx] = nums[min_el_idx], nums[i]			
        return nums

    
    def bubble_sort(self, nums: List[int]) -> List[int]:
        """
        Buble Sort Impelementation
        
        Time O(N^2)
        Space O(1)
        TLE
        """
        size = len(nums)
        for i in range(size):
            for j in range(size-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
        return nums
                
        
        