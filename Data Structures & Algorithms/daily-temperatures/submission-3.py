class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index
                
            
            stack.append([temp, i])
        
        return res


        