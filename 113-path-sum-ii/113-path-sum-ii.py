# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        
        self.find_all_paths(root, 0, targetSum, [], paths)
        return paths
    
    def find_all_paths(self, root, curr_sum, target_sum, path, paths):
        if not root:
            return
        
        path.append(root.val)
        if curr_sum + root.val == target_sum and self.is_leaf(root):
            paths.append(path[:])
        
        self.find_all_paths(root.left, curr_sum + root.val, target_sum, path, paths)
        self.find_all_paths(root.right, curr_sum + root.val, target_sum, path, paths)
        
        path.pop()
        
    def is_leaf(self, node):
        return not node.left and not node.right