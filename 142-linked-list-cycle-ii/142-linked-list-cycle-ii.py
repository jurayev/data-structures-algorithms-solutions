# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(N)
        Space Complexity O(1)
        """
        if not head:
            return None
        
        # find cycle
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # cycle found
                break

        if not fast or not fast.next:
            # there is not cycle, return -1
            return None

        # start from the node in cycle and the head node at the same time
        node1, node2 = head, slow
        
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
            
        return node1
        