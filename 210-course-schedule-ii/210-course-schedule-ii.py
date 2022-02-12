UNVISITED = 0
VISITING = 1
VISITED = 2
IN_CYCLE = 3

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.toposort_dfs(numCourses, prerequisites)
        #return self.toposort_bfs(numCourses, prerequisites)
        
    def toposort_dfs(self, n, edges):
        order = []
        # Build a graph
        states = {i: UNVISITED for i in range(n)}
        graph = defaultdict(list)
        for source, dest in edges:
            graph[source].append(dest)
        
        for node in range(n):
            self.dfs(graph, states, node, order)
        all_visited = all(state == VISITED for state in states.values())
        return order if all_visited else []
    
    def dfs(self, graph, states, node, order):
        if states[node] == VISITED:
            return 
        if states[node] in [VISITING, IN_CYCLE]:
            states[node] = IN_CYCLE
            return 
        
        states[node] = VISITING
        
        for connected in graph[node]:
            self.dfs(graph, states, connected, order)
        
        if states[node] != IN_CYCLE:
            order.append(node)
            states[node] = VISITED
    
    def toposort_bfs(self, n, edges):
        """
        {0: [1, 2]
         1: [3]
         2: [3]
         3: []}
        
        indegree = {
        0: 0
        1: 1
        2: 1
        3: 2
        }
        
        Time O(V +E)
        Space O(V + E)
        """
        order = []
        # Build a graph
        graph = defaultdict(list)
        indegree = collections.Counter()
        for source, dest in edges:
            graph[dest].append(source)
            indegree[source] += 1
 
        queue = collections.deque()
        # Find all starting nodes
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                
        # BFS
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for connection in graph[node]:
                indegree[connection] -= 1
                if indegree[connection] == 0:
                    queue.append(connection)
            
        return order if len(order) == n else []
            