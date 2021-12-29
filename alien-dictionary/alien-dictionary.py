class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        """
        Approach:
            1. Make a graph according to the letters order, comparing to adjacent words
            2. Find Topological order based on the graph
        
        Examples:
            ["ba", "bc", "ac", "cab"]

            b: a
            a: c

            res = bac


            ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
            y: 0
            w: 2
            z: 2
            x: 1

            y: w, w
            w: x, z
            x: z

            res = ywxz


        """
        n = len(words)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for word in words:
            for character in word:
                indegree[character] = 0
        
        for i in range(n-1):
            word1, word2 = words[i], words[i+1]
            idx1, idx2 = 0, 0
            while idx1 < len(word1) and idx2 < len(word2):
                char1 = word1[idx1]
                char2 = word2[idx2]
                if char1 != char2:
                    graph[char1].append(char2)
                    indegree[char2] += 1
                    break
                idx1 += 1
                idx2 += 1
            else:
                if len(word2) < len(word1): 
                    return ""
        order = []

        q = deque([node for node, count in indegree.items() if count == 0])

        while q:
            source = q.popleft()
            order.append(source)

            for dest in graph[source]:
                indegree[dest] -= 1
                if indegree[dest] <= 0:
                    q.append(dest)
                    
        if len(order) != len(indegree):
            return ""
        return "".join(order)