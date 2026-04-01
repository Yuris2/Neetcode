class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        #[temp, index]
        stack = []

        for i in range(len(temperatures)):
            currentTemp = temperatures[i]

            while stack and stack[-1][0] < currentTemp:
                log = stack.pop()
                res[log[1]] = i - log[1]
            
            stack.append([currentTemp, i])
        
        return res