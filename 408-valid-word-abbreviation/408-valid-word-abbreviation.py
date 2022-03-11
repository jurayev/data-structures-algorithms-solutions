class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        "internationalization", 
                            ^
        "i12iz4n"
               ^
        0
        
        "apple"
            i
        "a2e"
           j
         ""
        """
        i, j = 0, 0
        #word += "#"
        #abbr += "#"
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                size = 0
                while j < len(abbr) and abbr[j].isdigit():
                    size *= 10
                    size += int(abbr[j])
                    j += 1
                i += size
            else:
                break
        return j == len(abbr) and i == len(word)