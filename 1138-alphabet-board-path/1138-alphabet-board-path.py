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
        """
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        path = []
        row, col = 0, 0 # 5, 1
        rows, cols = len(board), len(board[0])
        for letter in target:
            new_row, new_col = self.search(cols, letter)
            x_axis, y_axis = "", ""
            # manhattan distance
            if row < new_row:
                moves = new_row - row
                y_axis = "D" * moves
            elif row > new_row:
                moves = row - new_row
                y_axis = "U" * moves
            if col < new_col:
                moves = new_col - col
                x_axis = "R" * moves
            elif col > new_col:
                moves = col - new_col
                x_axis = "L" * moves
            need_swap = new_row == rows-1 and new_col == 0
            if need_swap:
                path.append(x_axis)
                path.append(y_axis)
            else:
                path.append(y_axis)
                path.append(x_axis)
            path.append("!")
            row, col = new_row, new_col
            
        return "".join(path)
    
    def search(self, cols, letter):
        # in constant time
        index = ord(letter) - ord("a")
        row = index // cols # 4 // 5 -> 0 $ 5 // 5 -> 1 # 9 // 5 -> 1 # 26 // 5 -> 5
        col = index % cols
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         if board[row][col] == letter:
        #             return row, col
        return row, col
        
        