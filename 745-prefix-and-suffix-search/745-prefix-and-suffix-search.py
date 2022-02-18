class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.weight = -1
    
    def set_weight(self, weight):
        self.weight = weight

class WordFilter:
    """
    Sol 1:
    
        1. store all the words, sort them by len and preserve the indexes -> O(n log n)
        2. f(pre, suf) -> check everyword using startswith(), endswith() built-in, return the first answer found -> O(n*2m)
    Space == input Space
    
    Sol 2:
        1. store all the word in prefix tree and suffix tree
        
    a: 
      p:
        p:
      r:
        p:
        k:
        s:
        
    
    p:
      p:
        a:
      r:
        a
            
    f("a", "rp") -> 0
    
    test ->  "t#test"
              000000
    tesst -> "t#tesst"
              1111111
    """

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = TrieNode()
        self.insert_words(words)

    def f(self, prefix: str, suffix: str) -> int:
        search_word = suffix + "#" + prefix
        node = self.trie
        for char in search_word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weight
    
    def insert(self, word, weight):
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.set_weight(weight)
        
    def insert_words(self, words):
        for weight, word in enumerate(words):
            suffixed_word = "#" + word
            for char in reversed(word):
                suffixed_word = char + suffixed_word
                self.insert(suffixed_word, weight)
        

["WordFilter","f","f","f","f","f","f","f","f","f"]
[[["apple", "applee", "test", "tesst", "m", "k"]],["a","e"],["a","le"],["apple","le"],["te","t"],["t","sst"],["tests","t"],["app", "eee"],["m", "m"],["m", "k"]]
["WordFilter","f","f","f","f","f","f","f","f","f","f"]
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]      
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)