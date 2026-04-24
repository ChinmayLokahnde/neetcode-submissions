class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseOpen = {")" : "(", "]" : "[" , "}" : "{"}

        for c in s:
            if c in CloseOpen:
                if stack and stack[-1] == CloseOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

         