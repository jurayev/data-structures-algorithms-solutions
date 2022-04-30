class Solution:
    def trap(self, height: List[int]) -> int:
        return self.dp_solution(height)
        #return self.two_pointers_solution(height)
        
        
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
            total_water += min_max - heights[idx]
        return total_water

    
    def two_pointers_solution(self, heights):
        left_idx, right_idx = 0, len(heights)-1
        total_water = 0
        left_max = 0
        right_max = 0
        while left_idx <= right_idx:
            left_max = max(left_max, heights[left_idx])
            right_max = max(right_max, heights[right_idx])
            min_max = min(left_max, right_max)
            if heights[left_idx] <= heights[right_idx]:
                total_water += min_max - heights[left_idx]
                left_idx += 1
            else:
                total_water += min_max - heights[right_idx]
                right_idx -= 1
            
        return total_water
            
        