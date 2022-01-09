class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        [   [1,1,1],
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