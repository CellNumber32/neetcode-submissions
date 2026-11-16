class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = cur = 0
        for num in nums:
            if num:
                cur += 1
            else:
                if cur > ret:
                    ret = cur
                cur = 0
        return ret if cur < ret else cur