# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        
        map = {
        1: [8,2]
        0: [3,0]
        -1: [9,5]
        -2: [4]
        1: [8]
        
        }
        
        q = [, (0, 0), (1, 0), (7, 2)]
        
        (3, 0)
        (9, -1)
        (8, 1)
        (4,-2) 
        
        0: [3,0,1]
        -1: [9]
        -2: [4]
        1: [8]
        2: [7]
        """
        levels = defaultdict(defaultdict)
        self.dfs(root, 0, 0, levels)

        order = [(key, value) for key, value in levels.items()]
        order.sort(key=lambda x: x[0])
        vertical_order = []

        for _, level in order:
            flattened = []
            for idx in range(0, 101):
                for val in level.get(idx, []):
                    flattened.append(val)
            vertical_order.append(flattened)
        return vertical_order
    
    def dfs(self, node, column, row, levels):
        if not node:
            return 
        if row not in levels[column]:
            levels[column][row] = []
        levels[column][row].append(node.val)
        self.dfs(node.left, column - 1, row+1, levels)
        self.dfs(node.right, column + 1, row+1, levels)
    
        
        