class Solution:
    def findMinHeightTrees(self, nodes: int, edges: List[List[int]]) -> List[int]:
        """
        Approach:
            Topological sort solution
            
        Time Complexity O(V+E)
        Space Complexity O(V+E)
        
        Examples:
            [[0, 1], [1, 2], [1, 3], [2, 4]]

            0: 1
            1: 0, 2, 3
            2: 1, 4
            3: 1
            4: 2

            0: 1
            1: 3
            2: 2
            3: 1
            4: 1

            leaves = [0, 3, 4]
        """
        if nodes == 1:
            return [0]
        graph = collections.defaultdict(list)
        indegree = collections.Counter()
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
            indegree[source] += 1
            indegree[dest] += 1
            
        
        leaves = [source for source, value in indegree.items() if value == 1]
        
        total_nodes = nodes
        
        while total_nodes > 2:
            leaves_len = len(leaves)
            total_nodes -= leaves_len
            for _ in range(leaves_len):
                source = leaves.pop(0)
                for dest in graph[source]:
                    indegree[dest] -= 1
                    if indegree[dest] == 1:
                        leaves.append(dest)
                        
        return leaves
        