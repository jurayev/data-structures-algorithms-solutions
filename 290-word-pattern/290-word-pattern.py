class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        "abba"
        "dog dog dog dog"
        a: dog
        b: dog

        dog: a
        dog: b
        
        
        "abba"
        "dog cat cat fish"
        a: dog
        b: cat
        
        dog: a
        cat: b
        
        """
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        word_letter = {}
        letter_word = {}
        for letter, word in zip(list(pattern), words):
            if (word in word_letter and word_letter[word] != letter) or (letter in letter_word and letter_word[letter] != word):
                return False
            else:
                word_letter[word] = letter
                letter_word[letter] = word
                
        return True
                