class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        uf = UnionFind(n)
        
        for source, dest in edges:
            if not uf.union(source, dest):
                return False
        return True


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.sets = [i for i in range(size)]
        # sizes of the sets
        self.sizes = [1 for i in range(size)] 
    
    def find(self, node):
        # find the root with path compression
        if self.sets[node] != node:
            self.sets[node] = self.find(self.sets[node])
        return self.sets[node]
    
    def union(self, source, dest):
        source_root = self.find(source)
        dest_root = self.find(dest)
        if source_root == dest_root: return False
        # merge smaller to bigger sets
        if self.sizes[source_root] > self.sizes[dest_root]:
            self.sets[dest_root] = source_root
            self.sizes[source_root] += self.sizes[dest_root]
        else:
            self.sets[source_root] = dest_root
            self.sizes[dest_root] += self.sizes[source_root]
            
        return True