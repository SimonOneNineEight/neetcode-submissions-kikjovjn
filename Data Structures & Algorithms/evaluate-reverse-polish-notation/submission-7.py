class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if not token in operators:
                stack.append(int(token))
            else:
                left = stack.pop()
                right = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(right - left)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(float(right) / left))
        return stack[-1]