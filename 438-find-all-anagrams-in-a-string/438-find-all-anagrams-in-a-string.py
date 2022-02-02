class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        abab  
          ^^
        
        ab  -> count letters -> use of 32 slots with english lower case
        
        
        s = "cbaebabacd", p = "abc"
              ^ ^
         0 1 2 3 4 5....32      
        [1,1,1,0,0,0.....]  -> s chars 
         
         [1,1,1,0,0,0.....] -> p chars
         
        compare s chars with p chars in n time where n == 32 which is constant
        
        Time O(N+M)
        Space O(1), to store only 32 chars
        """
        p_size = len(p)
        s_size = len(s)
        if p_size > s_size:
            return []
        s_chars = [0] * 32
        p_chars = [0] * 32
        
        for idx, char in enumerate(p):
            p_chars[ord(char) - ord("a")] += 1
            s_chars[ord(s[idx]) - ord("a")] += 1
            
        
        start_indexes = []
        if p_chars == s_chars:
            start_indexes.append(0)
        i, j = 0, p_size
        while j < s_size:
            prev_char = s[i]
            next_char = s[j]
            s_chars[ord(prev_char) - ord("a")] -= 1
            s_chars[ord(next_char) - ord("a")] += 1
            i += 1
            j += 1
            if p_chars == s_chars:
                start_indexes.append(i)
                
                
        return start_indexes
        