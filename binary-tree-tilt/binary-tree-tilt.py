# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity O(N)
        Space complexity O(N), keeping the recursive stack takes N space
        """
        total, tilt = self.dfs(root)
        return tilt
    
    
    def dfs(self, root):
        if not root:
            return 0, 0
        
        left_total, left_tilt = self.dfs(root.left)
        right_total, right_tilt = self.dfs(root.right)
        
        return left_total + right_total + root.val, abs(left_total - right_total) + left_tilt + right_tilt