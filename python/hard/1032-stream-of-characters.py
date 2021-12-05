class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie([list(word)[::-1] for word in words])  # reversing the search word before insert into trie
        self.stream = collections.deque()  # [z,y,x,a] # using queue to append from left new chars

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        found = self.trie.search(self.stream)
        return found


class Trie:
    def __init__(self, words):
        self.trie = {}
        self.anchor = "*"
        self.build(words)

    def search(self, word):
        root = self.trie

        for char in word:
            if self.anchor in root:
                return True
            if char not in root:
                return False

            root = root[char]
        return self.anchor in root

    def build(self, words):

        root = self.trie
        for word in words:
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root[self.anchor] = True
            root = self.trie

    """
    Trie
    {
        c:
           b:
             a:
               *: true

         z:
           y:
             x:
                *: true
    }


    """
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)