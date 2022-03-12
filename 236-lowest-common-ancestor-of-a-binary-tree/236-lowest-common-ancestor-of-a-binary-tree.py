# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', node1: 'TreeNode', node2: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if node1.val == root.val:
            return node1
        if node2.val == root.val:
            return node2
        
        left_node = self.lowestCommonAncestor(root.left, node1, node2)
        right_node = self.lowestCommonAncestor(root.right, node1, node2)
        if left_node and right_node:
            return root
        
        return left_node or right_node
        