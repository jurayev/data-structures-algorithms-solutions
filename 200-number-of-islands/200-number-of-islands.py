class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.traverse_island_bfs(row, col, grid, visited)
                    islands += 1
                
        return islands
            
    def traverse_island_bfs(self, row, col, grid, visited):
        unvisited = deque([(row, col)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while unvisited:
            curr_row, curr_col = unvisited.popleft()
            if (curr_row, curr_col) in visited: continue
            visited.add((curr_row, curr_col))
            for next_row, next_col in directions:
                r, c = curr_row + next_row, curr_col + next_col
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    unvisited.append((r, c))
    
    def traverse_island_dfs(self, row, col, grid):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
            return
        grid[row][col] = "0"
        self.traverse_island_dfs(row+1, col, grid)
        self.traverse_island_dfs(row-1, col, grid)
        self.traverse_island_dfs(row, col+1, grid)
        self.traverse_island_dfs(row, col-1, grid)