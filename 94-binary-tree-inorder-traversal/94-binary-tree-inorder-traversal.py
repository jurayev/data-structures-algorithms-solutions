# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        self.dfs(root, nodes)
        return nodes
    
    def dfs(self, root, nodes):
        if not root:
            return
        
        self.dfs(root.left, nodes)
        nodes.append(root.val)
        self.dfs(root.right, nodes)