class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sett = counts.keys()
        nums_ascend = sorted(sett, key=lambda x: counts[x])
        return nums_ascend[-k:]