class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        [1,2,1,2,3], k = 2
               ^
                 ^
         0 1 2 3
        
        
        [1,1,2,2,1,1], k = 2
         ^
               ^
             2 2
        [1,1,2,1,1,1], k = 2
               3 3 3
                 4
        
        c = 1 + 1
        counts = {
        1: 2
        2: 2
        }
        
        if prev == curr:
            count[curr] = count[prev]
        else:
            count[curr] = count[prev] + 1
            
        if len(counts) < k:
            expand
        elif len(counts) == k:
            update total count
        else:
            shrink
            
        [1,2,1,2,3] k = 2
         ^
             ^
         1
        """
        return self.with_at_most_k(nums, k) - self.with_at_most_k(nums, k-1)
        
    def with_at_most_k(self, nums, k):
        total_subarrays = 0
        counts = Counter()
        
        start_idx, end_idx = 0, 0
        
        while end_idx < len(nums):
            end_num = nums[end_idx]
            counts[end_num] += 1
            
            while len(counts) > k:
                start_num = nums[start_idx]
                counts[start_num] -= 1
                if counts[start_num] == 0:
                    del counts[start_num]
                    
                start_idx += 1
            total_subarrays += end_idx - start_idx + 1
            end_idx += 1
            
                
            
        return total_subarrays