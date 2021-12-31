class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        Time Complexity O(V+E), V is count of distinct numbers, E - count of all numbers in seqs
        Space Complexity O(V+E)
        """
        sortedOrder = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for seq in seqs:
            for i in range(len(seq)-1):
                source, dest = seq[i], seq[i+1]
                graph[source].append(dest)
                indegree[dest] += 1
                
            for source in seq:
                indegree[source] += 0
        
        if len(indegree) != len(org):
            return False
        
        q = deque([v for v in indegree if indegree[v] == 0])
        
        while q:
            if len(q) > 1:
                return False
            source = q.popleft()
            sortedOrder.append(source)

            for dest in graph[source]:
                indegree[dest] -= 1
                if indegree[dest] <= 0:
                    q.append(dest)
        return len(sortedOrder) == len(org)    