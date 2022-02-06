class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # prefix sum for every row
        for r in range(1, len(self.prefix_matrix)): # 
            for c in range(1, len(self.prefix_matrix[r])):
                 self.prefix_matrix[r][c] += matrix[r-1][c-1] + self.prefix_matrix[r][c-1]
            
        # prefix sum for every column
        for c in range(1, len(self.prefix_matrix[0])):
            for r in range(1, len(self.prefix_matrix)):
                self.prefix_matrix[r][c] += self.prefix_matrix[r-1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        
        area_sum = self.prefix_matrix[row2][col2] - self.prefix_matrix[row1-1][col2] - self.prefix_matrix[row2][col1-1]
        return area_sum + self.prefix_matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
"""
[0,0,0,0,0]
[0,1,2,3,4] r = c =1
[0,0,2,0,4]
[0,0,2,0,4]

[1,2,3,4]
[0,2,0,4]
[0,2,0,4]

[1,3,6,10]
[0,2,2,6]
[0,2,2,6]

[1,3,6,10]
[0,5,8,16]
[0,7,10,22]

[1,x,6,x]
[0,5,8,16]
[0,x,10,x]
"""