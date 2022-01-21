# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: reversing the nodes in k groups in-place.
        Time O(N)
        Space O(1)
        """
        
        dummy = ListNode()
        new_head = dummy
        
        node = head
        while node:
            rev_head = self.reverse(node, k)
            new_head.next = rev_head
            new_head = node
            node = node.next
        return dummy.next
    
    def reverse(self, head, k):
        """
        k = 2
        1->2->3->4->5
              ^
        2->1->4->3->5
                    ^
        """
        node = head
        count = 0
        while count < k and node:
            count += 1
            node = node.next
        if count < k: return head
        
        node, prev = head, None
        while k and node:
            k -= 1
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        head.next = node
        return prev
    
    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Simple approach using extra space and reversing the nodes in k groups
        Time O(N)
        Space O(N)
        """
        if k < 2:
            return head
        nodes = []
        
        node = head
        
        while node:
            nodes.append(node)
            node = node.next
            
        result = []
        for i in range(0, len(nodes), k):
            k_nodes = nodes[i:i+k]
            if len(k_nodes) == k:
                result.extend(k_nodes[::-1])
            else:
                result.extend(k_nodes)
            
        dummy_node = ListNode()
        new_head = dummy_node
        for node in result:
            new_head.next = node
            new_head = new_head.next
        new_head.next = None  
        return dummy_node.next