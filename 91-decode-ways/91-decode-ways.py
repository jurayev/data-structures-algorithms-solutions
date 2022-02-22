class Solution:
    def numDecodings(self, s: str) -> int:
        """
        226
        
        2,26 -> BZ
        22,6 -> VF
        2,2,6 -> BBF
        
        2 2 6
        1 2 3
            i
          j
       
      
        2 2 0 6
        1 2 1 1
              i
        
        3 2 6
        1 1 2
            i
        
        8 0 8
        1 0 0
            i
            
        0 0 1
      1 0 0 0
      
      " 1 1 2 3"
      1 1 1 0 0
        
        state ->        decodings[i] - > num of decodings till i-th element
        initial state -> decodings[0....n-1] = 0
        transition functions -> decodings[i] = decodings[i-1] if can[i]
                             -> decodings[i] = decodings[i] + 1 if can[i]+can[i-1]
        calculation order -> 0.....n-1
        answer -> decodings[n-1]
        """
        n = len(s)
        decodings = [0 for _ in range(0, n+1)]
        decodings[0] = 1
        
        for i in range(1, n+1):
            one_num = s[i-1]
            two_num = s[i-2] + s[i-1] if i-2 >= 0 else "0" + s[i-1]
            decodings[i] += decodings[i-1] if self.can_decode(one_num) else 0
            decodings[i] += decodings[i-2] if self.can_decode(two_num) else 0
        return decodings[n]
    
    def can_decode(self, string_number):
        number = int(string_number)
        if len(string_number) != len(str(number)):
            return False
        return bool(1 <= number <= 26)