class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if i > 0:
                while stack and temp > stack[-1][1]:
                    prev_i = stack.pop()[0]
                    result[prev_i] = i - prev_i
            stack.append([i, temp])
        
        return result

