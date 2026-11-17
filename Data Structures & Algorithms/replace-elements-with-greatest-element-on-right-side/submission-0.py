class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # arr=[2,4,5,3,1,2]
        ret = []
        curGreatest = arr[-1]
        for num in arr[::-1]:
            ret.append(curGreatest)
            if num > curGreatest:
                curGreatest = num
        ret[0] = -1
        return ret[::-1]
