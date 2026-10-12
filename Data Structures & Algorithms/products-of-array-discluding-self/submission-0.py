class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1:
            indexOfZero = nums.index(0)
            nums[indexOfZero] = 1
            product = 1
            for num in nums:
                product *= num
            ret = [0] * len(nums)
            ret[indexOfZero] = product
            return ret
        elif nums.count(0) > 1:
            return [0] * len(nums)
        else:
            product = 1
            for num in nums:
                product *= num
            ret = []
            for num in nums:
                ret.append(product // num)
            return ret

        