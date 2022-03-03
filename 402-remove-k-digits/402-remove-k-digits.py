class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        
        [1,2,1,9]
        
        [1,2]
        while k > 0 and stack and stack[-1] >= digit:
            pop
"1432219"
3
"10200"
1
"10"
2
"1432219"
1
"1432219"
5
"1432219"
7
"0"
1
"1"
1
        """
        
        mono_stack = []
        #nums = [int(digit) for digit in num]
        
        for digit in num:
            while k > 0 and mono_stack and mono_stack[-1] > int(digit):
                mono_stack.pop()
                k -= 1
            mono_stack.append(int(digit))
        
        while mono_stack and k > 0:
            k -= 1
            mono_stack.pop()
        selected_nums = [str(digit) for digit in mono_stack]

        answer = str(int("".join(selected_nums))) if selected_nums else "0"
        return answer if answer else "0"