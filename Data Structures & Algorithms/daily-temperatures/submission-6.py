class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                popTemp, index = stack.pop()
                res[index] = i - index
            
            stack.append([temperatures[i], i])
        
        return res


        