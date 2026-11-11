class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, spe] for pos, spe in zip(position, speed)]
        carFleet = []
        for pos, spe in sorted(pairs)[::-1]:
            carFleet.append((target - pos)/spe)
            if len(carFleet) > 1 and carFleet[-1] <= carFleet[-2]:
                carFleet.pop()
        
        return len(carFleet)
        
        