class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            left = a < 0
            if not left or not stack:
                stack.append(a)
            else:
                #Same direction
                #moving left and greater than top
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == abs(a):
                    stack.pop()
                #Else bigger asteroid
        
        return stack

        