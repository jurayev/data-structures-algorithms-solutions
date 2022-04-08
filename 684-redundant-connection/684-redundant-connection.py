class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        
        {1} {2} {3}
        
        uf(1,2) -> {1,2} {3}
        uf(1,3) -> {1,2, 3}
        uf(2,3) -> answer
        
        Time O(N)
        Space O(N)
        """
        rank = [0] * 1001
        sets = [i for i in range(1001)]
        
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
        
        for source, dest in edges:
            if not union(source, dest):
                return [source, dest]
            
            
        return [-1, -1]
        