class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        [[1,2],[2,3],[3,4],[5,1]] n = 6
        
        output = 4
        
        [[1,3],[2,3]] n = 3
        
        output = 2
        
        cache = {
        1: 4
        2: 3
        3: 2
        4: 1
        5: 0
        }
        
        Topological sort:
        
        1. Start from any node
        2. Visit the next node
        3. Keep track of visited(to skip visited and use cached results) and visiting(to find a cycle) nodes
        4. When backtrack remove visiting nodes one by one
        5. Choose next starting node
        
        The answer is longest path
        if cycle detected, there is no answer return -1
        
        TC O(V*E) SC O(2V*E)
        """
        graph = {i: [] for i in range(n)}
        
        for from_node, to_node in relations:
            graph[from_node-1].append(to_node-1)
            
        visiting = set()
        longest_path = -1
        in_cycle = []
        cache = {}
        for node in range(n):
            path = self.toposort(cache, graph, node, visiting, in_cycle)
            if in_cycle:
                return -1
            longest_path = max(longest_path, path)
            
        return longest_path
    
    
    def toposort(self, cache, graph, from_node, visiting, in_cycle):
        if from_node in visiting:
            in_cycle.append(True)
            return 0
        if from_node in cache:
            return cache[from_node]

        visiting.add(from_node)
        longest = 0
        for to_node in graph[from_node]:
            longest = max(longest, self.toposort(cache, graph, to_node, visiting, in_cycle))
        visiting.remove(from_node)
        cache[from_node] = longest + 1
        return cache[from_node]
        
        