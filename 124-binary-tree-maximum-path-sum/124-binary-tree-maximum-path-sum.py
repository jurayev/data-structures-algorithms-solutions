# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root)[1]
        
    def dfs(self, root):
        if not root:
            return 0, float(-inf)
        left_branch_sum, best_left = self.dfs(root.left)
        right_branch_sum, best_right = self.dfs(root.right)
       
        sum_via_root = left_branch_sum + root.val + right_branch_sum
        left_sum_with_root = left_branch_sum + root.val
        right_sum_with_root = right_branch_sum + root.val
        
        
        best_branch = max(left_sum_with_root, right_sum_with_root, root.val)
        best_subtree = max(best_left, best_right)
        best_so_far = max(best_branch, best_subtree, sum_via_root)
        
        return best_branch, best_so_far
