# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel_node = ListNode(val=float("-inf"))
        node = head
        
        while node:
            next_node = node.next
            sorted_node = sentinel_node # -inf -> 1 -> 2 -> 3 -> 4 -> none
            while sorted_node.next and node.val > sorted_node.next.val:
                sorted_node = sorted_node.next
            node.next = sorted_node.next
            sorted_node.next = node
            node = next_node
        
        return sentinel_node.next