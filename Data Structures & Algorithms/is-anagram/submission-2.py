class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if s>t:
            sett = set(s)
        else:
            sett = set(t)
        for i in sett:
            if s.count(i) != t.count(i):
                return False
        
        return True

            