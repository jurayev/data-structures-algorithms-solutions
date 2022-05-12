class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        
        [10, 6, -132 /]
        """
        
        stack = []
        
        for token in tokens:
            if token == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            elif token == "*":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif token == "+":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            else:
                stack.append(int(token)) 
        return stack.pop()