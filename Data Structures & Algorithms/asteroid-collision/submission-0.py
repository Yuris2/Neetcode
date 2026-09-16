class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []


        for i in range(len(asteroids)):          
            while (stack and abs(stack[-1]) < abs(asteroids[i]) and 
            stack[-1] > 0 and asteroids[i] < 0):
                stack.pop()
            
            if (stack and abs(stack[-1]) == abs(asteroids[i]) and
            stack[-1] > 0 and asteroids[i] < 0):
                stack.pop()
                continue
            
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                continue
            
            stack.append(asteroids[i])


        return stack

            