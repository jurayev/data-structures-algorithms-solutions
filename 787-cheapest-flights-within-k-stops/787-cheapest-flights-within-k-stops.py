class Edge:
    
    def __init__(self, dest, cost):
        self.cost = cost
        self.dest = dest
        
class Node:
    
    def __init__(self, cost, stops, node_id):
        self.cost = cost
        self.stops = stops
        self.id = node_id
        
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.stops < other.cost
        return self.cost < other.cost
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # TODO impelement as dijkstra
        return self.dijkstra(flights, n, src, dst, k)
        #return self.bellman_ford_min_cost(flights, n, src, dst, k)
        
    def dijkstra(self, flights, cities, src, dst, stops):
        """
        Time O(E + E LOG V)
        Space O(E)
        [(0, 0), (100, 1), (200, 2), (500, 2)]
        
        [(0, 0, 0), (1, 1, 1), (5, 2, 1), (2, 2, 2), (6, 3, 2), (4, 3, 3)]
        4
        [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
        0
        3
        1
        """
        graph = collections.defaultdict(list)
        for source, dest, cost in flights:
            graph[source].append(Edge(dest, cost))
        
        costs = [float("inf") for _ in range(cities)]
        curr_stops = [float("inf") for _ in range(cities)]
        costs[src] = 0
        curr_stops[src] = 0
        
        cheapest = []
        heappush(cheapest, Node(0, 0, src))
        while cheapest:
            node = heappop(cheapest)
            if node.stops > curr_stops[node.id] or node.stops > stops:
                continue
            curr_stops[node.id] = node.stops 
            for edge in graph[node.id]:
                new_cost = node.cost + edge.cost
                costs[edge.dest] = min(new_cost, costs[edge.dest])
                heappush(cheapest, Node(new_cost, node.stops + 1, edge.dest))
    
        return costs[dst] if costs[dst] < float("inf") else -1
    
    def bellman_ford_min_cost(self, flights, airports, src, dst, at_most_stops):
        """
        
        Time O(K * E)
        Space O(V)


        costs = [0, 100, 200]

        stops = 1



                        0

             100	/	   \ 500
                  1     —    2
                       100
              50	 \		/ 25
                        3
                        
5
[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
0
2
2
4
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
0
3
1
2
[[0,1,100]]
0
1
0
3
[[0,1,100]]
0
2
0
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
0
5
[[0,1,100],[1,2,100],[0,2,500],[1,3,50],[3,2,25]]
0
2
1
5
[[0,1,100],[1,2,100],[0,2,500],[1,3,50],[3,2,25]]
0
2
2
5
[[0,1,100],[1,2,100],[0,2,500],[1,3,50],[3,2,25]]
0
2
0
5
[[0,1,100],[1,2,100],[0,2,500],[1,3,50],[3,2,25]]
0
2
4
        """
        costs = [float("inf") for _ in range(airports)]
        costs[src] = 0

        for airport in range(at_most_stops+1):
            curr_costs = costs[:]
            for source, destination, cost in flights:   # 1, 2, 100 # 0, 2, 500 # 0, 1, 100
                new_cost = cost + curr_costs[source]
                if new_cost < costs[destination]:
                    costs[destination] = new_cost


        return costs[dst] if costs[dst] < float("inf") else -1
