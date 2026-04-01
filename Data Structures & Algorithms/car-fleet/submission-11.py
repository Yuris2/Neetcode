class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Get an array that combines both the speed and position
        cars = [(s,p) for s, p in zip(speed, position)]

        cars.sort(key=lambda x:x[1], reverse = True)

        stack = []

        for speed,pos in cars:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
        