# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1: Collect every node and sort in the array, after link all together
        Time complexity O(nlogn)
        Space Complexity O(n)


        Approach 2: Collect every node and use min heap, after link it all together
        Time complexity O(nlogn)
        Space Complexity O(n)

        Approach 3: Keep k nodes in the min heap, after link it all together
        Time complexity O(nlogk)
        Space Complexity O(k)

        Examples:

        [
          1->4->5->None,
          ^
          1->3->4->None,
          ^
          2->6->None
          ^
        ]
        merging them into one sorted list:
        0->1->1->2->3->4->4->5->6
                       ^

        heap = [ (6,Node(6)),(4,Node(4)),(5,Node(5)),]
        heappush(heap, (3, ListNode(3)))
        heappush(heap, (1, ListNode(1)))
        heappush(heap, (2, ListNode(2)))
        """
        heap = []
        comp_counter = 0  # used for comparison in heap operations in case there are the same elements inside
        for node in lists:
            if not node:
                continue
            heappush(heap, (node.val, comp_counter, node))
            comp_counter += 1

        dummy = ListNode(0)  # this is to avoid linked list starting node overhead
        head = dummy
        while heap:
            val, _, node = heappop(heap)
            head.next = node
            head = head.next

            node = node.next
            if not node:
                continue
            heappush(heap, (node.val, comp_counter, node))
            comp_counter += 1

        return dummy.next
