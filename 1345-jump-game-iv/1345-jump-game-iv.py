class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Examples:
         0    1    2   3  4   5  6. 7 8   9
        [100,-23,-23,404,100,23,23,23,3,404]
              ^
        
        Approach:
            Build a graph, then perform bfs, and return the number of jump made

        Graph:
            0: 0, 1, 4
            1: 0, 1, 2
            2: 1, 3
            3: 2, 4, 9
            4: 3, 5, 0
            5: 4, 6, 7
            6: 5, 7
            7: 6, 5, 8
            8: 7, 9
            9: 8, 3
        
        Complexities:
            Time O(N)
            Space O(2N)
        """
        graph = collections.defaultdict(set)
        for idx, num in enumerate(arr):
            graph[num].add(idx)

        visited = set()
        target = len(arr)-1
        q = collections.deque([(0, 0)])
        
        while q:
            _from, steps = q.popleft()
            if _from == target:
                return steps
            
            value = arr[_from]
            visited.add(_from)
            
            for to in graph[value]:
                if to not in visited:
                    q.append((to, steps+1))
            
            prev_node = _from-1
            next_node = _from+1
            if prev_node >= 0 and prev_node not in visited:
                q.append((prev_node,steps+1))
            if next_node < len(arr):
                q.append((next_node,steps+1))
                
            graph[value].clear()
        return 0