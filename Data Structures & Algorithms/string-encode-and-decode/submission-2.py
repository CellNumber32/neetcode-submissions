class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += str(len(s)) + '!' + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i<len(s):

            cur_num = ''
            cur_string = ''

            while s[i] != '!':
                cur_num += s[i]
                i += 1
            #skip through the delimiter sign (!)
            i += 1
            for char in range(int(cur_num)):
                cur_string += s[i]
                i += 1
            ret.append(cur_string)
        return ret

            
            
            

            
            
            