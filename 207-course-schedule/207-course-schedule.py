class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        
        [[0,1],[1,2],[0,2]]
        
        {
        0: 1
        1: 2
        2: []
        }
        
        indegree {
        0: 1
        1: 1
        2: 0
        }
        start_node = [2]
        
        """
        return self.toposort(numCourses, prerequisites)
        
    def toposort(self, total, relations):
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for source, dest in relations:
            graph[dest].append(source)
            indegree[source] += 1
        
        free_nodes = []
        for node in range(total):
            if indegree[node] == 0:
                free_nodes.append(node)
        visited = 0
        queue = deque(free_nodes)
        while queue:
            node = queue.popleft()
            visited += 1
            
            for next_node in graph[node]:
                if indegree[next_node] > 0:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)
        return visited == total
        