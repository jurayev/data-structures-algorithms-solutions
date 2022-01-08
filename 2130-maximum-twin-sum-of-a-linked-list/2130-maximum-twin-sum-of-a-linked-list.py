# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        From BiWeekly Contest 69, Q2
        Submission time - 0:12:29
        Time Spent - 6 min
        
        Complexities:
            Time O(N)
            Space O(N)
        """
        nodes = []
        
        node = head
        
        while node:
            nodes.append(node.val)
            node = node.next
            
        start, end = 0, len(nodes)-1
        
        best = 0
        while start < end:
            best = max(best, nodes[start]+nodes[end])
            start += 1
            end -= 1
        
        return best