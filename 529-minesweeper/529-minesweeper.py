class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        board = 
        [["E","E","E","E","E"],
         ["E","E","M","E","E"],
         ["E","E","E","E","E"],
         ["E","E","E","E","E"]], click = [3,0]
         
        Output: 
        [["B","1","E","1","B"],
         ["B","1","M","1","B"],
         ["B","1","1","1","B"],
         ["B","B","B","B","B"]]
        
        
        """
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            self.dfs(board, click[0], click[1])
        return board
    
    def check(self, board, x, y):
        if not(0 <= x < len(board) and 0 <= y < len(board[0])):
            return 0
        if board[x][y] == "M":
            return 1
        return 0
    
    def dfs(self, board, x, y):
        if not(0 <= x < len(board) and 0 <= y < len(board[0])):
            return
        if board[x][y] != "E":
            return
        mines = 0
        dirs = [(1,0), (-1, 0), (0,1), (0,-1), (-1,-1),(-1,1),(1,-1),(1,1)]
        for dirx, diry in dirs:
            mines += self.check(board, x+dirx, y+diry)
        if mines:
            board[x][y] = str(mines)
            return
        board[x][y] = "B"
        
        for dirx, diry in dirs:
            self.dfs(board, x+dirx, y+diry)
        
        return 0