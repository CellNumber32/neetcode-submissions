class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ret = []

        for i in range(len(nums)):
            if i > 0:
                if nums[i - 1] == nums[i]:
                    continue

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    ret.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        
        return ret
