class TrieNode:
    def __init__(self,):
        self.children = defaultdict(TrieNode)
        self.weight = 0
        self.is_word = False
        
    def increment(self, value):
        self.weight += value
    
    def set_word(self):
        self.is_word = True
    
class MapSum:

    def __init__(self):
        self.trie = TrieNode()
        self.inserted_keys = Counter()

    def insert(self, key: str, val: int) -> None:
        # "word": 3 - 4
        #.   val - inserted
        #     4 - 3 -> 1
        #     3 - 4 -> -1
        #     4 - 0 -> 4
        
        new_val = val - self.inserted_keys[key]
        self.inserted_keys[key] = val
        node = self.trie
        for char in key:
            node = node.children[char]
            node.increment(new_val)
        node.set_word()
        

    def sum(self, prefix: str) -> int:
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.weight
    

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)