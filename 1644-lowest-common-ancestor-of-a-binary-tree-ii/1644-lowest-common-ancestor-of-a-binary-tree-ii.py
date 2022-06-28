# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes = [p, q]
        lca = self.dfs(root, nodes)
        return lca if not nodes else None
        
        
    def dfs(self, root, nodes):
        if not root:
            return None
        
        
        left = self.dfs(root.left, nodes)
        right = self.dfs(root.right, nodes)
        
        if left and right:
            return root
        
        if root in nodes:
            nodes.remove(root)
            return root
        
        return left or right