# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.group_nodes_by_odd_even_property(head)
        
    def group_nodes_by_odd_even_property(self, head: ListNode) -> ListNode: # 1 -> 2 -> null
	
        odd_head = ListNode(0) # 0 -> 1 -> null
        odd_tail = odd_head # 1 -> null
        even_head = ListNode(0) # 0 -> 2 -> null
        even_tail = even_head # 2 -> null

        node = head  # -> null
        while node and node.next:
            odd_tail.next = node
            odd_tail = odd_tail.next
            node = node.next
            even_tail.next = node
            even_tail = even_tail.next
            node = node.next
            
        even_tail.next = None    
        if node:  # null
            odd_tail.next = node
            odd_tail = odd_tail.next
        # link two LL
        odd_tail.next = even_head.next # 0 -> 1 -> 2 -> null
        return odd_head.next #  1 -> 2 -> null
