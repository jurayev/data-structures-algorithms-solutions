class Trie:
    
    def __init__(self, top_k=3):
        self.trie = {}
        self.top_k = top_k
        
        
    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            if "*" not in node:
                node["*"] = deque([], maxlen=self.top_k)
            node["*"].appendleft(word)
    
    def search(self, word, top_k=3):
        words = []
        
        node = self.trie
        
        for char in word:
            if char not in node:
                words.append([])
                node = {}
                continue
            node = node[char]
            best_matched_words = node["*"]
            words.append(best_matched_words)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for word in sorted(products, reverse=True):
            trie.insert(word)
            
        return trie.search(searchWord)
        
        
        