class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        "eidboaoo"
            ^
               ^
        a: 1
        b: 1
        
        "eidbbaooo"       
              ^
               ^
        "ab"
        
        counter = 1
        """
        
        if len(s1) > len(s2):
            return False
        
        letters = collections.Counter(s1)
        counter = len(s1)
        min_size = float(inf)
        start, end = 0, 0
        
        while end < len(s2):
            end_letter = s2[end]
            if end_letter in letters:
                letters[end_letter] -= 1
                if letters[end_letter] >= 0:
                    counter -= 1
            while counter == 0:
                min_size = min(min_size, end - start + 1)
                start_letter = s2[start]
                if start_letter in letters:
                    letters[start_letter] += 1
                    if letters[start_letter] > 0:
                        counter += 1
                start += 1
            end += 1
            
        print(min_size)
        return min_size == len(s1)