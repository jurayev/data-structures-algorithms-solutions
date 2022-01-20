class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            
        piles = [3,6,7,11], h = 8 rem = 1 k = 4
                            h = 2+3+4+6
                 1 2 2  3 
                
                1 2 3 4 5 6 7 8 9 10 11
                l          
                                     r
                 
        Time Complexity O(N log M), where N is the number of piles, M is the range 1....max pile
        Space Complexity O(1)
        """
        
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            curr_speed = left + (right-left) // 2
            if self.can_eat(piles, curr_speed, h):
                min_speed = min(min_speed, curr_speed)
                right = curr_speed - 1
            else:
                left = curr_speed + 1
                
        return min_speed
    
    def can_eat(self, piles, speed, h):
        """
        2//3  -> 0
        2 % 3 -> 2
        """
        for pile in piles:
            h -= pile // speed
            h -= int(pile % speed != 0)
        return h >= 0