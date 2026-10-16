class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanum(char):
            return ord('a')<= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z') or ord('0') <= ord(char) <= ord('9')
        
        l, r = 0, len(s) - 1
        while l<r:
            if not isAlphanum(s[l]):
                l += 1
                continue
            if not isAlphanum(s[r]):
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
