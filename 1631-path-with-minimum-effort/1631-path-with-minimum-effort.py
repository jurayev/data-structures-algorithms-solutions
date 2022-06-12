class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        source = (0, 0)
        dest = (len(heights)-1, len(heights[0])-1)
        return self.djikstra(heights, source, dest)
    
    
    def djikstra(self, graph, source, dest):
        rows, cols = len(graph), len(graph[0])
        visited = [[False] * cols for _ in range(rows)]
        costs = [[float("inf")] * cols for _ in range(rows)]
        costs[0][0] = 0
        queue = []
        heappush(queue, (0, source[0], source[1]))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            cost, row, col = heappop(queue)
            visited[row][col] = True
            
            for dir_row, dir_col in dirs:
                next_row, next_col = row+dir_row, col+dir_col
                if not self.is_valid(next_row, next_col, graph):
                    continue
                    
                if visited[next_row][next_col]:
                    continue
                new_cost = max(abs(graph[row][col] - graph[next_row][next_col]), costs[row][col])
                if costs[next_row][next_col] > new_cost:
                    costs[next_row][next_col] = new_cost
                    heappush(queue, (new_cost, next_row, next_col))
        return costs[-1][-1]
    
    
    def is_valid(self, row, col, matrix):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])