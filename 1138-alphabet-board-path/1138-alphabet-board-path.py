class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        
        l -> 4 moves
        
        
        
        1. Return just min moves
                1. Sol Time O(K * N), Space O(1) -> Linear scan from 0,0 pos
                2. Sol Time O(K log N), Space O(1) -> bin search scan from 0,0 pos
        2. Return the sequence of min moves 
                -> remember the last position and add moves taken from last pos to the current
        3. Return the sequence of min moves, it is still sorted, there might be duplicates
        4. Return the sequence of min moves if letters are placed arbitrary on the board -> BFS to find shortest path O(K* N^2)
        
        aziggo
        
        azy -> DDDDD!URRRR! (only one path!)
        zdz
        
        "abcde", 
        "fghij", 
        "klmno", 
        "pqrst", 
        "uvwxy", 
        "z"
        
        "leet"
        "code"
        "zaz"
        "azdz"
        """
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
            
        return "".join(path)
    
    def get_position(self, cols, letter):
        # in constant time
        index = ord(letter) - ord("a")
        row = index // cols
        col = index % cols
        return row, col
        
        