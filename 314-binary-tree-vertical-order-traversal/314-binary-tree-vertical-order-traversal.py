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
        return self.bfs(root)
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
        
    def bfs(self, root):
        order = defaultdict(list)
        if not root:
            return []
        q = deque([(root, 0)])
        while q:
            node, column = q.popleft()
            order[column].append(node.val)
            if node.left:
                q.append((node.left, column - 1))
            if node.right:
                q.append((node.right, column + 1))
        vertical_order = [(key, value) for key, value in order.items()]
        vertical_order.sort(key=lambda x: x[0])
        return [order for _, order in vertical_order]
        
        