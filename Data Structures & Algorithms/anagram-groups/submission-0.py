class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = {}
        for val in strs:
            charsCount = [0] * 26
            # ord(char) - 97
            for char in val:
                charsCount[ord(char) - 97] += 1

            if tuple(charsCount) in groupAnagrams:
                groupAnagrams[tuple(charsCount)].append(val)
            else:
                groupAnagrams[tuple(charsCount)] = [val]
        ret = []
        for anagramPair in groupAnagrams:
            ret.append(groupAnagrams.get(anagramPair))
        
        return ret

