class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        ret = []
        for k_frequency in range(k):
            cur_max = max(counter, key=counter.get)
            ret.append(cur_max)
            del counter[cur_max]
        return ret
