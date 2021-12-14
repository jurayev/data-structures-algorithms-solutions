# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = None
        node = head
        
        while node:  # 3 -> 4 -> 5
            next_node = node.next # 3
            node.next = new_head #  2-> 1-> 0 
            new_head = node      #  2-> 1-> 0 
            node = next_node     
        
        return new_head
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head, node = self.reverse(head)
        return new_head
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:       # 5 -> 4 -> 3 -> 2 -> 1
        if not head:
            return head, head
        if head.next:
            new_head, node = self.reverse(head.next)
            node.next = head
            head.next = None
            return new_head, node.next

        return head, head