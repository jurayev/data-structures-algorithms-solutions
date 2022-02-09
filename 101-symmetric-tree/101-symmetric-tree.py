# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        
        while stack:
            node1, node2 = stack.pop()
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            if not node1 and not node2:
                continue
            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True
        
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check_symmetric(root.left, root.right)
    
    
    def check_symmetric(self, root1, root2):
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        
        return self.check_symmetric(root1.left, root2.right) \
        and self.check_symmetric(root1.right, root2.left)