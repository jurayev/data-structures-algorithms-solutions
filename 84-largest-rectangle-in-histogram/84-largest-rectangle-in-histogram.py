class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best_area = 0

        for idx, height in enumerate(heights+[float("-inf")]):
            while stack and heights[stack[-1]] >= height:
                prev_idx = stack.pop()
                H = heights[prev_idx]
                W = idx if not stack else idx - stack[-1] - 1
                best_area = max(best_area, H * W)
            
            stack.append(idx)

        return best_area


        
        
        
    def largestRectangleArea1(self, heights: List[int]) -> int:
        """
        Brute force
        Time O(N^2)
        Space O(1)
        
        """
        best_area = float(-inf)
        n = len(heights)
        for i in range(0, n):
            min_h = heights[i]
            best_area = max(best_area, min_h)
            for j in range(i+1, n):
                min_h = min(min_h, heights[j])
                best_area = max(best_area, min_h * (1+j-i))
  
        return best_area