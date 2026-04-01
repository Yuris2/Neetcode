class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        meta = [(pos, speed) for pos,speed in zip(position,speed)]
        meta.sort(key = lambda x:x[0], reverse = True)

        for pos, speed in meta:
            time = (target - pos) / speed
            stack.append(time)

            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


        