class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        maxLeft = []
        maxRight = [0]*len(height)
        mL = 0
        mR = 0
        maxWater = 0

        for i in range(len(height)):
            maxLeft.append(mL)
            maxRight[-(i+1)] = mR 
            if height[i] > mL:
                mL = height[i]
            if height[-(i+1)] > mR:
                mR = height[-(i+1)]

        for i in range(len(height)):
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                maxWater += min(maxLeft[i], maxRight[i]) - height[i]
        
        return maxWater