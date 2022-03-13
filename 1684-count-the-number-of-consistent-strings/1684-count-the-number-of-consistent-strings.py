class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Count how many words you can make using given alphabet?
        You can use as many letters as you want but only from the alpabet
        
        Input: alphabet = "ab", words = ["ad","bd","aaab","baa","badab"]
        Output: 7
        """
        alphabet = collections.Counter(allowed)
        counter = len(words)
        for word in words:
            letters = Counter(word)
            for letter in letters:
                if letter not in alphabet:
                    counter -= 1
                    break
                
        return counter