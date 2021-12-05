# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """

        3                       3
     /      \
  2          3           2, 3             3 , 1
   \           \
      3         1          3            1

      res -> 7

               3                          3
             /      \
          4          5               4,4          5,1
       /    \           \
     1        3           1        0,0     2,2           1
   1   1      1  1     1       0,1    0,1
                               l k  r k
       res -> 9


     curr = node i + node left+2 + node right+2
     best = best left + best right)
        """
        return max(self.rob_houses(root))

    def rob_houses(self, root):
        if not root:
            return 0, 0

        not_rob_left, rob_left = self.rob_houses(root.left)
        not_rob_right, rob_right = self.rob_houses(root.right)

        return max(not_rob_left, rob_left) + max(not_rob_right, rob_right), not_rob_left + not_rob_right + root.val