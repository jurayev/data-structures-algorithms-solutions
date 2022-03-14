class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
        
        """
        time = 0
        letter_indices = {letter: i for i, letter in enumerate(keyboard)}
        start_letter = keyboard[0]
        for target_letter in word:
            time += abs(letter_indices[start_letter] - letter_indices[target_letter])
            start_letter = target_letter
            
        return time
            