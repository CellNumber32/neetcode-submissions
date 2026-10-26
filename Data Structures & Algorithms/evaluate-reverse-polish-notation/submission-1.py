import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        def resolve(operation):
            el2 = int(stack.pop())
            el = int(stack.pop())
            if operation == "*":
                stack.append(el*el2)
            elif operation == "/":
                stack.append(int(el/el2))
            elif operation == "-":
                stack.append(el-el2)
            else:    
                stack.append(el+el2)
        for token in tokens:
            if token.isdigit():
                stack.append(token)
            elif len(token) > 1:
                stack.append(token)
            else:
                resolve(token)
        
        return int(stack[-1])

