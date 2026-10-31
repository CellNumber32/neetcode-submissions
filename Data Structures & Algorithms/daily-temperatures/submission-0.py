class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        searchStack = []
        ret = [0] * len(temperatures)

        for dayIndex, temperature in enumerate(temperatures):
            while searchStack and searchStack[-1][0] < temperature:
                ret[searchStack[-1][1]] = dayIndex - searchStack[-1][1]
                searchStack.pop() 
            searchStack.append([temperature, dayIndex])
        return ret