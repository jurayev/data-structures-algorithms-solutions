class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        """
        hit  -> it, ht, hi
        
        hot  -> ot, ht, ho
        
        dot -> ot, dt, do
        
        dog -> og, dg, do
        
        ht: hit, hot , hop
        it: [hit]
        hi: [hit]
        ot: [hot, dot]
        do: [dot, dog]
        
        hit: hot, hop
        hot: hop
        
        Time O(M*N) + O(N) + O(N)
        Space O(M*N)
        
        hit
          ^
        """
        shortcuts = defaultdict(set)
        for word in [beginWord] + wordList:
            for i in range(0, len(word)):
                shortcut = word[:i] + "*" + word[i+1:]
                shortcuts[shortcut].add(word)
        
        graph = defaultdict(set)
        for shortcut in shortcuts:
            connected = shortcuts[shortcut]
            for node in connected:
                graph[node] = graph[node].union(connected)

        return self.bfs(graph, beginWord, endWord)
        
        
        
    def bfs(self, graph, source, target):
        q = deque([(source, 1)])
        visited = set([source])

        while q:
            curr_word, dist = q.popleft()
            if curr_word == target:
                return dist

            for next_word in graph[curr_word]:
                if next_word not in visited:
                    visited.add(next_word)
                    q.append((next_word, dist+1))
         
        return 0