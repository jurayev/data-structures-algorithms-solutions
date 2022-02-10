class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        return self.bf_min_cost(flights, n, src, dst, k)
        
        
    def bf_min_cost(self, flights, airports, src, dst, at_most_stops):
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
