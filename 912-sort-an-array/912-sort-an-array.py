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
        return self.bucket_sort(nums)
        return self.merge_sort(nums)
    
    def bucket_sort(self, nums):
        max_num = max(nums)
        pos_buckets = [0] * (max_num + 1)
        min_num = min(nums)
        neg_buckets = [0] * (abs(min_num)+1) # [1, 2, 3, 5]
        for num in nums:
            if num >= 0:
                pos_buckets[num] += 1
            else:
                neg_buckets[abs(num)] += 1
        sorted_nums = []
        for num in range(abs(min_num), -1, -1):
            for _ in range(neg_buckets[num]):
                sorted_nums.append(-num)
        
        for num in range(0, max_num+1):
            for _ in range(pos_buckets[num]):
                sorted_nums.append(num)
        return sorted_nums
    
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
        left_size, right_size = len(left_part), len(right_part)
        while left_idx < left_size or right_idx < right_size:
            left_el = left_part[left_idx] if left_idx < left_size else float("inf")
            right_el = right_part[right_idx] if right_idx < right_size else float("inf")
            if left_el < right_el:
                array.append(left_el)
                left_idx += 1
            else:
                array.append(right_el)
                right_idx += 1
        return array