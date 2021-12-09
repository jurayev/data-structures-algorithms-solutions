class Solution:
    def canReachDFS(self, arr: List[int], start: int) -> bool:
        """
        Examples:

             0 1 2 3 4 5 6
            [4,2,3,0,3,1,2]
                       ^
            start = 5
            0: [4]
            1: [3]
            2: [5]
            3: []
            4: [1]
            5: [4, 6]
            6: [4]
            visiting = {6,4,1}

             0 1 2 3
            [2,0,2,3,1]   - handle loops in the graph
                 ^
            start = 2

        Complexity:
            TC O(V+E)
            SC O(V+E) - for keeping visited indexes

        Approach:
            Treat the array as direct graph with cycles and traverse using DFS or BFS

            if 0 found: end the search and return True
            if never found: return False

            check boundary conditions  from 0  to len(arr)-1
            check for self loops and loops by keeping the index in visited set
            check for single node graph or empty graph

            [1,4,3]

            [2,4,3,0]
            [0,2]
        """
        visited = set()
        return self.bfs(arr, start, visited)

    def bfs(self, array, start, visited):
        if not (0 <= start < len(array)) or start in visited:
            return False

        value = array[start]
        if value == 0:
            return True

        visited.add(start)
        left_found = self.bfs(array, start - value, visited)
        right_found = self.bfs(array, start + value, visited)

        return left_found or right_found

    def canReachBFS(self, arr: List[int], start: int) -> bool:
        queue = collections.deque([start])
        visited = set()

        while queue:
            index = queue.popleft()
            if not (0 <= index < len(arr)) or index in visited:
                continue
            if arr[index] == 0:
                return True

            visited.add(index)

            left_dir = index - arr[index]
            right_dir = index + arr[index]
            queue.append(left_dir)
            queue.append(right_dir)
        return False