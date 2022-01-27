from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Put all nodes into the min_heap, always remove the min node. 
        Move pointer of the current node one step forward and push to the min_heap again

        Time (N log K)
        Space O(N)
        """
        min_heap = []
        list_id = 0
        for linked_list in lists:
            if linked_list:
                heappush(min_heap, (linked_list.val, list_id, linked_list))
                list_id += 1
        
        sentinel_head = ListNode()
        sentinel_tail = sentinel_head

        while min_heap:
            value, list_id, linked_list = heappop(min_heap)
            sentinel_tail.next = linked_list
            sentinel_tail = sentinel_tail.next

            if linked_list.next:
                heappush(min_heap, (linked_list.next.val, list_id, linked_list.next))

        sentinel_tail.next = None
        return sentinel_head.next
