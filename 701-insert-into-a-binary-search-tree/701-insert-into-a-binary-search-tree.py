# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searching insert position using BST properties.
        Complexities:
            Time O(log N) - N is the number of nodes
            Space O(log N) - for recursion stack
        """
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

        
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.insert(root, val)
        return root
    
    
    def insert1(self, root, val):
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
                return
            self.insert(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
                return
            self.insert(root.right, val)
        