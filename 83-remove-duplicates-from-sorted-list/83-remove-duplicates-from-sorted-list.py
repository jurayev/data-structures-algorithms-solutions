# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity O(N)
        Space Complexity O(1)
        
        Examples:
        dummy -> inf -> 1 -> 2 -> 3
                        ^
                 
        head -> 1 -> 1 -> 2 -> 3 -> 3
                                    ^
        """
        
        dummy_head = ListNode(val=float("inf"))
        curr_tail = dummy_head
        node = head
        while node:
            if node.val != curr_tail.val:
                curr_tail.next = node
                curr_tail = curr_tail.next
            node = node.next
        
        curr_tail.next = None
            
        
        return dummy_head.next