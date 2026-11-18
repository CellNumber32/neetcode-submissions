class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)*2):
            if i >= len(nums):
                ret.append(nums[i % len(nums)])
            else:
                ret.append(nums[i])

        return ret