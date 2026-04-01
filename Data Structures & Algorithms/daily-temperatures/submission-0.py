class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            #While the stack is not empty and the current temp is greater than the 
            #temp at the top of the stack
            while stack and stack[-1][0] < temp:
                topVal = stack.pop()
                res[topVal[1]] = i - topVal[1]
            
            stack.append([temp, i])
        
        return res
        