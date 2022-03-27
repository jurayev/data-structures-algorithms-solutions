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
# Ex 1.
#         -10 -> -3 -> 0 -> 5 -> 9 -> null - Sorted Linked List
#        
#               0         -> Height-balanced BST
#             /   \
#           -10     5
#              \     \
#               -3     9
#        
# Ex 2.     
#         -10 -> -4 -> -3 -> 0 -> 4 -> 5 -> 6 -> 9 -> null - Sorted Linked List
#        
#               0         > Height-balanced BST
#             /     \
#           -4        5
#         /    \    /   \
#       -10     -3 4      6
#                          \ 
#                            9
class Solution:
    ############################################# Sol 1 # Time O(N), Space(logN)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.head = head
        node = head
        size = 0
        while node:
            size += 1
            node = node.next

        return self.make_bst(0, size-1)
        
    def make_bst(self, left_idx, right_idx):
        
        if left_idx > right_idx:
            return None
        mid_idx = (left_idx + right_idx) // 2
        left_tree = self.make_bst(left_idx, mid_idx-1)
        # in-order traversal
        tree = TreeNode(self.head.val)
        self.head = self.head.next
        
        right_tree = self.make_bst(mid_idx+1, right_idx)
        tree.left = left_tree
        tree.right = right_tree
        return tree
    ################################################## Sol 2 # Time (3N) Space (N) 
    def sortedListToBST1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
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