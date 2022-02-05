class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
         0 1 2 3
        [1,2,3,1]
         ^
               ^
        
        """
        seen = {}
        for idx1, num in enumerate(nums):
            if num in seen:
                idx2 = seen[num]
                if idx1 - idx2 <= k:
                    return True
            seen[num] = idx1
            
        return False