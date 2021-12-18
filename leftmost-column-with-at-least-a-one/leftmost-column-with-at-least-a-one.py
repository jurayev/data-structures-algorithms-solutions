# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:	
        rows, cols = binaryMatrix.dimensions()

        col = cols               # 0
        for row in range(rows):  # 5		
            while col-1 >= 0 and binaryMatrix.get(row, col-1):  
                col -= 1

        return col if col < cols else -1
