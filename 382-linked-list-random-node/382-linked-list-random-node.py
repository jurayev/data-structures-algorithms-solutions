# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randint

class Solution:
     
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """
        getRandom() -> reservoir sampling
            Time Complexity O(N)
            Space Complexity O(1)
        """
        total = 0
        node = self.head
        picked_element = self.head.val
        while node:
            if randint(0, total) == 0:
                picked_element = node.val
            
            node = node.next
            total += 1
        return picked_element

class Solution1:
    """
    getRandom()
        Time Complexity O(1)
        Space Complexity O(N)
    """
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