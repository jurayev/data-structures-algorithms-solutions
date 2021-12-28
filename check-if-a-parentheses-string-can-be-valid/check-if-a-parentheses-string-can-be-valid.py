class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        Approach:
            1. Check if string can be balanced from left to right
            2. Check if string can be balanced from right to left
            3. Return true if step1 or step2 is true

        Examples:
            s = "))()))"
                "010100"
                  ^
            count = 2

            s = "((()(("
                "010100"
                   ^
            count = 3
            
            "((()))"
            "001111"
            count = 3

            ")("
            "01"
            
            c=-1
            u=1

            
        TC: O(2N)
        SC  O(1)
        """

        if len(s) % 2 == 1: return False
        
        open_count = 0
        closed_count = 0
        unlocked_count = 0
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if locked[i] == "0":
                unlocked_count += 1
            elif char == "(":
                open_count += 1
            elif char == ")":
                closed_count += 1
            if unlocked_count - open_count  + closed_count < 0:
                return False

        open_count = 0
        closed_count = 0
        unlocked_count = 0
        for i in range(len(s)):
            char = s[i]
            if locked[i] == "0":
                unlocked_count += 1
            elif char == "(":
                open_count += 1
            elif char == ")":
                closed_count += 1
            if unlocked_count + open_count - closed_count < 0:
                return False
        return True