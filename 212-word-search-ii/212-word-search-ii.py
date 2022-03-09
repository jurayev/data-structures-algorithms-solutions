class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        O(r*c* len(words)) time
        O(r*c) space
        """
        found_words: Set = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                for word in words:
                    self.dfs(row, col, board, word, 0, set(), found_words)
                
        return list(found_words)       
    
    def dfs(self, row: int, col: int, board: List[List[str]], word:str, word_idx:int, visiting: Set, found_words: Set):
        if word_idx >= len(word): 
            found_words.add(word)
            return
        if not self.in_bounds(board, row, col): return
        if (row, col) in visiting: return
        if board[row][col] == word[word_idx] and word not in found_words:
            visiting.add((row, col))
            self.dfs(row+1, col, board, word, word_idx+1, visiting, found_words)
            self.dfs(row-1, col, board, word, word_idx+1, visiting, found_words)
            self.dfs(row, col+1, board, word, word_idx+1, visiting, found_words)
            self.dfs(row, col-1, board, word, word_idx+1, visiting, found_words)
            visiting.remove((row, col))
            
    def in_bounds(self, board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        abc
        abd
        abr
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