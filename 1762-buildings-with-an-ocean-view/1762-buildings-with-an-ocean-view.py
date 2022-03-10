class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        1. Brute Force try all positions
            Time O(N^2)
            Space O(N)
        2. Use mono decreasing queue
            Time O(N)
            Space O(N)
        3. Scan from right to left and keep a tallest building
        
        [4,2,3,3,1]
         ^
        3
        [0, 3, 4]
        """
        tallest = float("-inf")
        buildings = []
        total = len(heights)
        for index in reversed(range(total)):
            building = heights[index]
            if building > tallest:
                tallest = building
                buildings.append(index)
                
        return buildings[::-1]
    
    def mono_queue(heights):
        mono_stack = []
        for index in range(len(heights)):
            height = heights[index]
            while mono_stack and heights[mono_stack[-1]] <= height:
                mono_stack.pop()
                
            mono_stack.append(index)
            
        return mono_stack