"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        """
        Time Complexity O(V+E), where V is total vertices, E is total edges
        Space Complexity O(V)

        Approach: Implement BFS

        Examples:
            Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
            Output: [[2,4],[1,3],[2,4],[1,3]]
            Explanation: There are 4 nodes in the graph.
            1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
            3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

        """
        if not node: return node

        clones = {node.val: Node(node.val)}
        queue = collections.deque([node])
        while queue:
            node_to_clone = queue.popleft()
            clone_node = clones[node_to_clone.val]

            for neigh in node_to_clone.neighbors:
                if neigh.val not in clones:
                    queue.append(neigh)
                    clones[neigh.val] = Node(neigh.val)
                clone_node.neighbors.append(clones[neigh.val])
        return clones[node.val]

    def cloneGraphIterativeDFS(self, node: 'Node') -> 'Node':
        """
        Time Complexity O(V+E), where V is total vertices, E is total edges
        Space Complexity O(V)

        Approach: Implement DFS

        Examples:
            Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
            Output: [[2,4],[1,3],[2,4],[1,3]]
            Explanation: There are 4 nodes in the graph.
            1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
            3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

        """
        if not node:
            return node
        clones = {node.val: Node(node.val)}
        stack = [node]  # 2, 3

        while stack:
            node_to_clone = stack.pop()
            clone = clones[node_to_clone.val]

            for neigh in node_to_clone.neighbors:
                if neigh.val not in clones:
                    clones[neigh.val] = Node(neigh.val)
                    stack.append(neigh)

                clone.neighbors.append(clones[neigh.val])

        return clones[node.val]

    def cloneGraphRecursiveDFS(self, node: 'Node') -> 'Node':
        """
        Time Complexity O(V+E), where V is total vertices, E is total edges
        Space Complexity O(V)

        Approach: Implement DFS

        Examples:
            Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
            Output: [[2,4],[1,3],[2,4],[1,3]]
            Explanation: There are 4 nodes in the graph.
            1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
            3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
            4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

        """
        if not node:
            return node
        clones = {}

        new_node = self.dfs(node, clones)

        return new_node

    def dfs(self, node, clones):
        if node.val in clones:
            return clones[node.val]

        clone_node = Node(node.val)
        clones[node.val] = clone_node

        for connected in node.neighbors:
            clone_connected_node = self.dfs(connected, clones)
            clone_node.neighbors.append(clone_connected_node)

        return clone_node