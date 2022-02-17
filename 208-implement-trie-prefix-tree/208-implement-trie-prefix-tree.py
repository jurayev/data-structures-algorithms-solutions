class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        
        a:
            p:
                p:
                    l:
                        l:
                    *:      e:
                                *:
        """
        self.root = {}
        self.anchor = "*"
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node[char] = node.get(char, {})
            node = node[char]
        node[self.anchor] = defaultdict()   
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.anchor in node

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
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