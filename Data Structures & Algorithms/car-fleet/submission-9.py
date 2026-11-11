class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        lastCarTime = 0
        carFleet = 0
        
        for p, s in sorted(pairs)[::-1]:
            if (target - p)/s > lastCarTime:
                carFleet += 1
                lastCarTime = (target - p)/s

        return carFleet
        
        