class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
           0    1   2.  3
        [[1,2],[3],[3],[]]
            ^
        
        paths = [[0, 1, 3], [0,2,3]]
        path = 
        
        """
        end = len(graph)-1
        
        @lru_cache(maxsize=None)
        def dfs_bottomup(node):
            if node == end:
                return [[node]]
            paths = []
            for next_node in graph[node]:
                for path in dfs_bottomup(next_node):          
                    paths.append( [node] + path)
            return paths
        
        return dfs_bottomup(0)
    
    def allPathsSourceTarget1(self, graph: List[List[int]]) -> List[List[int]]:
        """
        TC - O(V*E)
        SC - O(V*E)
        """
        
        start = 0
        end = len(graph) - 1
        
        paths = []
        self.dfs_topdown(graph, start, end, paths, [0])
        
        return paths
    
    
    def dfs(self, graph, node, end, paths, path):
        if node == end:
            paths.append(path[:])
            return
        
        if not (0 <= node <= end):
            return
        
        for next_node in graph[node]:
            path.append(next_node)
            self.dfs(graph, next_node, end, paths, path)
            path.pop()