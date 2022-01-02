class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        Question from Weekly Contest 274
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        nums = sorted(asteroids)
        
        total_mass = mass
        
        for num in nums:
            if total_mass < num:
                return False
            total_mass += num  
        return True