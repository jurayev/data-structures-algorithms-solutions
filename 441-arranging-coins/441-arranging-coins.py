class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        1, 2, 3, 4, 5
        
        1, 2, 3, 4, 5, 6, 7, 8,
        
        
        10 -> 4
        11 -> 4 + 1
        
        curr = k * (k + 1) / 2;
        """
        
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            used_coins = mid * (mid + 1) // 2
            if used_coins == n:
                return mid
            if used_coins < n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right