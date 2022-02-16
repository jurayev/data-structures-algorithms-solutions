class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        1: []
        2: [1]
        3: [1, 2]
        
        1 -> 2 -> 3
        """
        graph = defaultdict(list)
        indegree = Counter()
        for source, dest in prerequisites:
            graph[source].append(dest)
            indegree[dest] += 1
            indegree[source] += 0
            
        reachable = defaultdict(set)
        
        self.toposort(reachable, graph, indegree)
    
        return [source in reachable[dest] for source, dest in queries]
    
    def toposort(self, reachable, graph, indegree):
        q = deque([])
        
        for node, count in indegree.items():
            if count == 0:
                q.append(node)

        while q:
            source = q.popleft()
            
            for dest in graph[source]:
                reachable[dest].add(source)
                reachable[dest] = reachable[dest].union(reachable[source])
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    q.append(dest)
                
            
        
    def checkIfPrerequisite1(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        1: 0, 2
        2: 0
        0: []
        
        indegree:
        
        0: 2
        2: 1
        1: 0
        
        0, 1 -> False
        0, 2 -> False
        1, 0 -> True
        1, 2 -> True
        2, 0 -> True
        2, 1 -> False
        
        
        1 ----->   0    ------>  2
        
        check(1, 2) -> True
        check(1, 0) -> True
        check(0, 2) -> True
        
        Check(2, 1) -> False
        
        2
        [[1,0]]
        [[0,1],[1,0]]
        2
        []
        [[1,0],[0,1]]
        3
        [[1,2],[1,0],[2,0]]
        [[1,0],[1,2]]
        3
        [[1,2],[2,0]]
        [[1,0],[1,2],[2,0],[2,1],[0,1]]
        """
        graph = defaultdict(list)
        for source, dest in prerequisites:
            graph[source].append(dest)
            
        
        is_reachable = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for course in range(numCourses):
            self.bfs(course, is_reachable, graph)
            
        is_preconditions = []
        for source, dest in queries:
            is_preconditions.append(is_reachable[source][dest])
            
        return is_preconditions
    
    def bfs(self, source, is_reachable, graph):
        
        q = deque([source])
        visited = set()
        while q:
            curr_node = q.popleft()
            is_reachable[source][curr_node] = 1
            visited.add(curr_node)
            for next_node in graph[curr_node]:
                if next_node in visited: continue
                q.append(next_node)
        