class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Time O(V+E)
        Space O(V+E)
        
        ["JFK","ATL","JFK","SFO","ATL","SFO"]
        
        ["JFK","ATL","SFO","ATL","JFK", SFO]
        
        ["JFK","SFO","ATL","JFK","ATL","SFO"]
        
        
        JFK : ATL, SFO
        SFO: ATL
        ATL: JFK, SFO
        
        JFK : None, None
        SFO: None
        ATL: None, None
        
        
        [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
        [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        """
        graph = collections.defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)
            
        for node, connections in graph.items():
            graph[node] = sorted(connections)
        route = []
        self.dfs(graph, "JFK", route)
        return route[::-1]
        
        
    def dfs(self, graph, node, route):
        
        connections = graph[node]
        for i in range(len(connections)):
            connection = connections[i]
            if not connection: continue
            connections[i] = None
            self.dfs(graph, connection, route)
        route.append(node)