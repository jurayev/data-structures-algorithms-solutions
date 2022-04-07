class Solution:
    def earliestAcq(self, relations: List[List[int]], n: int) -> int:
        """
        n = 6
        [timestampi, xi, yi]
        [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], 
             0                  1                  2               3
        
        [20190224, 2, 4], [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]]
            4                 5                 6               7
        
        {0,1,5, 2,3,4}
        union(0,1)
        union(3,4)
        union(2,3)
        union(1,5)
        union(2,4)
        union(0,3) -> 20190301
        union(1,2)
        union(4,5)
        
        0: 3
        3: 3
         0,1,2,3,4,5
        [0,1,2,3,3,5]
        find(4) -> 4
        find(4) -> 
            find(3) -> 3
        find(4) -> 3
        union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
        
        """
        sorted_relations = sorted(relations, key=lambda x: x[0])
        union_find = UnionFind(n)
            
        for ts, source, dest in sorted_relations:
            union_find.union(source, dest)
            if union_find.size == 1:
                return ts
            
        return -1
    
class UnionFind:
    def __init__(self, size):
        self.size = size
        self.sets = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
    
    def find(self, node):
        # find the root with path compression
        if self.sets[node] != node:
            self.sets[node] = self.find(self.sets[node])
        return self.sets[node]
    
    def union(self, source, dest):
        source_root = self.find(source)
        dest_root = self.find(dest)
        if source_root == dest_root: return
        # merge smaller to bigger sets
        if self.sizes[source_root] > self.sizes[dest_root]:
            self.sets[dest_root] = source_root
            self.sizes[source_root] += self.sizes[dest_root]
        else:
            self.sets[source_root] = dest_root
            self.sizes[dest_root] += self.sizes[source_root]
            
        self.size -= 1
            
        
        
        
