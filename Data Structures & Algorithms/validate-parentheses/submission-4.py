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
            else:
                if stack:
                    if matchingBraces[stack[-1]] == brace:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if not stack else False