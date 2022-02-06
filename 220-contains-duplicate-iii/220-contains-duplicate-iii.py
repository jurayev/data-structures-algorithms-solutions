class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
         0 1 2 3
        [1,3,2,1]  t = 2, k = 2 
             ^
         
         num 8
         t = 2
         left = 8 - 2 = 6
         right = 8 + 2 = 10
         0 1 2 3 4 5
        [5,10,10]

        
        [1,5,9,1,4,9] k=2, t=3
             1, 8
        [1,6]
        """
        n = len(nums)
        seen_k = []
        
        for idx, num in enumerate(nums):
            leftmost_i = bisect.bisect_left(seen_k, num - t)
            rightmost_i = bisect.bisect_right(seen_k, num + t)
            if leftmost_i < len(seen_k) and rightmost_i - leftmost_i > 0:
                return True
            bisect.insort(seen_k, num)
            if len(seen_k) > k:
                seen_k.remove(nums[idx-k])
            
            
        return False