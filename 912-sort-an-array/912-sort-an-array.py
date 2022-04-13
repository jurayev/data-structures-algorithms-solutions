class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge Sort
        
        [5,1,1,2,0,0]
        
        [5,1,1, 2,0,0] -> [1,1,5] [0,0,2] -> [0,0,1,2,5]
        
        [5][1,1] -> [1,1,5]
        [] -> []
            [1][1] -> [1,1]
        """
        return self.merge_sort(nums)
        
    def merge_sort(self, nums) -> list:
        # Time O(N log N)
        # Space O(N)
        if len(nums) <= 1:
            return nums
        
        middle_idx = len(nums) // 2
        
        left_part = self.merge_sort(nums[:middle_idx])
        right_part = self.merge_sort(nums[middle_idx:])
        return self.merge(left_part, right_part)
    
    
    def merge(self, left_part, right_part):
        array = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left_part) or right_idx < len(right_part):
            left_el = left_part[left_idx] if left_idx < len(left_part) else float("inf")
            right_el = right_part[right_idx] if right_idx < len(right_part) else float("inf")
            if left_el < right_el:
                array.append(left_el)
                left_idx += 1
            else:
                array.append(right_el)
                right_idx += 1
        return array