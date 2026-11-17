class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = []
        curGreatest = arr[-1]
        for num in arr[::-1]:
            ret.append(curGreatest)
            if num > curGreatest:
                curGreatest = num
        ret[0] = -1
        return ret[::-1]
