class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        nums_ascend = sorted(counts.keys(), key=lambda x: counts[x])
        return nums_ascend[-k:]