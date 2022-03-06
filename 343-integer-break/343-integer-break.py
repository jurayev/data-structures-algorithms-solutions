class Solution:
    def integerBreak(self, n: int) -> int:
        """
        
        2,2,2,2,2
        
        5, 5 -> 25
        3, 3, 4 -> 36
        
        10 ->
        10 % 3 -> 1
        3 ** (3-1) * (3+1) -> 9 * 4 -> 36
        
        10 -> 
        10 % 2 -> 0
        2 ** (5-1) * (2+0) -> 16 * 2 -> 32
        
        10 -> 4 + 4 + 2
        10 % 4 -> 2
        4 ** (1) -> 4 * 6
        
        3 -> 1 + 2
        3 % 2 -> 1
        """
        precalc = {2: 1, 3: 2, 4: 4}
        if n in precalc: return precalc[n]
        best = 1
        for num in range(2, n):
            rem = n % num
            mult = num + rem if rem < 2 else rem
            power = (n // num - 1) if rem < 2 else n // num
            product = num ** power * mult
            best = max(best, product)
            
        return best