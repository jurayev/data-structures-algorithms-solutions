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
           c
         ""
        """
        size = ""
        i = 0
        for char in abbr:
            #print(size, char, word[i], i)
            if char.isdigit():
                size += char
                continue
            elif size:
                if str(int(size)) != size or not int(size):
                    return False
                i += int(size)
                size = ""
            if i < len(word) and char == word[i]:
                i += 1
            else:
                #print("exit")
                return False
        #print(i)
        if size:
            if str(int(size)) != size or not int(size):
                    return False
            i += int(size)
        return i == len(word)