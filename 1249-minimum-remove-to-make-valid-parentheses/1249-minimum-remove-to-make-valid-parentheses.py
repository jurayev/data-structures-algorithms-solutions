class Solution:
    def minRemoveToMakeValid1(self, s: str) -> str:
        """
         10010123
        "())()((("
         0101000
        "()()((("
        
        "()()"

        """
        open_count, close_count = 0, 0
        for char in s:
            if char == "(":
                open_count += 1
            elif char == ")" and open_count:
                open_count -= 1
            elif char == ")":
                close_count += 1
        formatted_chars = []
        for char in s:
            if char == ")" and close_count:
                close_count -= 1
            else:
                formatted_chars.append(char)
        s2 = "".join(formatted_chars)
        formatted_chars = []
        for char in reversed(s2):
            if char == "(" and open_count:
                open_count -= 1
            else:
                formatted_chars.append(char)
        return "".join(reversed(formatted_chars))
        
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Ex 1:
         "lee(t(c)o)de)" -> "lee(t(c)o)de)".replace(")", "")
         "(()))" -> ")"
         
         Ex 2:
          "))((()" 
            -> "))((" -> "))((".replace(")", "").replace(")", "").replace("(", "") 
            -> ""
         
         Time O(N):
            1. collect brackets O(N)
            2. remove all matching brackets O(N)
            3. remove all unmatched brackets O(N)
         Space O(N)
        """
        brackets = [] #  "))((" # ""
        for char in s:
            if char in ["(", ")"]:
                brackets.append(char)
        # ) -> remove ()
        # find mismatched brackets
        bracket_string = "".join(brackets) #  "))(("
        pair = "()"
        while pair in bracket_string:
            bracket_string = bracket_string.replace(pair, "")
        
        # replace ) from left to right
        formatted_string = s #  "))((" #  ")((" #  "((" #  "(" # ""
        for bracket in bracket_string:
            if bracket == ")":
                formatted_string = formatted_string.replace(bracket, "", 1)
        # replace ( from right to left
        formatted_string = "".join(reversed(formatted_string))
        for bracket in bracket_string:
            if bracket == "(":
                formatted_string = formatted_string.replace(bracket, "", 1)
        return "".join(reversed(formatted_string))