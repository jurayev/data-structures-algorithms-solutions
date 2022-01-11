class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        XOR solution
        
        Complexities:
            Time O(N^2)
            Space O(1)
        """
        n = len(matrix)
        
        xored = 0
        for i in range(1, n+1):
            xored ^= i
        
        for i in range(n):
            row = xored
            col = xored
            for j in range(n):
                row ^= matrix[i][j]
                col ^= matrix[j][i]
                
            if max(row, col) != 0:
                return False
        return True
        
    def checkValidWithSets(self, matrix: List[List[int]]) -> bool:
        """
        [[1,1,1],
         [1,2,3],
         [1,2,3]]
        
        Complexities:
            Time O(N^2)
            Space O(N+N)
        """
        n = len(matrix)
        
        for i in range(n):
            row = set() #
            col = set() #

            for j in range(n):
                row.add(matrix[i][j])
                col.add(matrix[j][i])
            
            if len(row) != n or len(col) != n:
                return False
        return True