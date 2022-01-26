# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Approach 1:
            Collect all integers from both trees, apply sorting over these numbers.
            Time O(n log n)
            Space O(n)
            
        Approach 2:
            Use BST properties to append the integer in the sorted order on the go.

            Time O(N+M)
            Space O(N+M)
        
        """
        root1_nums = []
        self.get_nums_of_bst(root1, root1_nums)
        root2_nums = []
        self.get_nums_of_bst(root2, root2_nums)
        
        merged = []
        root1_idx = 0
        root2_idx = 0
        
        while root1_idx < len(root1_nums) or root2_idx < len(root2_nums):
            num1 = root1_nums[root1_idx] if root1_idx < len(root1_nums) else float("inf")
            num2 = root2_nums[root2_idx] if root2_idx < len(root2_nums) else float("inf")
            if num1 < num2:
                merged.append(num1)
                root1_idx += 1
            else:
                merged.append(num2)
                root2_idx += 1
        
        return merged
    
    def get_nums_of_bst(self, root, nums):
        if not root:
            return
        
        self.get_nums_of_bst(root.left, nums)
        nums.append(root.val)
        self.get_nums_of_bst(root.right, nums)