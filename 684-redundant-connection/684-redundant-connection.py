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
        seen = set()
        for source, dest in edges:
            seen.add(source)
            seen.add(dest)
        n = len(seen)
        sets = [i for i in range(n+1)]
        
        def find(node) -> int:
            # find parent/root node with path compression
            if sets[node] != node:
                sets[node] = find(sets[node])
            return sets[node]
        
        def union(node1, node2) -> bool:
            r_node1 = find(node1)
            r_node2 = find(node2)
            if r_node1 == r_node2: return False
            sets[r_node1] = r_node2
            return True
        
        for source, dest in edges:
            if not union(source, dest):
                return [source, dest]
            
            
        return [-1, -1]
        