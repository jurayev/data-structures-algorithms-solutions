class Solution:
    def trap(self, height: List[int]) -> int:
        return self.dp_solution(height)
        
        
    def dp_solution(self, heights):
        max_height = 0
        
        left_maxes = []
        for height in heights:
            max_height = max(max_height, height)
            left_maxes.append(max_height)
        
        max_height = 0
        right_maxes = []
        for height in reversed(heights):
            max_height = max(max_height, height)
            right_maxes.append(max_height)
            
        right_maxes = right_maxes[::-1]
        total_water = 0
        for idx in range(len(heights)):
            min_max = min(left_maxes[idx], right_maxes[idx])
            total_water += abs(min_max - heights[idx])
        return total_water
        
        
    
    
    def two_pointer_solution(height):
        pass