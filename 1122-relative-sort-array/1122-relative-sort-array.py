class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        size = len(arr1)
        counts = collections.Counter(arr1)
        extra_nums = [num for num in arr1 if num not in set(arr2)]
        curr_index = 0
        for num2 in arr2:
            for i in range(counts[num2]):
                arr1[curr_index+i] = num2
            curr_index += counts[num2]
        
        
        self.bubble_sort(0, len(extra_nums), extra_nums)

        for num in extra_nums:
            arr1[curr_index] = num
            curr_index += 1
        return arr1
        
        
    def bubble_sort(self, start, end, nums):
        for i in range(start, end):
            for j in range(start, end-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]