class Solution:
    def calculate(self, s: str) -> int:
        """
        3+2*2/2-1
        
        3+2-1
        
        
        13+2*22
        
        
        """
        s = s.replace(" ", "")
        
        new_string = []
        for char in s:
            
            if char in "+-/*":
                new_string.append("|")
                new_string.append(char)
                new_string.append("|")
            else:
                new_string.append(char)
        
        s = "".join(new_string)
        operations = s.split("|")
        stack_operations = []
        
        for operation in operations:
            if stack_operations and stack_operations[-1] == "*":
                stack_operations.pop()
                stack_operations[-1] = int(stack_operations[-1]) * int(operation)
            elif stack_operations and stack_operations[-1] == "/":
                stack_operations.pop()
                stack_operations[-1] = int(stack_operations[-1]) // int(operation)
            else:
                stack_operations.append(operation)
        
        result = 0
        while len(stack_operations) > 1:
            num = stack_operations.pop()
            operation = stack_operations.pop()
            if operation == "+":
                result += int(num)
            else:
                result -= int(num)
        return result + int(stack_operations.pop())