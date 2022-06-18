class UnionFind:
    def __init__(self, size):
        self.size = size
        self.sizes = [1 for _ in range(self.size)]# node  0 1 2 3 4 
        self.sets = [i for i in range(self.size)] # root [0,0,0,3,3]
    
    def find(self, node):
        if node == self.sets[node]:
            return node
        self.sets[node] = self.find(self.sets[node])
        return self.sets[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.sizes[root1] > self.sizes[root2]:
                self.sets[root2] = self.sets[root1]
                self.sizes[root1] += self.sizes[root2]
            else:
                self.sets[root1] = self.sets[root2]
                self.sizes[root2] += self.sizes[root1]
            return 1
        return 0
                
                
        
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        graph = defaultdict(list)
        components = n
        for start, end in edges:
            components -= union_find.union(start, end)
       
        return components
        
    
    def countComponents_dfs_bfs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        components = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                self.bfs(node, graph, visited)
                components += 1
        return components
    
    def bfs(self, source, graph, visited):
        
        queue = deque([source])
        while queue:
            source = queue.popleft()
            visited.add(source)
            for dest in graph[source]:
                if dest not in visited:
                    queue.append(dest)
        
        
    
    def dfs_iterative(self, source, graph, visited):
        
        stack = [source]
        
        while stack:
            source = stack.pop()
            visited.add(source)
            for dest in graph[source]:
                if dest not in visited:
                    stack.append(dest)
        
        
        
    def dfs_recursive(self, source, graph, visited):
        
        visited.add(source)
        
        for dest in graph[source]:
            if dest not in visited:
                self.dfs(dest, graph, visited)
            
        