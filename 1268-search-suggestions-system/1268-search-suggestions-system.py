class Trie:
    
    def __init__(self,):
        self.trie = {}
        
        
    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            if "*" not in node:
                node["*"] = []
            node["*"].append(word)
            node["*"].sort()
    
    def search(self, word, top_k=3):
        words = []
        
        node = self.trie
        
        for char in word:
            if char not in node:
                words.append([])
                node = {}
                continue
            node = node[char]
            best_matched_words = node["*"][:top_k]
            words.append(best_matched_words)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for word in products:
            trie.insert(word)
            
        return trie.search(searchWord)
        
        
        