class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [(x,y) for x, y in zip(position, speed)]
        stack = []

        array.sort(key=lambda x:x[0], reverse = True)

        for p, s in array:
            #target = speed(time) + postiion => target - position / speed
            time = (target - p) / s
            stack.append(time)
            #if there is already a fleet and the current car is faster than the car
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
