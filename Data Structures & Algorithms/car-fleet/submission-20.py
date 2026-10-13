class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(speed, position))
        cars.sort(key=lambda x: x[1], reverse=True)
        stack = [] # times

        for spe, pos in cars:
            time = (target - pos) / spe
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
        


