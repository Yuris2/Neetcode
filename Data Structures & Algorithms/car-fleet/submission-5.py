class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [[x,y] for x, y in zip(position, speed)]
        stack = []

        array.sort(key = lambda t:t[0], reverse = True)

        #y = mx + b, target - position
        for pos, speed in array:
            time = (target - pos) / speed
            stack.append(time)

            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
            

        return len(stack)

        