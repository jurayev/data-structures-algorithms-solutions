class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        start from 0, 0
        
        while row-1 and col+1
        turn right -> col+1 or row-1
        
        while row+1 and col-1
        turn left -> row-1 or col+1
        
        """
        
        row, col = 0, 0 # 3, 0
        rows, cols = len(mat), len(mat[row]) # 1, 2
        output = []
        while row < rows and col < cols:
            # if row < rows and col < cols:
            #     output.append(mat[row][col])
      
            while row >= 0 and col < cols:
                output.append(mat[row][col])
                row -= 1
                col += 1
                
            # turn right
            if col < cols:
                row += 1
            # turn down
            else:
                row += 2
                col -= 1
            # if row < rows and col < cols:
            #     output.append(mat[row][col])
            while row < rows and col >= 0:
                output.append(mat[row][col])
                row += 1
                col -= 1
                
            # turn down
            if row < rows:
                col += 1
            # turn left
            else:
                row -= 1
                col += 2
        return output