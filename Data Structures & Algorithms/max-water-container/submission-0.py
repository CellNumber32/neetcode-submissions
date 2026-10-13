class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0
        while l < r:
            cur_Water = min(heights[l], heights[r]) * (r - l)
            if cur_Water > maxWater:
                maxWater = cur_Water
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
