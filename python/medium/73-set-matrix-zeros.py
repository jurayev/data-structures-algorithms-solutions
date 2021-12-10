class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
           [rc, c,2,c],
           [r, 4,5,2],
           [r, 0,1,5]

        """
        is_column = False

        n = len(matrix)
        m = len(matrix[0])

        for r in range(n):
            if matrix[r][0] == 0:
                is_column = True

            for c in range(1, m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for c in range(1, m):
            if matrix[0][c] == 0:
                for r in range(n):
                    matrix[r][c] = 0

        for r in range(1, n):
            if matrix[r][0] == 0:
                for c in range(m):
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(m):
                matrix[0][c] = 0

        if is_column:
            for r in range(0, n):
                matrix[r][0] = 0

    def setZeroesConstantSpace(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Examples:
           [r ,c,2,c],
           [3, 4,5,2],
           [r, 0,1,5]

            [0 ,0,0,0],
            [3, 0,5,0],
            [0, 0,0,0]

             [[x][x],
              [1][1],
              [0][0]]

          [[r,3,6,9,7,8,c,6],
           [0,3,7,0,0,4,3,8],
           [5,3,6,7,1,6,2,6],
           [8,7,2,5,0,6,4,0],
           [0,2,9,9,3,9,7,3]]

         Complexity:

             TC O(NM + NM)
             SC O(1)
        """
        n = len(matrix)
        m = len(matrix[0])
        # handle corner case when matrix[0][0] is 0
        if matrix and matrix[0] and matrix[0][0] == 0:
            matrix[0][0] = 'rc'

        # mark all rows and columns as to be processed
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    if col == 0 and matrix[0][0] == 'r':
                        matrix[0][col] = 'rc'
                    elif matrix[0][col] != 'rc':
                        matrix[0][col] = 'c'

                    matrix[row][0] = 'r' if matrix[row][0] != 'rc' else matrix[row][0]

        # make zeros for all rows marked with 'r' except the 1st row
        for row in range(1, n):
            if matrix[row][0] == 'r':
                for col in range(0, m):
                    matrix[row][col] = 0
        # make zeros for all columns marked with 'c' except the 1st column
        for col in range(1, m):
            if matrix[0][col] == 'c':
                for row in range(0, n):
                    matrix[row][col] = 0

        # make zeros except the matrix[0][0]
        for row in range(1, n):
            matrix[row][0] = 0 if matrix[0][0] in ['rc', 'c'] else matrix[row][0]

        # make zeros except  the matrix[0][0]
        for col in range(1, m):
            matrix[0][col] = 0 if matrix[0][0] in ['rc', 'r'] else matrix[0][col]

        # make zeros for the first column
        for row in range(n):
            matrix[row][0] = 0 if matrix[row][0] in ['r', 'rc'] else matrix[row][0]
        # make zeros for the first row
        for col in range(m):
            matrix[0][col] = 0 if matrix[0][col] in ['c', 'rc'] else matrix[0][col]

    def setZeroesUsingSets(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            matrix[r] = [0 for _ in range(m)]

        for c in cols:
            for r in range(n):
                matrix[r][c] = 0