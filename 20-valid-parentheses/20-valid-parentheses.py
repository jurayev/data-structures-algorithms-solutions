class Solution:
    def isValid(self, brackets: str) -> bool:
        pair_brackets = {"{": "}", "(": ")", "[": "]"}
        stack = [] # ]
        for bracket in brackets:
            if bracket in pair_brackets:
                stack.append(pair_brackets[bracket])
            elif stack and stack[-1] == bracket:
                stack.pop()
            else:
                return False

        return len(stack) == 0
