"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
    "53"
"""

class Solution:
    def lowestCommonAncestor(self, node1: 'Node', node2: 'Node') -> 'Node':
        node1_path = self.find_root(node1)
        node2_path = self.find_root(node2)
        for node in node2_path:
            if node in node1_path:
                return node
        return node1
    
    def find_root(self, node):
        if not node:
            return []
        
        path = [node]
        path.extend( self.find_root(node.parent))
        return path