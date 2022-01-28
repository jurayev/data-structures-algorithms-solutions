class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.children[char]
        node.end = True


    def search(self, word: str) -> bool:
        return self.backtrack(word, 0, self.trie)

    def backtrack(self, word, index, node) -> bool:
        """
        b . . t
        ^ 
        bbad
        bbam
        """
        if index >= len(word):
            return node.end

        char = word[index]
        if char == ".":
            for child_char in node.children:
                if self.backtrack(word, index+1, node.children[child_char]):
                    return True
            return False

        if char not in node.children:
            return False
        return self.backtrack(word, index+1, node.children[char])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)