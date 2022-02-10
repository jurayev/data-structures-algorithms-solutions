from heapq import heappush, heappop
from collections import defaultdict
class Edge:
	def __init__(self, source, dest, cost):
		self.source = source
		self.dest = dest
		self.cost = cost

class Solution:
    def networkDelayTime(self, times: List[List[int]], nodes: int, start_node: int) -> int:
        graph = defaultdict(list)
        for source, dest, cost in times:
            graph[source].append(Edge(source, dest, cost))

        # Implement Dijkstra, returns all costs
        #costs = self.dijkstra(graph, start_node, nodes)
        costs = self.bellman_ford_min_cost(times, start_node, nodes)
        # vertex : cost mapping
        # for every cost select the max cost and return
        max_cost = max(costs)
        return max_cost if max_cost != float("inf") else -1
    
    def bellman_ford_min_cost(self, times, start_node, nodes):
        costs = [float("inf") for _ in range(nodes)]
        costs[start_node-1] = 0
        visited = set()
        for source in range(1, nodes):
            for source, dest, cost in times:
                new_cost = costs[source-1] + cost
                if new_cost < costs[dest-1]:
                    costs[dest-1] = new_cost
        return costs

    def dijkstra(self, graph, start_node, nodes):
        """
        Time O(V + E LogV)
        Space O(V + E)
        
        start = 2
        in_progess = [(0,2)* (1,1)* (1,3)* (2,4)*]
                  1  2    3  4    5
        costs = [1,  0,  1, 2,  inf]
        visite = {2, 1, 3}
        """
        costs = [float("inf") for _ in range(nodes)]
        costs[start_node-1] = 0
        visited = set()
        in_progress = []
        heappush(in_progress, (0, start_node))
        while in_progress:
            cost, node = heappop(in_progress)
            if costs[node-1] < cost:
                # better cost for this node already found
                continue
            visited.add(node)
            for edge in graph[node]:
                if edge.dest in visited:
                    # already visited
                    continue
                new_cost = cost + edge.cost
                if new_cost < costs[edge.dest-1]:
                    # relax the edge
                    costs[edge.dest-1] = new_cost
                    heappush(in_progress, (new_cost, edge.dest))
        return costs
        