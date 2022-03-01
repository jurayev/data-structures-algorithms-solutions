# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        
        subproblems:
            1. rob current node
            2. not rob current node
        recurrence:
            1. find max amount can be robbed for current node
            2. pass to the parent: 
                            current robbed
                            current not robbed
                            max so far
        base cases:
            if not root:
                return current, max_so_far (0, float(-inf))
        
        answer : rob(root) -> max amount can be robbed
        
        Compelexity:
                Time (V*E)
                Space (V*E)
        """
        return max(self.rob_houses(root))
        
    def rob_houses(self, root):
        if not root:
            return 0, 0, float(-inf)
        
        left_robbed, left_not_robbed, left_max = self.rob_houses(root.left)  # 1, 0, 1
        right_robbed, right_not_robbed, right_max = self.rob_houses(root.right) # 3, 0, 3
        
        curren_robbed = left_not_robbed + right_not_robbed + root.val # 4
        current_not_robbed = max(left_robbed, left_not_robbed) + max(right_robbed, right_not_robbed)
        max_robbed = max(left_max + right_max, curren_robbed, current_not_robbed) # 1, 3, 4
        
        return curren_robbed, current_not_robbed, max_robbed
    
    