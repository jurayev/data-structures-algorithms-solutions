class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Input: 
        board = [["o","a","a","n"],
                 ["e","t","a","e"],
                 ["i","h","k","r"],
                 ["i","f","l","v"]], 
        words = ["oath","pea","eat","rain", "hi", "hih"]
        Output: ["eat","oath", "hi"]
        
        
        abc
        abd
        abr
        Time O(M * 4^L), L is the word with max len
        Space O(N)
        """
        found_words = []
        trie = Trie(words)
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(row, col, board, trie.root, found_words)
                
        return found_words
        
    def dfs(self, row, col, board, node, found_words):
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return
        letter = board[row][col]
        next_node = node.children.get(letter)
        if letter == "#":
            return
        if not next_node:
            return
        if next_node.word:
            found_words.append(next_node.word)
            next_node.word = None
        board[row][col] = "#"
        self.dfs(row+1, col, board, next_node, found_words)
        self.dfs(row-1, col, board, next_node, found_words)
        self.dfs(row, col+1, board, next_node, found_words)
        self.dfs(row, col-1, board, next_node, found_words)
        # remove matched node in Trie
        if not next_node.children:
            node.children.pop(letter)
        board[row][col] = letter
        
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.load(words)
    
    def load(self, words):
        for word in words:
            self.insert(word)
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None