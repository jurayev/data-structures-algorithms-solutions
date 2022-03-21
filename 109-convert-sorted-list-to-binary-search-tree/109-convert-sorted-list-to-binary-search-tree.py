# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        [-10,-3,0,5,9]
        
              0
            /   \
          -10     5
             \     \
              -3     9
        
        
        [-10,-4,-3 ,0,4,4, 5, 9]
        
              0
            /     \
          -4        5
        /    \    /   \
      -10     -3 4      6
                         \ 
                           9
        """
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        return self.build_bst(values)
    
    def build_bst(self, values):
        if not values:
            return None
        mid_idx = len(values) // 2
        left_tree = self.build_bst(values[:mid_idx])
        right_tree = self.build_bst(values[mid_idx+1:])
        root = TreeNode(values[mid_idx], left_tree, right_tree)
        return root