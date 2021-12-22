# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        use fast and slow pointer
        
        cut into two ll, then revert the second part
        two pointers, take nodes one by one and merge two lists
        
        TC O(n)
        SC O(1)
        
        [1,2,3,4 ,5,6]
           s
                f
        1->2->3
        
        5->4
        
        1->5->2->4->3
        """
        
        
        slow = head
        fast = head.next.next if head.next else head.next
        
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        
        first_head = head
        second_head = slow.next
        slow.next = None
        
        second_head = self.reverse(second_head)
        
        dummy = ListNode()
        new_head = dummy
        
        while first_head:
            new_head.next = first_head
            first_head = first_head.next
            new_head.next.next = second_head
            second_head = second_head.next if second_head else second_head
            new_head = new_head.next.next
            
        return dummy.next
    
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
        
        
        
        