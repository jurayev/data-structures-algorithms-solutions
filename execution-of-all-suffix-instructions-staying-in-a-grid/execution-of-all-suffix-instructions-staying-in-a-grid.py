class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        """
        Apprach:
            Perform brute force simulation
        
        Examples:
        n = 3, startPos = [0,1], s = "RRDD L U"
                                      1111-1-1
                                       R    R    D    D    L    U
                                [0,1][0,2][0,3][1,3][2,3][2,2][1,2] 
        
        TC O(N^2)
        SC O(N)
        """
        dirs = {"R": [0, 1], "L": [0, -1], "D":[1, 0], "U":[-1, 0]}
        exucuted = []
        for i in range(len(s)):
            curr_pos = startPos
            total_moves = 0
            for j in range(i, len(s)):
                move = s[j]
                row, col = curr_pos
                row_step, col_step = dirs[move]
                curr_pos = [row+row_step, col+col_step]
  
                if not (0 <= curr_pos[0] < n and 0 <= curr_pos[1] < n):
                    break
                total_moves += 1
            exucuted.append(total_moves)
        return exucuted