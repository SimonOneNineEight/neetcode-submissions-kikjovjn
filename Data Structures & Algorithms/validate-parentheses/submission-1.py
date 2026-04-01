class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []
        open_brackets = ["(", "[", "{"]

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if stack and stack[-1] == map[bracket]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            