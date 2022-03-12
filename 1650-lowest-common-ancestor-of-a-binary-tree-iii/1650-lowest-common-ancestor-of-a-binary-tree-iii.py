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
        nodes = set()
        self.find_root(node1, nodes)
        node = self.find_root(node2, nodes)
        return node
    
    def find_root(self, node, nodes):
        if not node:
            return None
        if node.val in nodes:
            return node
        nodes.add(node.val)
        return self.find_root(node.parent, nodes)