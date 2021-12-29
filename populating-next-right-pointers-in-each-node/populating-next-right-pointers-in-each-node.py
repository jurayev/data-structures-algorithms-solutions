"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach 1:
            Use BFS to traverse level by level, connecting the next node on the same level
            
            Time O(N)
            Space O(N)
        
        Approach 2:
            Use DFS recursively and access the next node via parent node,
            if current node is right child of the parent, access the next node via parent.next
            
            Time O(N)
            Space O(1), N space for recursion stack which is not counter for this problem
        """
        self.dfs(root, False, None)
        return root
        
    def dfs(self, node, is_left, parent):
        if not node:
            return
        
        if parent:# link the nodes
            if is_left:
                node.next = parent.right
            else:
                node.next = parent.next.left if parent.next else None
        self.dfs(node.left, True, node)
        self.dfs(node.right, False, node)