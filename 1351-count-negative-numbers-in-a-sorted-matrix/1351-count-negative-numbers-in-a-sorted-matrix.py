class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        [[4, 3, 2,-1],
         [3, 2, 1,-1],
         [1, 1,-1,-2],
         [-1,-1,-2,-3]]
        
        
        """
        count = 0
        rows, cols = len(grid), len(grid[0])
        row, col = rows-1, 0
        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                count += cols - col
                row -= 1
            else:
                col += 1
                
        return count