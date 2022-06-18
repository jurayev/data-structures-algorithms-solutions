"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
        
nodes = {

1: node1 -> [node2, node4]
2: node2 -> [node1, node3]
3: node3 -> [node2, node4]
4: node4 -> [node1, node3]
}
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        created_nodes = {}
        self.dfs(node, created_nodes)
        return created_nodes[1]
        
    
    def dfs(self, node, created_nodes):
        if node.val in created_nodes:
            return
        created_nodes[node.val] = Node(node.val)
        
        for next_node in node.neighbors:
            self.dfs(next_node, created_nodes)
            created_nodes[node.val].neighbors.append(created_nodes[next_node.val])