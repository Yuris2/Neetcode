class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(x,y) for x, y in zip(position, speed)]

        cars.sort(key=lambda x:x[0], reverse = True)

        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


        