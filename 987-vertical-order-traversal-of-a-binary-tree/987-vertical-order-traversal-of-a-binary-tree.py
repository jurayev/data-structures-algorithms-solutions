# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        {
        0: {0:[1], 2:[6,5]}
        }
        """
        matrix = {}
        self.traverse(root, 0, 0, matrix)
        sorted_cols = sorted(matrix.items()) # [(0,{}), (1, {})]
        sorted_cols = [value for key, value in sorted_cols]
        sorted_rows = []
        for col in sorted_cols:
            rows = []
            for _, row in sorted(col.items()):
                rows.extend(row)
            sorted_rows.append(rows)
        return sorted_rows
        
    def traverse(self, root, col, row, matrix):
        if not root:
            return
        # pre-order
        if col not in matrix:
            matrix[col] = {}
        if row not in matrix[col]:
            matrix[col][row] = []
        # O(logN) for search, O(N) for insert
        bisect.insort(matrix[col][row], root.val)
        self.traverse(root.left, col-1, row+1, matrix)
        # in-order
        self.traverse(root.right, col+1, row+1, matrix)
        # post-order
        