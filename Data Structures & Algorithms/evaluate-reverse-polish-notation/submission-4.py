class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    

        def add(num1, num2):
            return num1 + num2

        def sub(num1, num2):
            return num1 - num2

        def mul(num1, num2):
            return num1 * num2

        def div(num1, num2):
            return int(num1/num2)

        stack = []
        operators = ['+', '-', '*', '/']
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else :
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    stack.append(add(num1, num2))
                elif t == '-':
                    stack.append(sub(num1, num2))
                elif t == '*':
                    stack.append(mul(num1, num2))
                elif t == '/':
                    stack.append(div(num1, num2))
        return int(stack[-1])