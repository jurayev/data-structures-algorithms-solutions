class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for source, dest, time in times:
            graph[source].append((time, dest))
        return self.djikstra(graph, k, n)
        
        
    def djikstra(self, graph, start_node, total_nodes):
        max_time = 0
        unvisited = [] # priority heap
        heappush(unvisited, (0, start_node))
        costs = [float("inf") for _ in range(total_nodes+1)]
        costs[start_node] = 0
        costs[0] = 0

        while unvisited:
            time, source = heappop(unvisited)
            if costs[source] < time: # check if already better cost
                continue
            max_time = max(max_time, time)
            for dest_time, dest in graph[source]:
                cost = time + dest_time
                if costs[dest] > cost: # relax the edge
                    costs[dest] = cost
                    heappush(unvisited, (cost, dest))
                    
        for cost in costs:
            if cost == float("inf"):
                return -1
        return max_time