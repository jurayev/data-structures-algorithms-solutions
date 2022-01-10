class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return
    
    def addBinary3(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        
        res = num_a + num_b
        return "{0:b}".format(res)
    
    def addBinary2(self, a: str, b: str) -> str:
        """
          1
        0010
        1011
           1
           ^
        """
        n = max(len(a), len(b))
        a_list = [num for num in reversed(a)]
        b_list = [num for num in reversed(b)]
        result = ["0" for _ in range(n)]
        
        carry = 0
        for i in range(0, n):
            bina = a_list[i] if i < len(a_list) else "0"
            binb = b_list[i] if i < len(b_list) else "0"
            
            if bina == "1":
                carry += 1
            if binb == "1":
                carry += 1
                
            res = carry % 2
            result[i] = str(res)
            carry //= 2
                
            
        if carry:
            result.append(str(carry))
            
        return "".join(reversed(result))
        
        
    
    def addBinary(self, a: str, b: str) -> str:
        """
          10
        1011
        
        """
        
        mapping = {0: (0, 0),
                   1: (0, 1),
                   2: (1, 0),
                   3: (1, 1)}
        n = max(len(a), len(b))
        a_list = [int(num) for num in reversed(a)]
        b_list = [int(num) for num in reversed(b)]
        result = [0 for _ in range(n)]
        
        carry = 0
        for i in range(0, n):
            bin_a = a_list[i] if i < len(a_list) else 0
            bin_b = b_list[i] if i < len(b_list) else 0
            
            summ = bin_a + bin_b + carry
            
            carry = mapping[summ][0]
            res = mapping[summ][1]
            result[i] = res
            
        if carry:
            result.append(carry)
            
        return "".join(map(str,reversed(result)))
            