class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alphabet = collections.Counter(allowed)
        counter = 0
        for word in words:
            letters = Counter(word)
            matched = 1
            for letter in letters:
                if letter not in alphabet:
                    matched = 0
                    break
            counter += matched
                
        return counter