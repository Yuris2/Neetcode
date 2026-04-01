class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]* n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, t = stack.pop()
                res[index] = (i - index)
            stack.append([i, temp])
        
        return res