# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: 
            O(log N) Average
            O(N) Worst
        
        Space Complexity:
            O(log N) Average
            O(N) Worst
        """
        return self.search(root, p.val, q.val)
    
    def search(self, root, min_val, max_val):
        if not root:
            return None
        if min_val < root.val and max_val < root.val:
            # left
            return self.search(root.left, min_val, max_val)
        if min_val > root.val and max_val > root.val:
            # right
            return self.search(root.right, min_val, max_val)
        return root