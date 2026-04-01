class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        #index, temp
        stack = []

        for i, t in enumerate(temperatures):
            #temperature is warmer
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append([i,t])
        
        return res

        