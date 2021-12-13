class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        Approach: 
            Treat bomb locations as a directed graph, calculate if intersection(connected), traverse all connected bombs
            
        Complexity:
            Time:  O(N*2)
            Space: O(N)
            
        Examples:
            [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
             [x,y,r]
           +1[1,5]   [2,4]
           -1[1,-1]  [2,2]
           +1[4,2]   [3,3]
           -1[-2,2]  [1,3]

            diameter = math.sqrt((x2-x1)**2 + (y2-y1)**2)  = 1,5
                                   1        +    1


            is_intersect = d < abs(r1-r2) = true
                           1,5 < 2
             
        smaller example: 
            [[2,1,3],[6,1,4]]
            check intersection = (x1[0] - x2[0]) ** 2 + (y1[1] - y2[1]) ** 2 <= r1[2] ** 2:
                                 16               +     0                      16        
        """
        max_bombs = 0
        
        for idx in range(len(bombs)):      # 0
            visited = set()                # {0,1,2}
            self.dfs(bombs, idx, visited)
            max_bombs = max(max_bombs, len(visited))
        return max_bombs
    
    def dfs(self, bombs, idx, visited):   # 0  # 1  # 2
        if idx >= len(bombs):
            return
        visited.add(idx)
        x1, y1, r1 = bombs[idx]           # 1,2,3    # 2,3,1  # 3,4,2
        
        for next_idx in range(0, len(bombs)): # 1 # 2
            if idx == next_idx or next_idx in visited: 
                continue
            x2, y2, r2 = bombs[next_idx]  # 2,3,1    # 3,4,2  # 4,5,3
            is_intersect = (x2-x1)**2 + (y2-y1)**2 <= r1**2 # true # true # true

            if is_intersect:
                self.dfs(bombs, next_idx, visited)
        