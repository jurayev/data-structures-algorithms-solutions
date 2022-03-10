class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        1. Brute Force try all positions
            Time O(N^2)
            Space O(N)
        2. Use mono decreasing queue
            Time O(N)
            Space O(N)
        
        [4,2,3,3,1]
                 ^
        [0, 3, 4]
        """
        
        mono_stack = []
        for index in range(len(heights)):
            height = heights[index]
            while mono_stack and heights[mono_stack[-1]] <= height:
                mono_stack.pop()
                
            mono_stack.append(index)
            
        return mono_stack