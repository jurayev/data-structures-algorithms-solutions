# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
                      3
                   /		\
              5				 1
           /    \		/		\
        6		2		0		8
            /		\
            7	    4
           /
        11	
        
        LCA(11, 4) -> 2
        LCA(11, 8) -> 3
        LCA(4, 5) -> 5
        LCA(6, 3) -> 3
        Time O(N)
        Space O(N)
        """
        return self.find_lca(root, p, q)
    
    def find_lca(self, root, node1, node2):
        if not root:
            return None
        if root.val == node1.val or root.val == node2.val:
            return root

        left_node = self.find_lca(root.left, node1, node2)
        right_node = self.find_lca(root.right, node1, node2)

        if left_node and right_node:
            return root
        return left_node or right_node
