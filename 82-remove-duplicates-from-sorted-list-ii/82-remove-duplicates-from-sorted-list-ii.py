# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        new_head -> inf ->  1 -> 2 -> 5
                                 pt               
        
        1 -> 2 -> 3 -> 3 -> 3 -> 4 ->4 ->5
                                         ^
                                           
        Time O(N)
        Space O(1)
        """
        
        new_head = ListNode(float(inf))
        new_tail = new_head
        prev_tail = new_head
        
        node = head
        while node:
            if new_tail.val == node.val:
                while node and new_tail.val == node.val:
                    node = node.next
                new_tail = prev_tail
            
            prev_tail = new_tail
            prev_tail.next = None
            
            new_tail.next = node
            new_tail = new_tail.next
            
            node = node.next if node else None
            
        return new_head.next