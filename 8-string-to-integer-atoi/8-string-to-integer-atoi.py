class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        integer = 0
        # find the integer start pos
        i = 0
        while i < len(s) and not s[i].isnumeric():
            sign = -1 if s[i] == "-" else 1
            i += 1
        
        # check if any no-white space before the integer
        for j in range(0, i-1):
            if s[j] != " ":
                return 0

        if i-1 >= 0 and s[i-1] not in " -+":
            return 0
        # find the number end
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
        # conver the string to number
        for idx in range(i, j):
            integer *= 10
            integer += int(s[idx])
            

        return max(-2**31, min(sign * integer, 2**31-1))
        