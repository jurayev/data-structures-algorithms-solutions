# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next
        self.size = len(self.nodes)

    def getRandom(self) -> int:
        idx = randint(0, self.size-1)
        return self.nodes[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()