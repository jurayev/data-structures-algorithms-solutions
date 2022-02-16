class Solution1:
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
    
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, words: List[str]) -> int:
        if not end_word or not begin_word or not words or end_word not in words: return 0
        graph = collections.defaultdict(list)
        # O(n^2 * m) time | O(n^2 * m) space
        self.get_connected_words(words, graph)
        return self.bfs(graph, begin_word, end_word)
    
    def bfs(self, graph, start_node, end_node):
        visited = set()
        q = collections.deque([(start_node, 1)])
        while q:
            
            word, level = q.pop()
            visited.add(word)
            if word == end_node:
                return level
            
            for i in range(len(word)):
                combo_word = word[:i] + "*" + word[i+1:]
         
                for connection in graph[combo_word]:
                    if connection not in visited:
                        q.appendleft((connection, level+1))
        return 0
    
    def get_connected_words(self, words, graph):
        # *ot
        # d*t
        # do*
        for word in words:
            for i in range(len(word)):
                combo_word = word[:i] + "*" + word[i+1:]
                graph[combo_word].append(word)