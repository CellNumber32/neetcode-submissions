class Solution:
    def isValid(self, s: str) -> bool:
        matchingBraces = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for brace in s:
            if brace in matchingBraces:
                stack.append(brace)
            elif not stack:
                return False
            else:
                if matchingBraces[stack[-1]] == brace:
                    stack.pop()
                else:
                    return False
        return True if not stack else False