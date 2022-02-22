class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.find_unique_paths(obstacleGrid)
        
        
    def find_unique_paths(self, grid):
        """
        Time O(R*C)
        Space O(R*C)
        """
        rows, cols = len(grid), len(grid[0])
        paths = [[0 for i in range(cols+1)] for i in range(rows+1)]
        paths[1][1] = 1 if grid[0][0] != 1 else 0
        
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if grid[r-1][c-1] == 1: continue
                paths[r][c] = paths[r][c] + paths[r-1][c] + paths[r][c-1]
        return paths[rows][cols]

        