# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        """
        1 -> 2 - > 3   -> 4 -> 5
                          ^
                        |
             1 -> 2 ->
                          ^
        
        
        """
        if not head_a or not head_b:
            return head_a
        node_a, node_b = head_a, head_b
        
        while node_a != node_b:
            node_a = node_a.next if node_a else head_b
            node_b = node_b.next if node_b else head_a
            
        return node_a
        
        
        
    def getIntersectionNode1(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        size_a, size_b = self.get_size(head_a), self.get_size(head_b)

        if size_a < size_b:
            head_b = self.shorten_list(head_b, size_b - size_a)
        else:
            head_a = self.shorten_list(head_a, size_a - size_b)

        while head_a and head_b:
            if head_a == head_b:
                return head_a
            head_a = head_a.next
            head_b = head_b.next
        return None

    def shorten_list(self, head, size):
        while size:
            head = head.next
            size -= 1
        return head

    def get_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
