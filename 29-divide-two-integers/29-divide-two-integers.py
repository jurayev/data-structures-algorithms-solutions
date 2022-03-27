class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_sign = -1 if dividend < 0 else 1
        divisor_sign = -1 if divisor < 0 else 1
        
        dividend = abs(dividend) # 7 #
        divisor = abs(divisor)   # 2 #
        result = 0 # 3
        while dividend >= divisor:
            subdivisor, power = divisor, 1 # 2, 2
            while dividend >= subdivisor:  # 1, 8
                dividend -= subdivisor
                result += power
                subdivisor <<= 1
                power <<= 1

        result *= dividend_sign * divisor_sign
        return min(max(-2**31, result), 2**31 - 1)