class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        max_consec = 0
        for num in nums:
            cur_consec = 0
            if num - 1 not in nums:
                while num in nums:
                    num += 1
                    cur_consec += 1
                if max_consec < cur_consec:
                    max_consec = cur_consec
        return max_consec