class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        rank = [0] * 101
        sets = [i for i in range(101)]
        
        def find(node) -> int:
            # find parent/root node with path compression
            if sets[node] != node:
                sets[node] = find(sets[node])
            return sets[node]
        
        def union(node1, node2) -> bool:
            r_node1 = find(node1)
            r_node2 = find(node2)
            if r_node1 == r_node2: return False
            if rank[r_node1] > rank[r_node2]:
                sets[r_node2] = r_node1
                rank[r_node1] += 1
            else:
                sets[r_node1] = r_node2
                rank[r_node2] += 1
            return True

        for source in range(len(graph)):
            for j in range(0, len(graph[source])):
                if find(source) == find(graph[source][j]):
                    return False
                union(graph[source][0], graph[source][j])
                
        return True