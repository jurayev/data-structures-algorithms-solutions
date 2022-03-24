class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        start from 0, 0
        
        while row-1 and col+1
        turn right -> col+1 or row-1
        
        while row+1 and col-1
        turn left -> row-1 or col+1
        
        """
        
        row, col = 0, 0 # 0, 0
        rows, cols = len(mat), len(mat[row]) # 1, 2
        output = []
        while row < rows and col < cols:
            if row < rows and col < cols:
                output.append(mat[row][col])
      
            while row-1 >= 0 and col+1 < cols:
                row -= 1
                col += 1
                output.append(mat[row][col])
            # turn right
            if col+1 < cols:
                col += 1
            # turn down
            else:
                row += 1
            if row < rows and col < cols:
                output.append(mat[row][col])
            while row+1 < rows and col-1 >= 0:
                row += 1
                col -= 1
                output.append(mat[row][col])
            
            # turn down
            if row+1 < rows:
                row += 1
            # turn left
            else:
                col += 1
        return output