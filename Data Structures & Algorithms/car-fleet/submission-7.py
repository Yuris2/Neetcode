class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [(x, y) for x, y in zip(position, speed)]
        stack = []
        array.sort(key=lambda x:x[0], reverse = True)

        for p, s in array:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        