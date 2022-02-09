# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        
                6
             /     \
           3         8
         /   \      /  \
        1      3   7     10
         \    /  \
          2  2    4
        """
        return self.is_valid(root, float("-inf"), float("inf"))
        
        
    def is_valid(self, root, lower_bound, upper_bound):
        if not root:
            return True
        
        if not (lower_bound < root.val < upper_bound):
            return False
        
        return self.is_valid(root.left, lower_bound, root.val) \
            and self.is_valid(root.right, root.val, upper_bound)
        
        