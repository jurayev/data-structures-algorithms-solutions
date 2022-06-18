class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        components = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                self.dfs(node, graph, visited)
                components += 1
        return components

    def dfs(self, source, graph, visited):
        
        visited.add(source)
        
        for dest in graph[source]:
            if dest not in visited:
                self.dfs(dest, graph, visited)
            
        