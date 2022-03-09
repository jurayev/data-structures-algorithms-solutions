class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        
        [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]
         
         1. DFS
         2. BFS
        """
        visiting = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(row, col, board, 0, word, visiting):
                    return True
                
        return False
        
    def dfs(self, row, col, board, index, word, visiting):
        if index >= len(word):
            return True
        
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return False
        
        if board[row][col] != word[index] or (row, col) in visiting:
            return False
        visiting.add((row, col))
        up_dfs = self.dfs(row+1, col, board, index + 1, word, visiting)
        down_dfs = self.dfs(row-1, col, board, index + 1, word, visiting)
        right_dfs = self.dfs(row, col+1, board, index + 1, word, visiting)
        left_dfs = self.dfs(row, col-1, board, index + 1, word, visiting)
        visiting.remove((row, col))
        return up_dfs or down_dfs or right_dfs or left_dfs
        