# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Complexity:
            Time O(N)
            Space O(N)
        
        """
        if not root:
            return 0
        
        current = 0
        left_res = 0
        right_res = 0
        if low <= root.val <= high:
            current += root.val
            left_res = self.rangeSumBST(root.left, low, high)
            right_res = self.rangeSumBST(root.right, low, high)
        elif high < root.val:
            left_res = self.rangeSumBST(root.left, low, high)
        else:
            right_res = self.rangeSumBST(root.right, low, high)
        return left_res + right_res + current