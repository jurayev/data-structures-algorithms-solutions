class Solution:
    def mostWordsFound1(self, sentences: List[str]) -> int:
        best = 0
        
        for sentence in sentences:
            words = sentence.split(" ")
            best = max(best, len(words))
            
            
        return best
    
    def mostWordsFound(self, sentences: List[str]) -> int:
        best = 0
        
        for sentence in sentences:
            count = 1
            for char in sentence:
                if char == " ":
                    count += 1

            best = max(best, count)
               
        return best