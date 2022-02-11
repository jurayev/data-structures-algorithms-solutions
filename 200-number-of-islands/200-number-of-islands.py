class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        visited=set()
        q = deque()
        num = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range (n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    num+=1                    
                    q.append((i,j))         
                    visited.add((i,j))
                    while(q):
                        (ni,nj) = q.popleft()
                        
                        for neighbour in [(min(m-1,ni+1),nj), (ni,min(n-1,nj+1)), (max(0,ni-1),nj),(ni,max(0,nj-1))] :
                            
                            if neighbour not in visited and grid[neighbour[0]][neighbour[1]] == "1":
                                visited.add(neighbour)
                                q.append(neighbour)
            
        return num  

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.traverse_island_dfs(row, col, grid)
                    #self.traverse_island_bfs(row, col, grid, visited)
                    islands += 1
                
        return islands
    
    def traverse_island_dfs(self, row, col, grid):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
            return
        grid[row][col] = "0"
        self.traverse_island_dfs(row+1, col, grid)
        self.traverse_island_dfs(row-1, col, grid)
        self.traverse_island_dfs(row, col+1, grid)
        self.traverse_island_dfs(row, col-1, grid)
        
        
    def traverse_island_bfs(self, row, col, grid, visited):
        unvisited = collections.deque([(row, col)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while unvisited:
            curr_row, curr_col = unvisited.popleft()
            #visited.add((curr_row, curr_col))
            grid[curr_row][curr_col] = "0"
            for next_row, next_col in directions:
                r = curr_row + next_row
                c = curr_col + next_col
                # if (r, c) in visited:
                #     continue
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    unvisited.append((r, c))
        