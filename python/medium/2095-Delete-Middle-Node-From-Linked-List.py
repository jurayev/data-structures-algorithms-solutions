# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(N)
        Space O(1)

        Approach: Using fast and slow pointers to find the middle node


        [1,3,4,7,1,2,6]
               s
                       f

        [1,2]
           s
             f
        [1,2,3,4]
           s
               f
        """
        if not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head