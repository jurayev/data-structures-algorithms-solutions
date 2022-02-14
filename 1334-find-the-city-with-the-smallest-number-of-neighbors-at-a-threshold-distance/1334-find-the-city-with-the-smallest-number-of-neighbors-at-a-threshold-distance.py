class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        4
        [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
        4
        5
        [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
        2
        5
        [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,4],[3,4,5]]
        1
        5
        [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
        2
        5
        [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
        10
        """
        graph = collections.defaultdict(list)
        for source, dest, cost in edges:
            graph[source].append((dest, cost))
            graph[dest].append((source, cost))

        cities = []
        for node in range(n):
            #costs = self.bellman_ford(node, edges, distanceThreshold, n)
            costs = self.dijkstra(node, graph, distanceThreshold, n)
            total_cities = 0
            for cost in costs:
                total_cities += cost != float(inf)
            cities.append(total_cities)
        min_cities = min(cities)
        smallest_connections = [i for i in range(n) if cities[i] == min_cities]
        return smallest_connections[-1] if smallest_connections else -1

    def bellman_ford(self, start_node, edges, max_distance, total_nodes):
        """
        Time O(V*E)
        Space O(E)
        
        TLE
        """
        costs = [float(inf) for _ in range(total_nodes)]
        costs[start_node] = 0
        for node in range(total_nodes):
            for source, dest, cost in edges:
                new_cost = cost + costs[source]
                costs[dest] = min(costs[dest], new_cost)
                new_cost = cost + costs[dest]
                costs[source] = min(costs[source], new_cost)
                
        return [cost for cost in costs if cost <= max_distance]
    
    def dijkstra(self, start_node, graph, max_distance, total_nodes): 
        """
        Time O(V + E log V)
        Space O(E)
        """
        costs = [float(inf) for _ in range(total_nodes)]
        costs[start_node] = 0
        min_heap = []
        heappush(min_heap, (0, start_node))

        while min_heap:
            cost, source = heappop(min_heap)

            if cost > costs[source]:
                continue
            for dest, other_cost in graph[source]:
                new_cost = cost + other_cost
                if costs[dest] > new_cost and new_cost <= max_distance:
                    costs[dest] = new_cost
                    heappush(min_heap, (new_cost, dest))

        return costs
