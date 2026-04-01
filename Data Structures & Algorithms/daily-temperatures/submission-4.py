class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Approach.
        #1.     Create an array of all 0's to signify days for warmer
        #2.     Use a stack to store temp and index
        #3a.    If stack empty or temp at top of stack is warmer, add to stack
        #3b.    Else, res at stack index = days it takes to get warmer

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append([temperatures[i], i])
        
        return res
        
        