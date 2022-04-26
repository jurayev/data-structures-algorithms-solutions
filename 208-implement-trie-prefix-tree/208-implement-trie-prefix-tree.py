class TrieNode:
    def __init__(self,):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.trie = {}
        self.word_end = "*"

    def insert(self, word: str) -> None:
        node = self.trie
        
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            
        node[self.word_end] = True

    def search(self, word: str) -> bool:
        node = self.trie
        
        for char in word:
            if char not in node:
                return False
            node = node[char]
        
        return self.word_end in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)