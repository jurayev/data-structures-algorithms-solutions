class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        0: {1,2,7}
        1: {3,6,7}
        
        1: [2] 
        2: [1]
        source = 1
        target = 6
        <-- -- - -   --  --
     | ->  1 -> 2 ->  7 -> |
     |                ^
     |                |
     | -> 3 -> 6 ->   |
        
        Time O(N^2)
        Space O(N^2)
        """
        if source == target:
            return 0
        
        sources = set()
        targets = set()
        all_routes = []
        for idx, route in enumerate(routes):
            stops = set(route)
            if source in stops: sources.add(idx)
            if target in stops: targets.add(idx)
            all_routes.append(stops)
        
        N = len(routes)
        graph = collections.defaultdict(set)
        # build graph of connected routes
        for idx in range(N):
            for idn in range(idx+1, N):
                connections = [s in all_routes[idn] for s in all_routes[idx]]
                if any(connections):
                    graph[idx].add(idn)
                    graph[idn].add(idx)
        
        queue = collections.deque([(source, 1) for source in sources])

        # start routing from A->B->C routes (not stops)
        while queue:
            start, buses = queue.popleft()
                
            if start in targets: # reached any of all possible targets
                return buses
            
            
            for dest in graph[start]:
                if dest not in sources:
                    queue.append((dest, buses+1))
                    sources.add(dest)
   
        return -1