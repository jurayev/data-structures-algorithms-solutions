# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestorIteratively(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        N - number of nodes in the tree
        Time Complexity O(N)
        Space Complexity O(N)

        Approach: Solve Iteratively using parent link to find LCA

        Example:

                           3
                        /     \
                     5          1
                   /.  \      /.   \
                  6    2     0      8
               /         \
              7           4
        p = 7
        q = 2
        LCS = 5
        """
        # parent_nodes = {3:None, 5:3, 1:3, 6:5, 2:5, 0:1, 8:1, 7:2, 4:2}
        parent_nodes = {root: None}
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                parent_nodes[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_nodes[node.right] = node
                stack.append(node.right)

        left = q
        parents = set()
        while left:
            parents.add(left)
            left = parent_nodes[left]

        right = p
        while right not in parents:
            right = parent_nodes[right]
        return right

    def lowestCommonAncestorRecursively(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        N - number of nodes in the tree
        Time Complexity O(N)
        Space Complexity O(N)

        Approach: Solve recursively
        """
        if not root:
            return None

        if p == root:
            return root

        if q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right