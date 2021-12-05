# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        node = self.LCA(root, startValue, destValue)

        start_path = self.get_path(node, startValue)
        dest_path = self.get_path(node, destValue)

        # need to replace all with U in start_path
        return "U" * len(start_path) + dest_path

    def get_path(self, root, target):
        q = [(root, "")]

        while q:
            node, path = q.pop()
            if node.val == target:
                return path

            if node.left:
                q.append((node.left, path + "L"))
            if node.right:
                q.append((node.right, path + "R"))

    def LCA(self, root, start, dest):
        if not root:
            return root
        if root.val == start:
            return root
        if root.val == dest:
            return root

        left = self.LCA(root.left, start, dest)
        right = self.LCA(root.right, start, dest)

        if left and right:
            return root

        return left if left else right