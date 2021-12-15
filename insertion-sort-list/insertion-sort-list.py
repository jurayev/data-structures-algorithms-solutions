# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        4 -> 2 -> 1 -> 3 -> None
                       ^
        
    -inf 1 -> 2 -> 4 -> None
              ^ 
        """
        
        start_node = ListNode()
        curr = head
        while curr:
            sorted_node = start_node
            while sorted_node.next and sorted_node.next.val < curr.val:
                sorted_node = sorted_node.next
            
            temp = curr.next
            curr.next = sorted_node.next
            sorted_node.next = curr
            curr = temp
        
        return start_node.next
        
        
        
    def insertionSortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Examples:
        
        in =     4 -> 2 -> 1 -> 3 -> None
                 ^
           
        sorting= 4 -> 2 -> 3 -> 1 -> None
                 ^
        out =    1 -> 2 -> 3 -> 4 -> None
        
        
        start from the end and process one node at a time
        
        reverse list
        return new_head
        
        """
        new_head = self.sort(head)
        new_head = self.reverse(new_head)
        return new_head
        
    def sort(self, node):
        if node.next:
            pre_node = self.sort(node.next)
            node.next = pre_node
        
        dummy = ListNode()
        curr_head = dummy
        curr = node
        while curr.next:
            if curr.val >= curr.next.val:
                break
            temp = curr.next
            curr.next = curr.next.next
            temp.next = curr
            curr_head.next = temp
            curr_head = curr_head.next

        return dummy.next or node
    
    def reverse(self, node):
        prev = None # 3->2->1->None
        curr = node # 
        while curr:
            temp = curr.next  # 2
            curr.next = prev #1->None
            prev = curr
            curr = temp
        return prev