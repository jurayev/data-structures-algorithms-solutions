# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0


"""
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, res, 0)
        return res[0]

    def dfs(self, root, res, curr_number):
        if not root: return
        curr_number = (curr_number << 1) | root.val
        if not root.left and not root.right:
            res[0] += curr_number

        self.dfs(root.left, res, curr_number)
        self.dfs(root.right, res, curr_number)
            
        
        
    def sumRootToLeaf1(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, [], res)
        return int(res[0]/2)

    def dfs1(self, root, bits, res):
        if not root:
            num = int("".join(bits), 2)
            res[0] += num
            return 
        bits.append(str(root.val))
        self.dfs(root.left, bits, res)
        self.dfs(root.right, bits, res)
        bits.pop()
        