class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        try:
            for c in s:
                if (c == ')' and stack[-1] == '('):
                    stack.pop()
                elif (c == '}' and stack[-1] == '{'):
                    stack.pop()
                elif (c == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    stack.append(c)
        except IndexError:
            return False
        
        if stack == []:
            return True
        return False