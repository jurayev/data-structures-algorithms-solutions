class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        1. Return just min moves
                1. Sol Time O(N), Space O(1) -> Linear scan from 0,0 pos
        2. Return the sequence of min moves 
                1. Sol Time O(N), Space O(K) -> Linear scan from 0,0 pos
        3. Return the sequence of min moves, it is still sorted, there might be duplicates
        4. Return the sequence of min moves if letters are placed arbitrary on the board -> BFS to find shortest path 
                1. Sol Time O(N * (V+E)), Space(K + V + E)
        
        aziggo
        
        azy -> DDDDD!URRRR! (only one path!)
        zdz
        
        "abcde", 
        "fghij", 
        "klmno", 
        "pqrst", 
        "uvwxy", 
        "z"
        
        "leet" -> 15, "DDR!UURRR!!DDD!"
        "code" -> 14, "RR!DDRR!UUL!R!"
        "zaz"  -> 18, "DDDDD!UUUUU!DDDDD!"
        "azdz" -> 25, "!DDDDD!UUUUURRR!LLLDDDDD!"
        "a"    -> 1,  "!"
        "b"    -> 2,  "R!"
        
        z -> corner case -> row = 5, col = 1
        """
        #return self.find_shortest_path(target)
        return self.manhattan_distance(target)
    
    def find_shortest_path(self, target):
        path = ""
        row, col = 0, 0
        rows, cols = 6, 5
        for letter in target:
            next_row, next_col = self.get_position(cols, letter)
            path += self.bfs(row, col, next_row, next_col, rows, cols) + "!"
            row, col = next_row, next_col
        return path
    
    def get_connected(self, row, col):
        dirs = [(-1, 0, "U"), (0, -1, "L"), (0, 1, "R"), (1, 0, "D")] # make this order
        return [(row+r, col+c, move) for r, c, move in dirs]
    
    def bfs(self, start_row, start_col, target_row, target_col, rows, cols):
        visited = set()
        queue = deque([(start_row, start_col, "")])
        while queue:
            row, col, path = queue.popleft()
            if row == target_row and col == target_col:
                return path
            visited.add((row, col))
            
            for next_row, next_col, move in self.get_connected(row, col):
                is_visited = (next_row, next_col) in visited
                if 0 <= next_row < rows and 0 <= next_col < cols and not is_visited:
                    queue.append((next_row, next_col, path + move))
            
        return ""
        
    def manhattan_distance(self, target):
        path = []
        row, col = 0, 0
        for letter in target:
            new_row, new_col = self.get_position(5, letter)
            moves = ""
            # manhattan distance
            if row > new_row:
                moves += "U" * (row - new_row)
            if col > new_col:
                moves += "L" * (col - new_col)
            if row < new_row:
                moves += "D" * (new_row - row)
            if col < new_col:
                moves += "R" * (new_col - col)
            path.append(moves)
            path.append("!")
            row, col = new_row, new_col
        print(len("".join(path)))    
        return "".join(path)
    
    def get_position(self, cols, letter):
        # in constant time
        index = ord(letter) - ord("a")
        row = index // cols
        col = index % cols
        return row, col
        
        