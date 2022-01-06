# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time O(N), N - number of nodes in tree
        Space O(M), M - longest level
        """
        
        queue = []
        if root:
            queue.append(root)
        levels = []
        while queue:
            next_level = []
            levels.append([el.val for el in queue])
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        return levels
                
            