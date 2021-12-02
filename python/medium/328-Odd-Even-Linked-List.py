# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        [2,1,3,5,6,4,7]
         0 1 2 3 4 5 6
         ^
        [2,3,6,7,1,5,4]

   even 0 -> 2 -> 3 -> 6 -> 7
                            ^
   odd  1 -> 1 -> 5 -> 4 -> None
                       ^

 merged 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4 -> None

        Time Complecity O(n)
        Space Complexity O(1)
        """

        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)

        even_head = even_dummy
        odd_head = odd_dummy

        node = head

        index = 0
        while node:
            if index % 2 == 0:  # even index
                even_head.next = node
                even_head = even_head.next
            else:  # odd index
                odd_head.next = node
                odd_head = odd_head.next

            node = node.next
            index += 1

        odd_head.next = None
        even_head.next = odd_dummy.next

        return even_dummy.next