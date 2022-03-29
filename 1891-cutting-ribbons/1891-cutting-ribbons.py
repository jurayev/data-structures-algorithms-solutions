class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        """
        [7,5,9], k = 4, sum=21//4 -> 5
         1 1 1
        [0,1,2,3,4,5]
                   m
                   l          
                   r
        """
        left_idx = 0
        right_idx = sum(ribbons) // 2
        
        while left_idx < right_idx:
            mid_idx = (1 + left_idx + right_idx) // 2
            
            obtained_ribbons = 0
            for ribbon in ribbons:
                obtained_ribbons += ribbon // mid_idx

            if obtained_ribbons >= k:
                left_idx = mid_idx
            else:
                right_idx = mid_idx - 1
        return left_idx