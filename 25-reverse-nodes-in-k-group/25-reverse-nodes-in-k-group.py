# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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