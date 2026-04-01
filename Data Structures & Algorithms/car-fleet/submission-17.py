class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        cars.sort(key=lambda x:x[0], reverse = True)

        stack = []

        #y = mx + b
        for p, s in cars:
            time = (target - p) / s
            
            #Will form a fleet
            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
        
        return len(stack)
        