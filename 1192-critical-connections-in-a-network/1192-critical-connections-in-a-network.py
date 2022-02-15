class StatesEnum:
	UNVISITED = 0
	VISITING = 1
	VISITED = 2
	IN_CYCLE = 3

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
	    # find all nodes in cycle
        # discard the nodes in cycle
        # the rest are nodes from citical connections
        # NOT WORKING SOLUTION
        """
        	            2   
                    /       |
                  /	        |
            6 —-- 1  —----- 0
            |
            |
            3  —------- 4
        
            
                    	2   
                    /       |
                  /	        |
            6 —-- 1  —----- 0
                    |
                    |
                    3  —------- 4
                    
                    
        5
        [[0,1],[1,2],[2,0],[1,3],[3,4]]
        """
        return self.tarjan(connections, n)
        #return self.detect_critical_connections(n, connections)

    def tarjan(self, connections, n):
        # Create the adjacency list.
        graph = defaultdict(list)
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
		# ids is used for recording when we discover i-th node.
		# lows is used for saving the low-link value for i-th node.
        ids, lows, ans = [None] * n, [None] * n, []
        self.time = 0
        
        def dfs(v, parent):
            if ids[v] is not None:
                return
            
			# record the time when we discover this node
            ids[v] = lows[v] = self.time
            self.time += 1
            for adj in graph[v]:
                if adj == parent:
                    continue
                    
                dfs(adj, v)
				
				# save lowest discover time in one SCC (strongly connected component)
                lows[v] = min(lows[v], lows[adj])
				
				# How to understand this condition:
				# If there is a cycle (in one SCC), for any two connected nodes, 
				# say v and adj, the discover time is alway >= low-link value, which is id[v] >= lows[adj].
                # If no cycle between two nodes, then we have the following condition. Then they are two SCCs.
                if ids[v] < lows[adj] or ids[adj] < lows[v]:
                    ans.append([v, adj])
        
        dfs(0, None)
        return ans
    
    def detect_critical_connections(self, n_nodes, connections):
        # Time O(V + E) + O(V+E)
        # Space O(V + E)
        critical_connections = []
        graph = collections.defaultdict(list) # adj list

        for source, dest in connections:
            graph[source].append(dest)
            graph[dest].append(source)

        states = {}  # 0, 1, 2
        for node in range(n_nodes):
            states[node] = StatesEnum.UNVISITED
        indegree = collections.Counter()
        self.dfs(graph, states, indegree, 0)
        visited = set()
        for node in range(n_nodes):
            visited.add(node)
            if indegree[node] == 0: continue
            for connection in graph[node]:
                if connection in visited: continue
                critical_connections.append([node, connection])

        return critical_connections


    def dfs(self, graph, states, indegree, node):
        if indegree[node] >= 2:
            return
        if states[node] == StatesEnum.VISITED:
            return
        if states[node] == StatesEnum.VISITING:
            indegree[node] += 1
        
        states[node] = StatesEnum.VISITING
        for connection in graph[node]:
            self.dfs(graph, states, indegree, connection)

        states[node] = StatesEnum.VISITED

	
