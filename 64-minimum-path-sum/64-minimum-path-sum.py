class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        [1,3,1]
        [1,5,1]
        [4,2,1]
        
        time O (nm)
        space O(nm)

        state -> sums[r][c] = min path sum till r, c position
        initial state -> sums[0][0…cols] = inf
                      -> sums[0…cols][0] = inf
        transition function -> sum[r][c] = min(sum[r-1][c], sum[r][c-1]) + sum[r][c]
        calculation order: 1….rows-1; 1….cols-1

        """
        return self.find_min_path_sum(grid)
    
    def find_min_path_sum(self, grid):
        rows, cols = len(grid), len(grid[0])
        if not rows or not cols:
            return -1
        sums = [[float("inf") for _ in range(cols+1)] for _ in range(rows+1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if r == 1 and c == 1:
                    sums[r][c] = grid[r-1][c-1]
                else:
                    sums[r][c] = min(sums[r-1][c], sums[r][c-1]) + grid[r-1][c-1]
        return sums[rows][cols]
