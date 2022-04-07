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
        [0,0,3,3,3,0]
        
        union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
        
        """
        sorted_relations = sorted(relations, key=lambda x: x[0])
        sets = [i for i in range(n)]
        sizes = {i: 1 for i in range(n)}
        num_components = n
        
        def find(node):
            # find the root of the node
            root = node
            while root != sets[root]:
                root = sets[root]
            # compressing the path
            while root != node:
                next_node = sets[node]
                sets[node] = root
                node = next_node
            return root
        
        def union(source, dest):
            root_source = find(source)
            root_dest = find(dest)
            # nothing to do if both from the same component
            if root_source == root_dest: return
            # check which component is larger
            # merge smaller with larger
            if sizes[root_source] > sizes[root_dest]:
                sets[root_source] = root_dest
                sizes[root_source] += sizes[root_dest]
            else:
                sets[root_dest] = root_source
                sizes[root_dest] += sizes[root_source]
            
            # decrement components after merge
            nonlocal num_components
            num_components -= 1
            
        for ts, source, dest in sorted_relations:
            union(source, dest)
            if num_components == 1:
                return ts
            
        return -1
            
        
        
        
