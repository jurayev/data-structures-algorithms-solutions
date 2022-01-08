class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """
        From BiWeekly Contest 69, Q1
        Submission time - 0:06:06
        Time Spent - 6 min
        
        Complexities:
            Time O(N)
            Space O(N)
        """
        words = title.split(" ")
        
        for i in range(len(words)):
            word = words[i]
            if len(word) < 3:
                word = word.lower()
            else:
                word = word.lower().capitalize()
            words[i] = word
            
        return " ".join(words)