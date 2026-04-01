class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, temperature = stack.pop()
                res[index] = i - index
            stack.append([i, temp])
        
        return res
        